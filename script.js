const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector("#nav-menu");
const contactForm = document.querySelector("#contact-form");
const siteHeader = document.querySelector(".site-header");
const programSelect = document.querySelector("#program");

const campusWhatsApp = {
  hidalgo: {
    name: "Plantel Hidalgo",
    phone: "524777134804",
  },
  centro: {
    name: "Plantel Centro",
    phone: "524772659137",
  },
};

if (navToggle && navMenu) {
  const closeMenu = () => {
    navMenu.classList.remove("is-open");
    navToggle.setAttribute("aria-expanded", "false");
    navToggle.setAttribute("aria-label", "Abrir menú");
    document.body.classList.remove("menu-open");
  };

  navToggle.addEventListener("click", () => {
    const isOpen = navMenu.classList.toggle("is-open");

    navToggle.setAttribute("aria-expanded", String(isOpen));
    navToggle.setAttribute("aria-label", isOpen ? "Cerrar menú" : "Abrir menú");
    document.body.classList.toggle("menu-open", isOpen);
  });

  navMenu.addEventListener("click", (event) => {
    if (event.target instanceof Element && event.target.closest("a")) {
      closeMenu();
    }
  });

  document.addEventListener("click", (event) => {
    if (
      navMenu.classList.contains("is-open") &&
      event.target instanceof Node &&
      !navMenu.contains(event.target) &&
      !navToggle.contains(event.target)
    ) {
      closeMenu();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && navMenu.classList.contains("is-open")) {
      closeMenu();
      navToggle.focus();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 1020) {
      closeMenu();
    }
  });
}

document.querySelectorAll('[aria-disabled="true"]').forEach((element) => {
  element.addEventListener("click", (event) => {
    event.preventDefault();
  });
});

if (contactForm) {
  const formErrorSummary = contactForm.querySelector("#form-errors");
  const fields = {
    name: contactForm.querySelector("#name"),
    phone: contactForm.querySelector("#phone"),
    program: contactForm.querySelector("#program"),
    campus: contactForm.querySelector("#campus"),
    privacy: contactForm.querySelector("#privacy-consent"),
  };

  const setFieldError = (fieldName, message) => {
    const field = fields[fieldName];
    const error = contactForm.querySelector(`#${fieldName === "privacy" ? "privacy" : fieldName}-error`);

    if (field) field.setAttribute("aria-invalid", message ? "true" : "false");
    if (error) error.textContent = message;
  };

  const validateForm = () => {
    const errors = [];
    const name = fields.name?.value.trim() || "";
    const phone = fields.phone?.value.trim() || "";
    const phoneDigits = phone.replace(/\D/g, "");
    const validPhone = /^\d{10}$/.test(phoneDigits) || /^52\d{10}$/.test(phoneDigits);

    setFieldError("name", "");
    setFieldError("phone", "");
    setFieldError("program", "");
    setFieldError("campus", "");
    setFieldError("privacy", "");

    if (name.length < 3) {
      const message = "Escribe tu nombre completo con al menos 3 caracteres.";
      setFieldError("name", message);
      errors.push({ field: fields.name, message });
    }

    if (!validPhone) {
      const message = "Ingresa un teléfono mexicano válido de 10 dígitos, con o sin el prefijo +52.";
      setFieldError("phone", message);
      errors.push({ field: fields.phone, message });
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
    const selectedCampus = formData.get("campus");
    const campus = campusWhatsApp[selectedCampus];
    const name = String(formData.get("name") || "").trim();
    const program = String(formData.get("program") || "");

    const whatsappMessage = [
      `Hola, mi nombre es ${name}.`,
      `Quiero recibir información sobre ${program} en ${campus.name}.`,
      "",
      "Me interesa conocer:",
      "• Plan de estudios",
      "• Horarios",
      "• Requisitos",
      "• Promoción vigente",
      "• Fecha de inicio",
    ].join("\n");

    const whatsappUrl = `https://wa.me/${campus.phone}?text=${encodeURIComponent(whatsappMessage)}`;
    window.trackSiteEvent?.("generate_lead", {
      method: "whatsapp_form",
      program,
      campus: campus.name,
    });
    window.trackSiteEvent?.("form_submit", { program, campus: campus.name });
    window.open(whatsappUrl, "_blank", "noopener");
  });
}

document.querySelectorAll("[data-program-choice]").forEach((button) => {
  button.addEventListener("click", () => {
    if (programSelect instanceof HTMLSelectElement) {
      programSelect.value = button.dataset.programChoice || "";
    }
  });
});

document.querySelectorAll("[data-campus-choice]").forEach((button) => {
  button.addEventListener("click", () => {
    const campusSelect = document.querySelector("#campus");
    if (campusSelect instanceof HTMLSelectElement) {
      campusSelect.value = button.dataset.campusChoice || "";
    }
  });
});

document.addEventListener("click", (event) => {
  const link = event.target instanceof Element ? event.target.closest("a") : null;
  if (!link) return;

  const href = link.getAttribute("href") || "";
  if (href.includes("wa.me/")) {
    window.trackSiteEvent?.("click_whatsapp", { destination: href });
  } else if (href.startsWith("tel:")) {
    window.trackSiteEvent?.("click_call", { phone: href.replace("tel:", "") });
  } else if (href.includes("maps.app") || href.includes("google.com/maps")) {
    window.trackSiteEvent?.("get_directions", { destination: href });
  } else if (href === "#oferta") {
    window.trackSiteEvent?.("view_academic_offer", { link_text: link.textContent.trim() });
  }

  if (link.matches("[data-plan-download]")) {
    window.trackSiteEvent?.("download_plan", {
      program: link.dataset.program || "",
      file: href,
    });
  }
});

document.querySelectorAll(".program-details").forEach((details) => {
  details.addEventListener("toggle", () => {
    if (!details.open) return;
    const program = details.closest("[data-program]")?.dataset.program || "";
    window.trackSiteEvent?.("view_plan", { program });
  });
});

if (siteHeader) {
  const updateHeader = () => {
    siteHeader.classList.toggle("is-scrolled", window.scrollY > 18);
  };

  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });
}

const galleryButtons = document.querySelectorAll(".gallery-open");

if (galleryButtons.length) {
  const lightbox = document.createElement("div");
  let lastGalleryTrigger = null;
  lightbox.className = "image-lightbox";
  lightbox.setAttribute("role", "dialog");
  lightbox.setAttribute("aria-modal", "true");
  lightbox.setAttribute("aria-label", "Vista ampliada de fotografía");
  lightbox.innerHTML = '<button type="button" aria-label="Cerrar imagen">×</button><img alt="">';
  document.body.appendChild(lightbox);

  const lightboxImage = lightbox.querySelector("img");
  const closeButton = lightbox.querySelector("button");

  const closeLightbox = () => {
    lightbox.classList.remove("is-open");
    document.body.classList.remove("menu-open");
    lastGalleryTrigger?.focus();
  };

  galleryButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const image = button.querySelector("img");

      if (!image) return;

      lastGalleryTrigger = button;
      lightboxImage.src = image.src;
      lightboxImage.alt = image.alt;
      lightbox.classList.add("is-open");
      document.body.classList.add("menu-open");
      closeButton.focus();
    });
  });

  lightbox.addEventListener("click", (event) => {
    if (event.target === lightbox) {
      closeLightbox();
    }
  });

  closeButton.addEventListener("click", closeLightbox);

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && lightbox.classList.contains("is-open")) {
      closeLightbox();
    } else if (event.key === "Tab" && lightbox.classList.contains("is-open")) {
      event.preventDefault();
      closeButton.focus();
    }
  });
}
