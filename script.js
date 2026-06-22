const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector("#nav-menu");
const contactForm = document.querySelector("#contact-form");
const siteHeader = document.querySelector(".site-header");

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
  navToggle.addEventListener("click", () => {
    const isOpen = navMenu.classList.toggle("is-open");

    navToggle.setAttribute("aria-expanded", String(isOpen));
    document.body.classList.toggle("menu-open", isOpen);
  });

  navMenu.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      navMenu.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
      document.body.classList.remove("menu-open");
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
      `Carrera de interés: ${program}`,
      `Mensaje: ${message}`,
    ].join("\n");

    const whatsappUrl = `https://wa.me/${campus.phone}?text=${encodeURIComponent(whatsappMessage)}`;
    window.open(whatsappUrl, "_blank", "noopener");
  });
}

if (siteHeader) {
  const updateHeader = () => {
    siteHeader.classList.toggle("is-scrolled", window.scrollY > 18);
  };

  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });
}

const revealTargets = document.querySelectorAll(
  ".section-heading, .quick-card, .card, .program-card, .admission-step, .reason-card, .gallery-item, .campus-card, .schedule-card, .contact-form, .emotional-media, .emotional-content"
);

if ("IntersectionObserver" in window) {
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

const galleryImages = document.querySelectorAll(".gallery-item img");

if (galleryImages.length) {
  const lightbox = document.createElement("div");
  lightbox.className = "image-lightbox";
  lightbox.innerHTML = '<button type="button" aria-label="Cerrar imagen">X</button><img alt="">';
  document.body.appendChild(lightbox);

  const lightboxImage = lightbox.querySelector("img");
  const closeButton = lightbox.querySelector("button");

  const closeLightbox = () => {
    lightbox.classList.remove("is-open");
    document.body.classList.remove("menu-open");
  };

  galleryImages.forEach((image) => {
    image.addEventListener("click", () => {
      lightboxImage.src = image.src;
      lightboxImage.alt = image.alt;
      lightbox.classList.add("is-open");
      document.body.classList.add("menu-open");
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
