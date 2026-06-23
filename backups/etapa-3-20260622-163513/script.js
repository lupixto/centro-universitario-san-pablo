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
  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(contactForm);
    const selectedCampus = formData.get("campus");
    const campus = campusWhatsApp[selectedCampus];

    if (!campus) {
      document.querySelector("#campus")?.focus();
      return;
    }

    const name = formData.get("name") || "";
    const phone = formData.get("phone") || "";
    const program = formData.get("program") || "";
    const message = formData.get("message") || "Quiero recibir más información.";

    const whatsappMessage = [
      "Hola, quiero informes del Centro Universitario San Pablo.",
      `Plantel: ${campus.name}`,
      `Nombre: ${name}`,
      `Teléfono: ${phone}`,
      `Programa de interés: ${program}`,
      `Mensaje: ${message}`,
    ].join("\n");

    const whatsappUrl = `https://wa.me/${campus.phone}?text=${encodeURIComponent(whatsappMessage)}`;
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

if (siteHeader) {
  const updateHeader = () => {
    siteHeader.classList.toggle("is-scrolled", window.scrollY > 18);
  };

  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });
}

const revealTargets = document.querySelectorAll(
  ".section-heading, .tuition-summary article, .program-card, .reason-card, .purpose-band, .campaign-card, .admission-step, .responsible-info article, .rvoe-register, .requirements-panel, .gallery-item, .testimonials-heading, .campus-card, .schedule-inline, .faq-list details, .contact-form, .privacy-card"
);

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if ("IntersectionObserver" in window && !reduceMotion) {
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.14 }
  );

  revealTargets.forEach((element) => {
    element.classList.add("reveal");
    revealObserver.observe(element);
  });
} else {
  revealTargets.forEach((element) => element.classList.add("is-visible"));
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
    if (event.key === "Escape") {
      closeLightbox();
    }
  });
}
