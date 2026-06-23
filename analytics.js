(function () {
  "use strict";

  const GA4_MEASUREMENT_ID = "";
  // PENDIENTE DE CONFIRMACIÓN: colocar aquí el identificador real, por ejemplo G-XXXXXXXXXX.

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () {
    window.dataLayer.push(arguments);
  };

  window.trackSiteEvent = function (eventName, parameters) {
    if (!GA4_MEASUREMENT_ID) return;
    window.gtag("event", eventName, parameters || {});
  };

  if (!GA4_MEASUREMENT_ID) return;

  const script = document.createElement("script");
  script.async = true;
  script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(GA4_MEASUREMENT_ID)}`;
  document.head.appendChild(script);

  window.gtag("js", new Date());
  window.gtag("config", GA4_MEASUREMENT_ID, { anonymize_ip: true });
})();
