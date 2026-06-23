import json
import os
import re
from pathlib import Path

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

import build_phase1_site as base

ROOT = Path(__file__).resolve().parents[1]
SITE = base.SITE
PENDING = base.PENDING

PUBLISHABLE = [
    "index.html",
    "oferta-academica/index.html",
    *[p["url"] for p in base.PROGRAMS],
    "admisiones/index.html",
    "admisiones/costos-promociones.html",
    "admisiones/preguntas-frecuentes.html",
    "planteles/index.html",
    "planteles/hidalgo.html",
    "planteles/centro.html",
    "vida-universitaria/galeria.html",
    "contacto/index.html",
    "legales/aviso-privacidad.html",
]


def prefix_for(path: Path) -> str:
    return "../" * (len(path.parts) - 1)


def page_url(rel: str) -> str:
    if rel == "index.html":
        return f"{SITE}/"
    if rel.endswith("index.html"):
        return f"{SITE}/{rel[:-10]}"
    return f"{SITE}/{rel}"


def crumb_label(part: str) -> str:
    labels = {
        "oferta-academica": "Oferta académica",
        "admisiones": "Admisiones",
        "universidad": "Universidad",
        "vida-universitaria": "Vida universitaria",
        "planteles": "Planteles",
        "contacto": "Contacto",
        "legales": "Legales",
        "index": "Inicio",
        "derecho": "Derecho",
        "pedagogia": "Pedagogía",
        "administracion": "Administración",
        "contabilidad": "Contabilidad",
        "ingenieria-industrial": "Ingeniería Industrial",
        "comercio-internacional": "Comercio Internacional y Aduanal",
        "doctorado-educacion": "Doctorado en Educación",
        "costos-promociones": "Costos y promociones",
        "preguntas-frecuentes": "Preguntas frecuentes",
        "hidalgo": "Plantel Hidalgo",
        "centro": "Plantel Centro",
        "galeria": "Galería",
        "aviso-privacidad": "Aviso de privacidad",
    }
    return labels.get(part, part.replace("-", " ").title())


def breadcrumbs(rel: str) -> str:
    path = Path(rel)
    prefix = prefix_for(path)
    if rel == "index.html":
        return ""
    items = [("Inicio", f"{prefix}index.html")]
    parts = list(path.parts)
    if len(parts) > 1:
        folder = parts[0]
        index_path = f"{prefix}{folder}/index.html"
        if (ROOT / folder / "index.html").exists():
            items.append((crumb_label(folder), index_path))
    stem = path.stem
    if stem != "index":
        items.append((crumb_label(stem), ""))
    html = ['<nav class="breadcrumbs container" aria-label="Ruta de navegación"><ol>']
    for index, (label, url) in enumerate(items, 1):
        if url and index != len(items):
            html.append(f'<li><a href="{url}">{label}</a></li>')
        else:
            html.append(f'<li aria-current="page">{label}</li>')
    html.append("</ol></nav>")
    return "".join(html)


def json_ld(rel: str, title: str) -> str:
    graph = [
        {
            "@type": ["CollegeOrUniversity", "EducationalOrganization"],
            "@id": f"{SITE}/#institucion",
            "name": "Centro Universitario San Pablo",
            "url": f"{SITE}/",
            "logo": f"{SITE}/assets/logo-san-pablo-320.webp",
            "slogan": "SPIRITVS GLADIVS",
            "telephone": ["+52 477 713 4804", "+52 477 265 9137"],
            "sameAs": [base.SOCIALS["facebook"], base.SOCIALS["instagram"]],
            "address": [
                {
                    "@type": "PostalAddress",
                    "streetAddress": "Calle Hidalgo 412, Obregón",
                    "postalCode": "37320",
                    "addressLocality": "León de los Aldama",
                    "addressRegion": "Guanajuato",
                    "addressCountry": "MX",
                },
                {
                    "@type": "PostalAddress",
                    "streetAddress": "Emiliano Zapata #202A, Segundo Piso, Zona Centro",
                    "postalCode": "37000",
                    "addressLocality": "León de los Aldama",
                    "addressRegion": "Guanajuato",
                    "addressCountry": "MX",
                },
            ],
            "contactPoint": [
                {"@type": "ContactPoint", "telephone": "+52 477 713 4804", "contactType": "admissions", "areaServed": "León, Guanajuato"},
                {"@type": "ContactPoint", "telephone": "+52 477 265 9137", "contactType": "admissions", "areaServed": "León, Guanajuato"},
            ],
        }
    ]
    for program in base.PROGRAMS:
        graph.append(
            {
                "@type": "Course",
                "name": program["name"],
                "description": program["description"],
                "url": f"{SITE}/{program['url']}",
                "provider": {"@id": f"{SITE}/#institucion"},
            }
        )
    if rel.endswith("preguntas-frecuentes.html"):
        graph.append(
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": "¿Las carreras cuentan con RVOE?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. La institución confirma que las carreras cuentan con RVOE; las claves y documentos están pendientes de publicación."}},
                    {"@type": "Question", "name": "¿Puedo estudiar los sábados?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Los programas son presenciales y cuentan con opción sabatina. El horario específico debe confirmarse con un asesor."}},
                    {"@type": "Question", "name": "¿La promoción tiene vigencia?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Está sujeta a vigencia, disponibilidad y confirmación directa con el plantel."}},
                ],
            }
        )
    if rel != "index.html":
        path = Path(rel)
        items = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{SITE}/"}]
        pos = 2
        if len(path.parts) > 1:
            folder = path.parts[0]
            items.append({"@type": "ListItem", "position": pos, "name": crumb_label(folder), "item": f"{SITE}/{folder}/"})
            pos += 1
        if path.stem != "index":
            items.append({"@type": "ListItem", "position": pos, "name": crumb_label(path.stem), "item": page_url(rel)})
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":")) + "</script>"


def unique_title(rel: str, html: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, flags=re.S)
    if match:
        return re.sub(r"\s+", " ", match.group(1)).strip()
    return "Centro Universitario San Pablo"


def patch_head(rel: str, html: str) -> str:
    title = unique_title(rel, html)
    if "application/ld+json" not in html:
        html = html.replace("</head>", f"  {json_ld(rel, title)}\n</head>")
    return html


def patch_breadcrumbs(rel: str, html: str) -> str:
    if 'class="breadcrumbs' in html or rel == "index.html":
        return html
    return html.replace('  <main id="contenido">', '  <main id="contenido">\n' + breadcrumbs(rel), 1)


def patch_forms(html: str) -> str:
    if 'id="contact-form"' not in html:
        return html
    if 'id="email"' not in html:
        html = html.replace(
            '<label for="program">Programa de interés</label>',
            '<label for="email">Correo electrónico <span class="optional-label">opcional</span></label>\n'
            '        <input id="email" name="email" type="email" autocomplete="email" placeholder="correo@ejemplo.com" aria-describedby="email-error">\n'
            '        <span class="field-error" id="email-error" aria-live="polite"></span>\n'
            '        <label for="program">Programa de interés</label>',
        )
    return html


def patch_images(html: str) -> str:
    if "equipo-san-pablo.webp" in html and "fetchpriority" not in html:
        html = html.replace('alt="Comunidad del Centro Universitario San Pablo"', 'alt="Comunidad del Centro Universitario San Pablo" fetchpriority="high"')
    replacements = {
        'src="../assets/comunidad-academica.webp" width="1600"': 'src="../assets/comunidad-academica.webp" srcset="../assets/comunidad-academica-640.webp 640w, ../assets/comunidad-academica.webp 1600w" sizes="(max-width: 760px) calc(100vw - 28px), 56vw" width="1600"',
        'src="../assets/congreso-estudiantes.webp" width="2048"': 'src="../assets/congreso-estudiantes.webp" srcset="../assets/congreso-estudiantes-640.webp 640w, ../assets/congreso-estudiantes.webp 2048w" sizes="(max-width: 760px) calc(100vw - 28px), 28vw" width="2048"',
        'src="../assets/graduacion-grupo.webp" width="1600"': 'src="../assets/graduacion-grupo.webp" srcset="../assets/graduacion-grupo-640.webp 640w, ../assets/graduacion-grupo.webp 1600w" sizes="(max-width: 760px) calc(100vw - 28px), 28vw" width="1600"',
        'src="../assets/reconocimiento-egresada.webp" width="1142"': 'src="../assets/reconocimiento-egresada.webp" srcset="../assets/reconocimiento-egresada-640.webp 457w, ../assets/reconocimiento-egresada.webp 1142w" sizes="(max-width: 760px) calc(100vw - 28px), 28vw" width="1142"',
        'src="../assets/actividad-cultural.webp" width="2048"': 'src="../assets/actividad-cultural.webp" srcset="../assets/actividad-cultural-640.webp 640w, ../assets/actividad-cultural.webp 2048w" sizes="(max-width: 760px) calc(100vw - 28px), 28vw" width="2048"',
        'src="../assets/plantel-emiliano-zapata.webp" width="960"': 'src="../assets/plantel-emiliano-zapata.webp" srcset="../assets/plantel-emiliano-zapata-640.webp 480w, ../assets/plantel-emiliano-zapata.webp 960w" sizes="(max-width: 760px) calc(100vw - 28px), 48vw" width="960"',
    }
    for old, new in replacements.items():
        html = html.replace(old, new)
    return html


def patch_html_files():
    for path in ROOT.rglob("*.html"):
        if any(part in {"backup-fase-1", "backup-fase-2", "backup-fase-3", "backups"} for part in path.parts):
            continue
        rel = path.relative_to(ROOT).as_posix()
        html = path.read_text(encoding="utf-8")
        html = patch_head(rel, html)
        html = patch_breadcrumbs(rel, html)
        html = patch_forms(html)
        html = patch_images(html)
        path.write_text(html.rstrip() + "\n", encoding="utf-8")


def write_analytics_config():
    (ROOT / "scripts" / "analytics-config.js").write_text(
        """window.CUSP_ANALYTICS_CONFIG = {
  GA_MEASUREMENT_ID: "",
  META_PIXEL_ID: "",
  TIKTOK_PIXEL_ID: ""
};
""",
        encoding="utf-8",
    )


def write_analytics_js():
    (ROOT / "analytics.js").write_text(
        """(function () {
  const config = window.CUSP_ANALYTICS_CONFIG || {};

  window.trackSiteEvent = function (eventName, parameters) {
    const payload = parameters || {};
    if (window.gtag && config.GA_MEASUREMENT_ID) {
      window.gtag("event", eventName, payload);
    }
    if (window.fbq && config.META_PIXEL_ID) {
      window.fbq("trackCustom", eventName, payload);
    }
    if (window.ttq && config.TIKTOK_PIXEL_ID) {
      window.ttq.track(eventName, payload);
    }
  };

  if (config.GA_MEASUREMENT_ID) {
    const script = document.createElement("script");
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(config.GA_MEASUREMENT_ID)}`;
    document.head.appendChild(script);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", config.GA_MEASUREMENT_ID);
  }

  if (config.META_PIXEL_ID) {
    window.fbq = window.fbq || function () {
      window.fbq.callMethod ? window.fbq.callMethod.apply(window.fbq, arguments) : window.fbq.queue.push(arguments);
    };
    window.fbq.queue = window.fbq.queue || [];
    window.fbq.loaded = true;
    window.fbq.version = "2.0";
    const script = document.createElement("script");
    script.async = true;
    script.src = "https://connect.facebook.net/en_US/fbevents.js";
    document.head.appendChild(script);
    window.fbq("init", config.META_PIXEL_ID);
    window.fbq("track", "PageView");
  }

  if (config.TIKTOK_PIXEL_ID) {
    window.ttq = window.ttq || {
      track: function () {},
      page: function () {}
    };
  }
})();
""",
        encoding="utf-8",
    )


def patch_script_tags():
    for path in ROOT.rglob("*.html"):
        if any(part in {"backup-fase-1", "backup-fase-2", "backup-fase-3", "backups"} for part in path.parts):
            continue
        prefix = prefix_for(path.relative_to(ROOT))
        html = path.read_text(encoding="utf-8")
        config_src = f'{prefix}scripts/analytics-config.js'
        if config_src not in html:
            html = html.replace(f'<script src="{prefix}analytics.js"></script>', f'<script src="{config_src}"></script>\n  <script src="{prefix}analytics.js"></script>')
        path.write_text(html.rstrip() + "\n", encoding="utf-8")


def write_script_js():
    (ROOT / "script.js").write_text(
        r"""const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector("#nav-menu");
const siteHeader = document.querySelector("[data-site-header]");

const campusWhatsApp = {
  hidalgo: { name: "Plantel Hidalgo", phone: "524777134804" },
  centro: { name: "Plantel Centro", phone: "524772659137" },
};

const programNames = {
  derecho: "Derecho",
  pedagogia: "Pedagogía",
  administracion: "Administración",
  contabilidad: "Contabilidad",
  "ingenieria-industrial": "Ingeniería Industrial",
  "comercio-internacional": "Comercio Internacional y Aduanal",
  "doctorado-educacion": "Doctorado en Educación",
};

const closeMenu = () => {
  navMenu?.classList.remove("is-open");
  navToggle?.setAttribute("aria-expanded", "false");
  navToggle?.setAttribute("aria-label", "Abrir menú");
  document.body.classList.remove("menu-open");
  document.querySelectorAll(".has-dropdown.is-open").forEach((item) => {
    item.classList.remove("is-open");
    item.querySelector("button")?.setAttribute("aria-expanded", "false");
  });
};

if (navToggle && navMenu) {
  navToggle.addEventListener("click", () => {
    const isOpen = navMenu.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
    navToggle.setAttribute("aria-label", isOpen ? "Cerrar menú" : "Abrir menú");
    document.body.classList.toggle("menu-open", isOpen);
  });

  document.querySelector("[data-menu-close]")?.addEventListener("click", closeMenu);

  navMenu.addEventListener("click", (event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;

    const dropdownButton = target.closest(".has-dropdown > button");
    if (dropdownButton) {
      const item = dropdownButton.closest(".has-dropdown");
      const isOpen = item.classList.toggle("is-open");
      dropdownButton.setAttribute("aria-expanded", String(isOpen));
      return;
    }

    if (target.closest("a")) closeMenu();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && navMenu.classList.contains("is-open")) {
      closeMenu();
      navToggle.focus();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 1020) closeMenu();
  });
}

if (siteHeader) {
  const updateHeader = () => siteHeader.classList.toggle("is-scrolled", window.scrollY > 18);
  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });
}

document.querySelectorAll("[data-current-year]").forEach((element) => {
  element.textContent = String(new Date().getFullYear());
});

const params = new URLSearchParams(location.search);
const programParam = params.get("programa");
const programSelect = document.querySelector("#program");

if (programParam && programSelect instanceof HTMLSelectElement && programNames[programParam]) {
  programSelect.value = programParam;
  window.trackSiteEvent?.("select_program", { program: programNames[programParam], source: "url" });
}

const search = document.querySelector("[data-program-search]");
if (search) {
  const cards = document.querySelectorAll("[data-program-card]");
  search.addEventListener("input", () => {
    const value = search.value.trim().toLowerCase();
    cards.forEach((card) => {
      card.hidden = Boolean(value && !card.textContent.toLowerCase().includes(value));
    });
  });
}

const filters = document.querySelectorAll("[data-filter]");
if (filters.length) {
  const cards = document.querySelectorAll("[data-program-card]");
  const apply = () => {
    const values = {};
    filters.forEach((filter) => {
      values[filter.dataset.filter] = filter.value;
    });
    cards.forEach((card) => {
      const visible =
        (!values.level || card.dataset.level === values.level) &&
        (!values.area || card.dataset.area === values.area) &&
        (!values.campus || card.dataset.campus === values.campus);
      card.hidden = !visible;
    });
  };
  filters.forEach((filter) => filter.addEventListener("change", apply));
}

document.querySelectorAll("#program").forEach((select) => {
  select.addEventListener("change", () => {
    window.trackSiteEvent?.("select_program", { program: select.selectedOptions[0]?.textContent.trim() || "" });
  });
});

document.querySelectorAll("#campus").forEach((select) => {
  select.addEventListener("change", () => {
    const campus = campusWhatsApp[select.value];
    window.trackSiteEvent?.("select_campus", { campus: campus?.name || select.value });
  });
});

const validateMexicanPhone = (value) => {
  const digits = value.replace(/\D/g, "");
  return /^\d{10}$/.test(digits) || /^52\d{10}$/.test(digits);
};

document.querySelectorAll("#contact-form").forEach((contactForm) => {
  const formErrorSummary = contactForm.querySelector("#form-errors");
  const fields = {
    name: contactForm.querySelector("#name"),
    phone: contactForm.querySelector("#phone"),
    email: contactForm.querySelector("#email"),
    program: contactForm.querySelector("#program"),
    campus: contactForm.querySelector("#campus"),
    privacy: contactForm.querySelector("#privacy-consent"),
    message: contactForm.querySelector("#message"),
  };

  const setFieldError = (fieldName, message) => {
    const field = fields[fieldName];
    const error = contactForm.querySelector(`#${fieldName === "privacy" ? "privacy" : fieldName}-error`);
    if (field) field.setAttribute("aria-invalid", message ? "true" : "false");
    if (error) error.textContent = message;
  };

  const validateForm = () => {
    const errors = [];
    Object.keys(fields).forEach((key) => setFieldError(key, ""));

    const name = fields.name?.value.trim() || "";
    const phone = fields.phone?.value.trim() || "";
    const email = fields.email?.value.trim() || "";

    if (name.length < 3) {
      const message = "Escribe tu nombre completo con al menos 3 caracteres.";
      setFieldError("name", message);
      errors.push({ field: fields.name, message });
    }

    if (!validateMexicanPhone(phone)) {
      const message = "Ingresa un teléfono mexicano válido de 10 dígitos, con o sin +52.";
      setFieldError("phone", message);
      errors.push({ field: fields.phone, message });
    }

    if (email && fields.email instanceof HTMLInputElement && !fields.email.validity.valid) {
      const message = "Ingresa un correo electrónico válido o deja el campo vacío.";
      setFieldError("email", message);
      errors.push({ field: fields.email, message });
    }

    if (!fields.program?.value) {
      const message = "Selecciona la carrera o programa que te interesa.";
      setFieldError("program", message);
      errors.push({ field: fields.program, message });
    }

    if (!fields.campus?.value || !campusWhatsApp[fields.campus.value]) {
      const message = "Selecciona el plantel al que deseas enviar tu solicitud.";
      setFieldError("campus", message);
      errors.push({ field: fields.campus, message });
    }

    if (!fields.privacy?.checked) {
      const message = "Debes aceptar el aviso de privacidad para continuar.";
      setFieldError("privacy", message);
      errors.push({ field: fields.privacy, message });
    }

    if (formErrorSummary) {
      formErrorSummary.hidden = errors.length === 0;
      formErrorSummary.textContent = errors.length
        ? `Revisa ${errors.length} ${errors.length === 1 ? "campo" : "campos"} antes de continuar.`
        : "";
    }

    return errors;
  };

  Object.entries(fields).forEach(([fieldName, field]) => {
    field?.addEventListener(fieldName === "privacy" ? "change" : "input", () => {
      setFieldError(fieldName, "");
      if (formErrorSummary) formErrorSummary.hidden = true;
    });
  });

  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const errors = validateForm();
    if (errors.length) {
      formErrorSummary?.focus();
      errors[0].field?.focus();
      return;
    }

    const formData = new FormData(contactForm);
    const campus = campusWhatsApp[formData.get("campus")];
    const name = String(formData.get("name") || "").trim();
    const option = fields.program.selectedOptions[0];
    const program = option ? option.textContent.trim() : String(formData.get("program") || "");
    const message = String(formData.get("message") || "").trim() || "Sin mensaje adicional.";

    const whatsappMessage = [
      `Hola, mi nombre es ${name}.`,
      "",
      `Quiero recibir información sobre ${program} en ${campus.name}.`,
      "",
      "Me interesa conocer:",
      "",
      "• Plan de estudios",
      "• Horarios",
      "• Requisitos",
      "• Costos",
      "• Promoción vigente",
      "• Fecha de inicio",
      "",
      "Mensaje adicional:",
      "",
      message,
    ].join("\n");

    window.trackSiteEvent?.("form_submit", { program, campus: campus.name });
    window.trackSiteEvent?.("generate_lead", { method: "whatsapp_form", program, campus: campus.name });
    window.open(`https://wa.me/${campus.phone}?text=${encodeURIComponent(whatsappMessage)}`, "_blank", "noopener");
  });
});

document.addEventListener("click", (event) => {
  const link = event.target instanceof Element ? event.target.closest("a") : null;
  if (!link) return;

  const href = link.getAttribute("href") || "";
  const text = link.textContent.trim();

  if (href.includes("wa.me/")) window.trackSiteEvent?.("click_whatsapp", { destination: href });
  else if (href.startsWith("tel:")) window.trackSiteEvent?.("click_call", { phone: href.replace("tel:", "") });
  else if (href.includes("maps.app") || href.includes("google.com/maps")) window.trackSiteEvent?.("click_map", { destination: href });

  if (href.includes("oferta-academica")) window.trackSiteEvent?.("click_program", { link_text: text });
  if (/plan de estudios/i.test(text)) window.trackSiteEvent?.("view_plan", { link_text: text });
  if (/agendar visita/i.test(text)) window.trackSiteEvent?.("schedule_visit", { link_text: text });
  if (link.matches("[data-plan-download]")) window.trackSiteEvent?.("download_pdf", { file: href, program: link.dataset.program || "" });
});

const galleryButtons = document.querySelectorAll(".gallery-open");
if (galleryButtons.length) {
  const lightbox = document.createElement("div");
  let lastTrigger = null;
  lightbox.className = "image-lightbox";
  lightbox.setAttribute("role", "dialog");
  lightbox.setAttribute("aria-modal", "true");
  lightbox.setAttribute("aria-label", "Vista ampliada de fotografía");
  lightbox.innerHTML = '<button type="button" aria-label="Cerrar imagen">×</button><img alt="">';
  document.body.appendChild(lightbox);

  const image = lightbox.querySelector("img");
  const closeButton = lightbox.querySelector("button");
  const close = () => {
    lightbox.classList.remove("is-open");
    document.body.classList.remove("menu-open");
    lastTrigger?.focus();
  };

  galleryButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const source = button.querySelector("img");
      if (!source) return;
      lastTrigger = button;
      image.src = source.src;
      image.alt = source.alt;
      lightbox.classList.add("is-open");
      document.body.classList.add("menu-open");
      closeButton.focus();
    });
  });

  lightbox.addEventListener("click", (event) => {
    if (event.target === lightbox) close();
  });
  closeButton.addEventListener("click", close);
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && lightbox.classList.contains("is-open")) close();
  });
}
""",
        encoding="utf-8",
    )


def patch_styles():
    path = ROOT / "styles.css"
    css = path.read_text(encoding="utf-8")
    additions = """
.optional-label{font-weight:700;color:var(--muted);font-size:.88em}
.breadcrumbs{padding-top:18px;font-size:13px;color:var(--muted)}
.breadcrumbs ol{margin:0;padding:0;list-style:none;display:flex;gap:8px;flex-wrap:wrap}
.breadcrumbs li:not(:last-child)::after{content:"/";margin-left:8px;color:var(--gold)}
.breadcrumbs a{text-decoration:none;color:var(--gold-2)}
.breadcrumbs a:hover{text-decoration:underline}
[aria-invalid="true"]{border-color:#ff8b8b!important;box-shadow:0 0 0 3px rgba(255,139,139,.2)}
button,.button,a,input,select,textarea,summary{touch-action:manipulation}
.nav-menu a,.button,.nav-toggle,.has-dropdown>button{min-width:44px}
.table-wrap{max-width:100%;overflow-x:auto}
.gallery-open:focus-visible{outline:3px solid var(--gold-2);outline-offset:4px}
@media (max-width:360px){.hero h1,.page-hero h1{font-size:32px}.brand strong{font-size:12px}.brand small{font-size:10px}.nav-toggle{width:48px;height:48px}.mobile-bottom-bar{left:8px;right:8px}}
"""
    if ".breadcrumbs" not in css:
        css += "\n" + additions
    css = css.replace("@media (prefers-reduced-motion:reduce){", "@media (prefers-reduced-motion:reduce){")
    path.write_text(css.rstrip() + "\n", encoding="utf-8")


def write_sitemap():
    urls = []
    for rel in PUBLISHABLE:
        urls.append(
            f"  <url><loc>{page_url(rel)}</loc><lastmod>2026-06-22</lastmod><changefreq>monthly</changefreq><priority>{'1.0' if rel == 'index.html' else '0.7'}</priority></url>"
        )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")


def write_readme():
    (ROOT / "README.md").write_text(
        """# Centro Universitario San Pablo

Portal universitario estático multipágina compatible con GitHub Pages.

## Estructura

- `index.html`: portada.
- `oferta-academica/`: catálogo y páginas por programa.
- `admisiones/`: proceso, costos, fechas, requisitos y preguntas.
- `universidad/`: institución, modelo educativo, RVOE y directorio.
- `vida-universitaria/`: galería, noticias, eventos y egresados.
- `planteles/`: Plantel Hidalgo y Plantel Centro.
- `contacto/`: formulario principal.
- `legales/`: aviso de privacidad y términos.
- `assets/`: imágenes originales y WebP.
- `scripts/analytics-config.js`: IDs opcionales de analítica.
- `DATOS-PENDIENTES.md`: lista de información que falta confirmar.

## Ejecutar localmente

Abre `index.html` con doble clic. El sitio no requiere framework ni servidor para funcionar.

## Publicar en GitHub Pages

Sube los archivos de la raíz del proyecto al repositorio, entra a `Settings > Pages` y publica desde la rama principal en `/(root)`.

## Editar carreras

Actualiza las páginas dentro de `oferta-academica/`, el catálogo `oferta-academica/index.html`, el selector `#program` en formularios y el listado `programNames` en `script.js`.

## Editar RVOE

Completa `universidad/rvoe.html` y las secciones RVOE de cada programa. No elimines `.is-pending` hasta tener clave, autoridad, fecha, modalidad, plantel y documento oficial.

## Editar costos y promociones

Busca `$1,300`, `$699` y `$1,800`. Actualiza portada, admisiones, páginas de programa y preguntas frecuentes. No inventes vigencias o restricciones.

## Editar fechas

Actualiza `admisiones/fechas-inicio.html` y las secciones de fecha de inicio en cada programa.

## Editar teléfonos y WhatsApp

Actualiza teléfonos en HTML, footer y el objeto `campusWhatsApp` en `script.js`. WhatsApp debe usar formato internacional: `52` + 10 dígitos.

## Editar planteles

Actualiza `planteles/index.html`, `planteles/hidalgo.html`, `planteles/centro.html`, enlaces de mapa y carreras disponibles por plantel.

## Agregar testimonios, noticias o eventos

Usa las tarjetas ya preparadas en `vida-universitaria/`. Publica únicamente contenido real y autorizado.

## Subir planes de estudio

Agrega PDFs oficiales en una carpeta nueva, por ejemplo `assets/planes/`, y enlázalos con `data-plan-download` para medir descargas.

## Activar analítica

Edita `scripts/analytics-config.js`:

```js
GA_MEASUREMENT_ID = "";
META_PIXEL_ID = "";
TIKTOK_PIXEL_ID = "";
```

Si los campos están vacíos, no se carga ninguna herramienta. Eventos preparados: WhatsApp, teléfono, formulario, mapa, carrera, plan de estudios, PDF, visita, plantel y programa.

## Ocultar bloques pendientes

Los bloques pendientes usan `.is-pending`. Puedes ocultarlos con CSS cuando el cliente lo pida:

```css
.is-pending { display: none; }
```

## Comprobar enlaces

Usa el validador local `scripts/validate_site.py` o revisa manualmente navegación, teléfonos, WhatsApp, mapas y redes.

## Hacer respaldo

Copia los archivos principales y carpetas antes de editar. Este proyecto ya tiene respaldos `backup-fase-1`, `backup-fase-2` y `backup-fase-3`.
""",
        encoding="utf-8",
    )


def main():
    write_analytics_config()
    write_analytics_js()
    patch_html_files()
    patch_script_tags()
    write_script_js()
    patch_styles()
    write_sitemap()
    write_readme()


if __name__ == "__main__":
    main()
