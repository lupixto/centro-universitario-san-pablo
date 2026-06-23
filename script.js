const navToggle = document.querySelector(".nav-toggle");
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
