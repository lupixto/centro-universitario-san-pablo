(function () {
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
