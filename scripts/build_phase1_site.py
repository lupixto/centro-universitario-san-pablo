from pathlib import Path
from datetime import date
from html import escape

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://lupixito.github.io/centro-universitario-san-pablo"
TODAY = date.today().isoformat()

PROGRAMS = [
    {
        "slug": "derecho",
        "name": "Derecho",
        "level": "Licenciatura",
        "area": "Ciencias sociales",
        "icon": "scales",
        "description": "Prepárate para comprender, defender y aplicar la ley con visión profesional.",
        "duration": "3 años",
        "cost": "Desde $1,300 al mes",
        "promo": "Primer cuatrimestre por $699 e inscripción gratis para nuevo ingreso.",
        "url": "oferta-academica/derecho.html",
    },
    {
        "slug": "pedagogia",
        "name": "Pedagogía",
        "level": "Licenciatura",
        "area": "Educación",
        "icon": "book",
        "description": "Forma parte del desarrollo educativo con herramientas para enseñar, orientar y transformar.",
        "duration": "3 años",
        "cost": "Desde $1,300 al mes",
        "promo": "Primer cuatrimestre por $699 e inscripción gratis para nuevo ingreso.",
        "url": "oferta-academica/pedagogia.html",
    },
    {
        "slug": "administracion",
        "name": "Administración",
        "level": "Licenciatura",
        "area": "Negocios",
        "icon": "briefcase",
        "description": "Desarrolla habilidades para dirigir equipos, organizar recursos y tomar mejores decisiones.",
        "duration": "3 años",
        "cost": "Desde $1,300 al mes",
        "promo": "Primer cuatrimestre por $699 e inscripción gratis para nuevo ingreso.",
        "url": "oferta-academica/administracion.html",
    },
    {
        "slug": "contabilidad",
        "name": "Contabilidad",
        "level": "Licenciatura",
        "area": "Negocios",
        "icon": "calculator",
        "description": "Aprende a interpretar, organizar y cuidar la información financiera de una organización.",
        "duration": "3 años",
        "cost": "Desde $1,300 al mes",
        "promo": "Primer cuatrimestre por $699 e inscripción gratis para nuevo ingreso.",
        "url": "oferta-academica/contabilidad.html",
    },
    {
        "slug": "ingenieria-industrial",
        "name": "Ingeniería Industrial",
        "level": "Licenciatura",
        "area": "Ingeniería",
        "icon": "gear",
        "description": "Prepárate para mejorar procesos, productividad y operación dentro de empresas e industrias.",
        "duration": "3 años",
        "cost": "Desde $1,300 al mes",
        "promo": "Primer cuatrimestre por $699 e inscripción gratis para nuevo ingreso.",
        "url": "oferta-academica/ingenieria-industrial.html",
    },
    {
        "slug": "comercio-internacional",
        "name": "Comercio Internacional y Aduanal",
        "level": "Licenciatura",
        "area": "Negocios internacionales",
        "icon": "globe",
        "description": "Conoce el mundo del comercio exterior, logística, importación y exportación.",
        "duration": "3 años",
        "cost": "Desde $1,300 al mes",
        "promo": "Primer cuatrimestre por $699 e inscripción gratis para nuevo ingreso.",
        "url": "oferta-academica/comercio-internacional.html",
    },
    {
        "slug": "doctorado-educacion",
        "name": "Doctorado en Educación",
        "level": "Doctorado",
        "area": "Educación",
        "icon": "graduate",
        "description": "Fortalece tu perfil académico con una visión avanzada sobre educación e investigación.",
        "duration": "3 años",
        "cost": "$1,800 al mes",
        "promo": "La promoción de licenciaturas no aplica al Doctorado en Educación.",
        "url": "oferta-academica/doctorado-educacion.html",
    },
]

PLANTELES = {
    "hidalgo": {
        "name": "Plantel Hidalgo",
        "address": "Calle Hidalgo 412, Obregón, 37320 León de los Aldama, Gto.",
        "phone": "477 713 4804",
        "tel": "4777134804",
        "wa": "524777134804",
        "map": "https://www.google.com/maps/search/?api=1&query=Calle%20Hidalgo%20412%2C%20Obregon%2C%2037320%20Leon%20de%20los%20Aldama%2C%20Gto.",
    },
    "centro": {
        "name": "Plantel Centro",
        "address": "Emiliano Zapata #202A, Segundo Piso, Zona Centro, 37000 León de los Aldama, Gto.",
        "phone": "477 265 9137",
        "tel": "4772659137",
        "wa": "524772659137",
        "map": "https://maps.app.goo.gl/R2KZGukq2DcuyGDQ8",
    },
}

SOCIALS = {
    "facebook": "https://www.facebook.com/share/18etCjsebR/?mibextid=wwXIfr",
    "instagram": "https://www.instagram.com/centro_universitario_san_pablo?igsh=MXRteDE3eHA0YjRnaQ==",
}

PENDING = "PENDIENTE DE CONFIRMACIÓN"
HOURS = "Lunes a viernes: 8:00 a.m. a 3:00 p.m. · Sábado: 7:00 a.m. a 3:00 p.m. · Domingo: cerrado"


def prefix_for(path: str) -> str:
    depth = len(Path(path).parts) - 1
    return "../" * depth


def href(prefix: str, target: str) -> str:
    if target.endswith("/"):
        return f"{prefix}{target}index.html"
    return f"{prefix}{target}"


def svg_sprite() -> str:
    return """
  <svg class="icon-sprite" aria-hidden="true">
    <defs>
      <symbol id="icon-scales" viewBox="0 0 24 24"><path d="M12 3v18M7 21h10M5 6h14M5 6l-3 6h6L5 6Zm14 0-3 6h6l-3-6ZM2 12c0 2 1.3 3 3 3s3-1 3-3M16 12c0 2 1.3 3 3 3s3-1 3-3"/></symbol>
      <symbol id="icon-book" viewBox="0 0 24 24"><path d="M4 5.5A3.5 3.5 0 0 1 7.5 2H12v18H7.5A3.5 3.5 0 0 0 4 23V5.5ZM20 5.5A3.5 3.5 0 0 0 16.5 2H12v18h4.5A3.5 3.5 0 0 1 20 23V5.5Z"/></symbol>
      <symbol id="icon-briefcase" viewBox="0 0 24 24"><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 7h18v13H3V7Zm0 5c5 3 13 3 18 0M10 13h4"/></symbol>
      <symbol id="icon-calculator" viewBox="0 0 24 24"><path d="M5 2h14v20H5V2Zm3 3h8v4H8V5Zm0 8h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01M16 17h.01"/></symbol>
      <symbol id="icon-gear" viewBox="0 0 24 24"><path d="M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8Zm0-5 1 2.3 2.5.7 2-1.5 2 2-1.5 2 .7 2.5L21 12l-2.3 1-.7 2.5 1.5 2-2 2-2-1.5-2.5.7L12 21l-1-2.3-2.5-.7-2 1.5-2-2 1.5-2-.7-2.5L3 12l2.3-1L6 8.5l-1.5-2 2-2 2 1.5 2.5-.7L12 3Z"/></symbol>
      <symbol id="icon-globe" viewBox="0 0 24 24"><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18M4.9 7h14.2M4.9 17h14.2M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/></symbol>
      <symbol id="icon-graduate" viewBox="0 0 24 24"><path d="m2 9 10-5 10 5-10 5L2 9Zm4 2.2V16c3 3 9 3 12 0v-4.8M22 9v6"/></symbol>
      <symbol id="icon-location" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Zm-8-3a3 3 0 1 0 0 6 3 3 0 0 0 0-6Z"/></symbol>
      <symbol id="icon-wallet" viewBox="0 0 24 24"><path d="M3 6h16a2 2 0 0 1 2 2v11H3V6Zm0 0V4h14v2M16 12h5v4h-5a2 2 0 0 1 0-4Z"/></symbol>
      <symbol id="icon-user" viewBox="0 0 24 24"><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm-7 9a7 7 0 0 1 14 0M18 8l2 2 3-4"/></symbol>
      <symbol id="icon-calendar" viewBox="0 0 24 24"><path d="M4 5h16v16H4V5Zm0 5h16M8 2v6M16 2v6M8 14h3M13 14h3M8 18h3"/></symbol>
      <symbol id="icon-shield" viewBox="0 0 24 24"><path d="M12 2 20 5v6c0 5-3.2 9-8 11-4.8-2-8-6-8-11V5l8-3Zm-4 10 2.5 2.5L16 9"/></symbol>
      <symbol id="icon-message" viewBox="0 0 24 24"><path d="M4 4h16v13H9l-5 4V4Zm4 5h8M8 13h5"/></symbol>
      <symbol id="icon-search" viewBox="0 0 24 24"><path d="m21 21-5.2-5.2M18 10.5a7.5 7.5 0 1 1-15 0 7.5 7.5 0 0 1 15 0Z"/></symbol>
    </defs>
  </svg>"""


def icon(name: str) -> str:
    return f'<svg class="ui-icon" aria-hidden="true"><use href="#icon-{name}"></use></svg>'


def head(title: str, description: str, page: str, prefix: str) -> str:
    canonical = f"{SITE}/{'' if page == 'index.html' else page}"
    if not canonical.endswith("/") and page.endswith("index.html"):
        canonical = canonical.removesuffix("index.html")
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{escape(description)}">
  <meta name="theme-color" content="#050506">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/png" sizes="64x64" href="{prefix}assets/favicon.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{prefix}assets/apple-touch-icon.png">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Centro Universitario San Pablo">
  <meta property="og:locale" content="es_MX">
  <meta property="og:image" content="{SITE}/assets/equipo-san-pablo.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <title>{escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&amp;family=Sora:wght@500;600;700;800&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}styles.css">
</head>"""


def header(prefix: str) -> str:
    return f"""
<body>
  <a class="skip-link" href="#contenido">Saltar al contenido principal</a>
{svg_sprite()}
  <header class="site-header" data-site-header>
    <div class="topbar">
      <div class="container topbar-inner">
        <a href="tel:{PLANTELES['hidalgo']['tel']}">Hidalgo: {PLANTELES['hidalgo']['phone']}</a>
        <a href="tel:{PLANTELES['centro']['tel']}">Centro: {PLANTELES['centro']['phone']}</a>
        <a href="https://wa.me/{PLANTELES['centro']['wa']}?text=Hola%2C%20quiero%20informes%20del%20Centro%20Universitario%20San%20Pablo." target="_blank" rel="noopener">WhatsApp</a>
        <a href="{href(prefix, 'planteles/')}">Planteles</a>
        <span>{HOURS}</span>
        <span class="soon-link">Acceso estudiantes: Próximamente</span>
      </div>
    </div>
    <nav class="nav container" aria-label="Navegación principal">
      <a class="brand" href="{href(prefix, 'index.html')}" aria-label="Centro Universitario San Pablo, ir al inicio">
        <span class="brand-mark"><img src="{prefix}assets/logo-san-pablo-320.webp" width="320" height="320" alt="" aria-hidden="true"></span>
        <span><strong>Centro Universitario San Pablo</strong><small>SPIRITVS GLADIVS</small></span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-menu" aria-label="Abrir menú">
        <span></span><span></span><span></span>
      </button>
      <div class="nav-backdrop" data-menu-close></div>
      <ul class="nav-menu" id="nav-menu">
        <li><a href="{href(prefix, 'index.html')}">Inicio</a></li>
        <li class="has-dropdown"><a href="{href(prefix, 'oferta-academica/')}">Oferta académica</a><button type="button" aria-expanded="false" aria-label="Abrir submenu de oferta académica"></button><ul>
          <li><a href="{href(prefix, 'oferta-academica/')}">Todas las carreras</a></li><li><a href="{href(prefix, 'oferta-academica/#licenciaturas')}">Licenciaturas</a></li><li><a href="{href(prefix, 'oferta-academica/doctorado-educacion.html')}">Doctorado</a></li>
        </ul></li>
        <li class="has-dropdown"><a href="{href(prefix, 'admisiones/')}">Admisiones</a><button type="button" aria-expanded="false" aria-label="Abrir submenu de admisiones"></button><ul>
          <li><a href="{href(prefix, 'admisiones/')}">Proceso de inscripción</a></li><li><a href="{href(prefix, 'admisiones/requisitos.html')}">Requisitos</a></li><li><a href="{href(prefix, 'admisiones/costos-promociones.html')}">Costos y promociones</a></li><li><a href="{href(prefix, 'admisiones/fechas-inicio.html')}">Fechas de inicio</a></li><li><a href="{href(prefix, 'admisiones/preguntas-frecuentes.html')}">Preguntas frecuentes</a></li>
        </ul></li>
        <li class="has-dropdown"><a href="{href(prefix, 'universidad/quienes-somos.html')}">Universidad</a><button type="button" aria-expanded="false" aria-label="Abrir submenu de universidad"></button><ul>
          <li><a href="{href(prefix, 'universidad/quienes-somos.html')}">Quiénes somos</a></li><li><a href="{href(prefix, 'universidad/historia.html')}">Historia</a></li><li><a href="{href(prefix, 'universidad/identidad-institucional.html')}">Misión, visión y valores</a></li><li><a href="{href(prefix, 'universidad/modelo-educativo.html')}">Modelo educativo</a></li><li><a href="{href(prefix, 'universidad/rvoe.html')}">RVOE</a></li><li><a href="{href(prefix, 'universidad/directorio.html')}">Directorio</a></li>
        </ul></li>
        <li class="has-dropdown"><a href="{href(prefix, 'vida-universitaria/')}">Vida universitaria</a><button type="button" aria-expanded="false" aria-label="Abrir submenu de vida universitaria"></button><ul>
          <li><a href="{href(prefix, 'vida-universitaria/noticias.html')}">Noticias</a></li><li><a href="{href(prefix, 'vida-universitaria/eventos.html')}">Eventos</a></li><li><a href="{href(prefix, 'vida-universitaria/galeria.html')}">Galería</a></li><li><a href="{href(prefix, 'vida-universitaria/egresados.html')}">Egresados</a></li>
        </ul></li>
        <li><a href="{href(prefix, 'planteles/')}">Planteles</a></li>
        <li><a href="{href(prefix, 'contacto/')}">Contacto</a></li>
        <li><a class="nav-cta" href="{href(prefix, 'contacto/')}">Solicitar informes</a></li>
      </ul>
    </nav>
  </header>
"""


def footer(prefix: str) -> str:
    wa_msg = "Hola%2C%20quiero%20informes%20del%20Centro%20Universitario%20San%20Pablo."
    return f"""
  <a class="floating-whatsapp" href="https://wa.me/{PLANTELES['centro']['wa']}?text={wa_msg}" target="_blank" rel="noopener" aria-label="Pedir informes por WhatsApp">WhatsApp</a>
  <div class="mobile-bottom-bar" aria-label="Acciones rápidas"><a href="{href(prefix, 'contacto/')}">Pedir informes</a><a href="tel:{PLANTELES['centro']['tel']}">Llamar</a></div>
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand"><span class="footer-mark"><img src="{prefix}assets/logo-san-pablo-320.webp" width="320" height="320" alt="Logo del Centro Universitario San Pablo" loading="lazy" decoding="async"></span><strong>Centro Universitario San Pablo</strong><p>SPIRITVS GLADIVS</p></div>
      <div><h2>Planteles</h2><p><strong>Hidalgo</strong><br>{PLANTELES['hidalgo']['address']}<br><a href="tel:{PLANTELES['hidalgo']['tel']}">{PLANTELES['hidalgo']['phone']}</a></p><p><strong>Centro</strong><br>{PLANTELES['centro']['address']}<br><a href="tel:{PLANTELES['centro']['tel']}">{PLANTELES['centro']['phone']}</a></p></div>
      <div><h2>Oferta académica</h2><p>Derecho, Pedagogía, Administración, Contabilidad, Ingeniería Industrial, Comercio Internacional y Aduanal.</p><p>Doctorado en Educación.</p><h2>Horarios</h2><p>{HOURS}</p></div>
      <div><h2>Enlaces</h2><p><a href="{href(prefix, 'oferta-academica/')}">Oferta académica</a><br><a href="{href(prefix, 'admisiones/')}">Admisiones</a><br><a href="{href(prefix, 'planteles/')}">Planteles</a><br><a href="{href(prefix, 'legales/aviso-privacidad.html')}">Aviso de privacidad</a><br><a href="{href(prefix, 'legales/terminos.html')}">Términos</a></p><h2>Redes sociales</h2><p class="footer-social"><a href="{SOCIALS['facebook']}" target="_blank" rel="noopener">Facebook</a><a href="{SOCIALS['instagram']}" target="_blank" rel="noopener">Instagram</a></p></div>
    </div>
    <div class="container footer-legal-row"><p>La información de promociones, costos, modalidades y disponibilidad puede estar sujeta a cambios. Consulta detalles directamente con un asesor.</p><p>© <span data-current-year>{TODAY[:4]}</span> Centro Universitario San Pablo.</p></div>
  </footer>
  <script src="{prefix}analytics.js"></script>
  <script src="{prefix}script.js"></script>
</body>
</html>
"""


def page(path: str, title: str, description: str, content: str) -> None:
    prefix = prefix_for(path)
    output = head(title, description, path, prefix) + header(prefix) + f'\n  <main id="contenido">\n{content}\n  </main>\n' + footer(prefix)
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(output, encoding="utf-8")


def program_cards(prefix: str = "") -> str:
    cards = []
    for p in PROGRAMS:
        cards.append(f"""
          <article class="program-card" data-program-card data-level="{p['level']}" data-area="{p['area']}" data-campus="pendiente">
            <span class="program-icon">{icon(p['icon'])}</span>
            <p class="program-level">{p['level']}</p>
            <h3>{p['name']}</h3>
            <p>{p['description']}</p>
            <ul class="mini-list"><li>{p['duration']}</li><li>Modalidad presencial</li><li>Opción sabatina</li></ul>
            <div class="card-actions"><a class="button button-outline" href="{href(prefix, p['url'])}">Ver programa</a><a class="button button-primary" href="{href(prefix, 'contacto/')}?programa={p['slug']}">Solicitar informes</a></div>
          </article>""")
    return "\n".join(cards)


def trust_strip() -> str:
    items = ["Programas con RVOE", "Modalidad presencial", "Opción sabatina", "Dos planteles en León", "Atención personalizada"]
    return '<div class="trust-strip container">' + "".join(f"<span>{item}</span>" for item in items) + "</div>"


def home() -> str:
    return f"""
    <section class="hero section" id="inicio">
      <div class="container hero-grid">
        <div class="hero-content">
          <p class="eyebrow">Nuevo ingreso</p>
          <h1>Estudia una licenciatura en 3 años sin dejar de trabajar</h1>
          <p class="hero-strong">Programas presenciales con opción sabatina, atención cercana y dos planteles en León.</p>
          <p class="hero-lead">Nuevo ingreso: inscripción gratis y primer cuatrimestre por $699.</p>
          <p class="hero-note">Promoción sujeta a vigencia, disponibilidad y confirmación directa con el plantel.</p>
          <div class="hero-actions"><a class="button button-primary" href="oferta-academica/index.html">Explorar carreras</a><a class="button button-secondary" href="contacto/index.html">Solicitar información</a></div>
        </div>
        <div class="hero-visual">
          <img src="assets/equipo-san-pablo.webp" srcset="assets/equipo-san-pablo-640.webp 640w, assets/equipo-san-pablo.webp 2048w" sizes="(max-width: 760px) calc(100vw - 28px), 48vw" width="2048" height="1536" alt="Comunidad del Centro Universitario San Pablo" fetchpriority="high" decoding="async">
          <div class="floating-promo-card"><strong>$699</strong><span>Primer cuatrimestre</span><small>Inscripción gratis</small></div>
        </div>
      </div>
    </section>
    {trust_strip()}
    <section class="section program-finder">
      <div class="container">
        <div class="finder-panel">
          <div><p class="eyebrow">Busca tu programa</p><h2>Encuentra una opción para avanzar</h2></div>
          <label class="search-box">{icon('search')}<span class="sr-only">Buscar programa</span><input type="search" data-program-search placeholder="Buscar por carrera o área"></label>
        </div>
      </div>
    </section>
    <section class="section section-muted" id="carreras-destacadas">
      <div class="container">
        <div class="section-heading"><p class="eyebrow">Carreras destacadas</p><h2>Oferta académica confirmada</h2><p>No se publican maestrías hasta contar con nombres y datos confirmados.</p></div>
        <div class="program-grid">{program_cards()}</div>
      </div>
    </section>
    <section class="section" id="diferenciadores">
      <div class="container">
        <div class="section-heading centered-heading"><p class="eyebrow">Razones para elegir San Pablo</p><h2>Una universidad cercana, seria y accesible</h2></div>
        <div class="feature-grid">
          <article>{icon('wallet')}<h3>Colegiaturas accesibles</h3><p>Licenciaturas desde $1,300 al mes.</p></article>
          <article>{icon('calendar')}<h3>Opción sabatina</h3><p>Programas presenciales para personas que trabajan.</p></article>
          <article>{icon('shield')}<h3>Programas con RVOE</h3><p>Las claves oficiales se publicarán al ser confirmadas por la institución.</p></article>
          <article>{icon('location')}<h3>Dos planteles en León</h3><p>Atención directa en Hidalgo y Centro.</p></article>
        </div>
      </div>
    </section>
    <section class="section campaign-section" id="promocion">
      <div class="container campaign-grid"><div><p class="eyebrow">Promoción vigente</p><h2>Inscripción gratis y primer cuatrimestre por $699</h2><p>Promoción aplicable a nuevo ingreso en licenciaturas. No aplica al Doctorado en Educación.</p></div><a class="button button-primary" href="contacto/">Preguntar por la promoción</a></div>
    </section>
    <section class="section admission-section">
      <div class="container">
        <div class="section-heading"><p class="eyebrow">Proceso de admisión</p><h2>Inscribirte es más fácil de lo que parece</h2></div>
        <div class="steps"><article><span>1</span><h3>Solicita información</h3><p>Un asesor te orienta por WhatsApp.</p></article><article><span>2</span><h3>Elige tu carrera</h3><p>Consulta disponibilidad por plantel.</p></article><article><span>3</span><h3>Revisa requisitos</h3><p>{PENDING}</p></article><article><span>4</span><h3>Inicia tu proceso</h3><p>Fechas por confirmar con el plantel.</p></article></div>
      </div>
    </section>
    <section class="section section-muted" id="vida">
      <div class="container">
        <div class="section-heading"><p class="eyebrow">Vida universitaria</p><h2>Comunidad, actividades y logros</h2></div>
        <div class="gallery-collage">
          <figure class="gallery-featured"><img src="assets/comunidad-academica.webp" srcset="assets/comunidad-academica-640.webp 640w, assets/comunidad-academica.webp 1600w" sizes="(max-width: 760px) calc(100vw - 28px), 56vw" width="1600" height="1200" alt="Comunidad académica reunida" loading="lazy" decoding="async"><figcaption>Comunidad académica San Pablo.</figcaption></figure>
          <figure><img src="assets/congreso-estudiantes.webp" width="2048" height="1536" alt="Estudiantes en congreso académico" loading="lazy" decoding="async"><figcaption>Congresos académicos.</figcaption></figure>
          <figure><img src="assets/graduacion-grupo.webp" width="1600" height="1200" alt="Grupo de egresados en graduación" loading="lazy" decoding="async"><figcaption>Graduaciones.</figcaption></figure>
          <figure><img src="assets/plantel-emiliano-zapata.webp" width="960" height="1280" alt="Espacio interior del Plantel Centro" loading="lazy" decoding="async"><figcaption>Plantel Centro.</figcaption></figure>
          <figure><img src="assets/reconocimiento-egresada.webp" width="1142" height="1600" alt="Egresada con reconocimiento" loading="lazy" decoding="async"><figcaption>Reconocimientos.</figcaption></figure>
        </div>
      </div>
    </section>
    <section class="section testimonials-section">
      <div class="container">
        <div class="section-heading"><p class="eyebrow">Testimonios</p><h2>Historias reales por publicar</h2><p>Se integrarán únicamente testimonios autorizados.</p></div>
        <div class="testimonial-grid"><article class="is-pending"><h3>Testimonio 1</h3><p>{PENDING}</p></article><article class="is-pending"><h3>Testimonio 2</h3><p>{PENDING}</p></article><article class="is-pending"><h3>Testimonio 3</h3><p>{PENDING}</p></article></div>
      </div>
    </section>
    {planteles_section('')}
    <section class="section final-cta"><div class="container"><h2>¿Listo para recibir orientación?</h2><p>Elige carrera, plantel y recibe información por WhatsApp.</p><a class="button button-primary" href="contacto/index.html">Solicitar informes</a></div></section>
"""


def planteles_section(prefix: str) -> str:
    cards = []
    for key, campus in PLANTELES.items():
        photo = '<div class="campus-photo-placeholder">Fotografía exterior pendiente</div>'
        if key == "centro":
            photo = f'<img src="{prefix}assets/plantel-emiliano-zapata.webp" width="960" height="1280" alt="Espacio institucional del Plantel Centro" loading="lazy" decoding="async">'
        cards.append(f"""
          <article class="campus-card">
            <div class="campus-media">{photo}</div>
            <div class="campus-body"><h3>{campus['name']}</h3><address>{campus['address']}</address><p><strong>Teléfono:</strong> <a href="tel:{campus['tel']}">{campus['phone']}</a></p><p><strong>Horario:</strong> {HOURS}</p><p class="is-pending"><strong>Carreras disponibles por plantel:</strong> {PENDING}</p><div class="card-actions"><a class="button button-outline" href="tel:{campus['tel']}">Llamar</a><a class="button button-primary" href="https://wa.me/{campus['wa']}?text=Hola%2C%20quiero%20informes%20del%20Centro%20Universitario%20San%20Pablo%20{campus['name'].replace(' ', '%20')}." target="_blank" rel="noopener">WhatsApp</a><a class="button button-outline" href="{campus['map']}" target="_blank" rel="noopener">Cómo llegar</a></div></div>
          </article>""")
    return f"""
    <section class="section campus-section" id="planteles">
      <div class="container"><div class="section-heading"><p class="eyebrow">Planteles</p><h2>Dos puntos de atención en León</h2><p>Elige el plantel que te quede más cerca y solicita información directa.</p></div><div class="campus-grid">{''.join(cards)}</div></div>
    </section>"""


def oferta_index() -> str:
    return f"""
    <section class="page-hero"><div class="container"><p class="eyebrow">Oferta académica</p><h1>Programas para construir tu proyecto profesional</h1><p>Consulta licenciaturas y doctorado confirmados. Las maestrías no se publican hasta contar con información oficial.</p></div></section>
    <section class="section"><div class="container">
      <div class="filters" aria-label="Filtros de programas"><label>Nivel<select data-filter="level"><option value="">Todos</option><option>Licenciatura</option><option>Doctorado</option></select></label><label>Área<select data-filter="area"><option value="">Todas</option><option>Ciencias sociales</option><option>Educación</option><option>Negocios</option><option>Ingeniería</option><option>Negocios internacionales</option></select></label><label>Plantel<select data-filter="campus"><option value="">Todos</option><option value="pendiente">Por confirmar</option></select></label></div>
      <div class="program-grid" id="licenciaturas">{program_cards('../')}</div>
    </div></section>"""


def program_page(p: dict) -> str:
    promo = p["promo"] if p["level"] == "Licenciatura" else "No aplica promoción de licenciaturas."
    return f"""
    <section class="page-hero program-hero"><div class="container"><p class="eyebrow">{p['level']}</p><h1>{p['name']}</h1><p>{p['description']}</p><div class="hero-actions"><a class="button button-primary" href="../contacto/index.html?programa={p['slug']}">Recibir costos y horarios</a><a class="button button-secondary" href="#plan">Ver plan de estudios</a></div></div></section>
    <section class="section"><div class="container program-layout">
      <aside class="program-summary"><h2>Ficha rápida</h2><dl><div><dt>Duración</dt><dd>{p['duration']}</dd></div><div><dt>Modalidad</dt><dd>Presencial</dd></div><div><dt>Opción sabatina</dt><dd>Sí</dd></div><div><dt>Plantel</dt><dd>{PENDING}</dd></div><div><dt>RVOE</dt><dd>Cuenta con RVOE; clave pendiente</dd></div><div><dt>Costos</dt><dd>{p['cost']}</dd></div></dl><a class="button button-primary" href="../contacto/index.html?programa={p['slug']}">Solicitar informes</a></aside>
      <div class="program-content">
        <section><h2>Descripción</h2><p>{p['description']}</p></section>
        <section class="is-pending"><h2>Perfil de ingreso</h2><p>{PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: perfil de ingreso --></section>
        <section class="is-pending"><h2>Perfil de egreso</h2><p>{PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: perfil de egreso --></section>
        <section class="is-pending"><h2>Campo laboral</h2><p>{PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: campo laboral --></section>
        <section id="plan" class="is-pending"><h2>Plan de estudios</h2><p>{PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: plan de estudios --></section>
        <section class="is-pending"><h2>Requisitos</h2><p>{PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: requisitos oficiales --></section>
        <section><h2>Costos y promoción</h2><p>{promo}</p><p>La información puede estar sujeta a vigencia, disponibilidad y confirmación directa con el plantel.</p></section>
        <section class="is-pending"><h2>Fechas de inicio</h2><p>{PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: fechas de inicio --></section>
      </div>
    </div></section>"""


def contact_page(prefix: str = "../") -> str:
    options = "".join(f'<option value="{p["slug"]}">{p["name"]}</option>' for p in PROGRAMS)
    return f"""
    <section class="page-hero"><div class="container"><p class="eyebrow">Contacto</p><h1>Recibe información personalizada</h1><p>Déjanos tus datos y un asesor te compartirá carreras, promociones, plantel disponible y requisitos.</p></div></section>
    <section class="section"><div class="container contact-grid">
      <div class="contact-panel"><h2>También puedes escribir directo</h2><p><strong>Plantel Hidalgo:</strong> <a href="https://wa.me/{PLANTELES['hidalgo']['wa']}" target="_blank" rel="noopener">{PLANTELES['hidalgo']['phone']}</a></p><p><strong>Plantel Centro:</strong> <a href="https://wa.me/{PLANTELES['centro']['wa']}" target="_blank" rel="noopener">{PLANTELES['centro']['phone']}</a></p><p class="social-row"><a href="{SOCIALS['facebook']}" target="_blank" rel="noopener">Facebook</a><a href="{SOCIALS['instagram']}" target="_blank" rel="noopener">Instagram</a></p></div>
      <form class="contact-form" id="contact-form" action="#" method="post" novalidate>
        <div class="form-errors" id="form-errors" role="alert" aria-live="polite" tabindex="-1" hidden></div>
        <label for="name">Nombre completo</label><input id="name" name="name" type="text" autocomplete="name" required aria-describedby="name-error"><span class="field-error" id="name-error" aria-live="polite"></span>
        <label for="phone">WhatsApp</label><input id="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="477 000 0000" required aria-describedby="phone-error phone-hint"><small id="phone-hint">Ingresa 10 dígitos; puedes usar +52.</small><span class="field-error" id="phone-error" aria-live="polite"></span>
        <label for="program">Programa de interés</label><select id="program" name="program" required aria-describedby="program-error"><option value="">Selecciona una opción</option>{options}</select><span class="field-error" id="program-error" aria-live="polite"></span>
        <label for="campus">Plantel de interés</label><select id="campus" name="campus" required aria-describedby="campus-error"><option value="">Selecciona un plantel</option><option value="hidalgo">Plantel Hidalgo</option><option value="centro">Plantel Centro</option></select><span class="field-error" id="campus-error" aria-live="polite"></span>
        <label for="message">Mensaje</label><textarea id="message" name="message" rows="4"></textarea>
        <label class="consent-field" for="privacy-consent"><input id="privacy-consent" name="privacy-consent" type="checkbox" required aria-describedby="privacy-error"><span>He leído el <a href="{prefix}legales/aviso-privacidad.html">aviso de privacidad</a> y autorizo el uso de mis datos para recibir información.</span></label><span class="field-error" id="privacy-error" aria-live="polite"></span>
        <button class="button button-primary" type="submit">Enviar solicitud por WhatsApp</button>
      </form>
    </div></section>"""


def simple_page(title: str, eyebrow: str, body: str) -> str:
    return f"""
    <section class="page-hero"><div class="container"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p>{body}</p></div></section>
    <section class="section"><div class="container content-card"><p>{body}</p><p class="is-pending">{PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: completar información oficial de esta página --></div></section>"""


def admisiones_index() -> str:
    return f"""
    <section class="page-hero"><div class="container"><p class="eyebrow">Admisiones</p><h1>Proceso de inscripción</h1><p>Recibe orientación directa para elegir programa, plantel y requisitos.</p></div></section>
    <section class="section"><div class="container"><div class="steps"><article><span>1</span><h3>Solicita información</h3><p>Comparte carrera y plantel de interés.</p></article><article><span>2</span><h3>Consulta requisitos</h3><p>{PENDING}</p></article><article><span>3</span><h3>Confirma horarios</h3><p>Modalidad presencial con opción sabatina.</p></article><article><span>4</span><h3>Inicia tu proceso</h3><p>Fechas de inicio pendientes.</p></article></div></div></section>"""


def faq_page() -> str:
    faqs = [
        ("¿Las carreras cuentan con RVOE?", "Sí. La institución confirma que las carreras cuentan con RVOE; las claves y documentos están pendientes de publicación."),
        ("¿Cuándo inicia el próximo cuatrimestre?", PENDING),
        ("¿Qué documentos necesito?", PENDING),
        ("¿Puedo estudiar solamente los sábados?", "Los programas son presenciales y cuentan con opción sabatina. El horario específico debe confirmarse con un asesor."),
        ("¿Puedo revalidar materias?", PENDING),
        ("¿Cómo funciona la titulación?", PENDING),
        ("¿En qué plantel se ofrece cada carrera?", PENDING),
        ("¿Qué formas de pago aceptan?", PENDING),
        ("¿La promoción tiene vigencia?", "Sí, está sujeta a vigencia, disponibilidad y confirmación directa con el plantel."),
        ("¿Las colegiaturas pueden cambiar?", "La información de costos y disponibilidad puede estar sujeta a cambios. Consulta condiciones vigentes con un asesor."),
    ]
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    return f'<section class="page-hero"><div class="container"><p class="eyebrow">Admisiones</p><h1>Preguntas frecuentes</h1><p>Respuestas claras con información confirmada y pendientes visibles.</p></div></section><section class="section"><div class="container faq-list">{items}</div></section>'


def write_styles() -> None:
    css = r""":root{--black:#050506;--panel:#101014;--panel-2:#17171d;--ink:#fff8e7;--muted:#c9c2b4;--gold:#d7b56d;--gold-2:#fff0bd;--line:rgba(215,181,109,.24);--green:#1f7a55;--white:#fff;--shadow:0 24px 70px rgba(0,0,0,.42);--radius:22px;--max:1180px;--header:132px}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:calc(var(--header) + 20px)}body{margin:0;font-family:Manrope,Arial,sans-serif;color:var(--ink);background:radial-gradient(circle at 15% 0,rgba(215,181,109,.14),transparent 28%),linear-gradient(180deg,#050506,#101014 46%,#0b0b0d);overflow-x:hidden}body.menu-open{overflow:hidden}img{max-width:100%;display:block}a{color:inherit}.container{width:min(var(--max),calc(100% - 32px));margin-inline:auto}.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}.skip-link{position:absolute;left:16px;top:-80px;background:var(--gold);color:#090909;padding:12px 16px;border-radius:12px;z-index:50}.skip-link:focus{top:16px}.icon-sprite{display:none}.ui-icon{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}.site-header{position:sticky;top:0;z-index:40;background:rgba(5,5,6,.9);backdrop-filter:blur(18px);border-bottom:1px solid var(--line);box-shadow:0 16px 46px rgba(0,0,0,.35)}.topbar{border-bottom:1px solid rgba(255,255,255,.08);font-size:12px;color:var(--muted)}.topbar-inner{min-height:36px;display:flex;gap:18px;align-items:center;white-space:nowrap;overflow:hidden}.topbar a{text-decoration:none;color:var(--gold-2)}.soon-link{margin-left:auto}.nav{min-height:86px;display:flex;align-items:center;gap:22px}.brand{display:flex;align-items:center;gap:12px;text-decoration:none;min-width:260px}.brand-mark,.footer-mark{width:62px;height:62px;border-radius:50%;display:grid;place-items:center;background:#fff;border:1px solid var(--gold);box-shadow:0 12px 32px rgba(0,0,0,.3);overflow:hidden}.brand strong{display:block;font-family:Sora,sans-serif;font-size:15px;line-height:1.15;text-transform:uppercase}.brand small{display:block;color:var(--gold);font-weight:800;letter-spacing:.08em;margin-top:4px}.nav-toggle{display:none;margin-left:auto;width:54px;height:54px;border:1px solid var(--line);border-radius:16px;background:rgba(255,255,255,.04);color:var(--ink)}.nav-toggle span{display:block;width:24px;height:2px;background:currentColor;margin:5px auto}.nav-menu{margin:0 0 0 auto;padding:0;list-style:none;display:flex;align-items:center;gap:4px}.nav-menu a,.has-dropdown>button{min-height:42px;display:flex;align-items:center;border:0;background:transparent;color:var(--ink);text-decoration:none;border-radius:12px;padding:0 12px;font-weight:800;font-size:13px}.nav-menu a:hover,.has-dropdown>button:hover{background:rgba(215,181,109,.12);color:var(--gold-2)}.has-dropdown{position:relative;display:flex;align-items:center}.has-dropdown>button{width:34px;padding:0}.has-dropdown>button:after{content:"";border:5px solid transparent;border-top-color:currentColor;margin:auto}.has-dropdown ul{position:absolute;top:100%;left:0;min-width:250px;margin:0;padding:10px;list-style:none;background:#101014;border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);opacity:0;visibility:hidden;transform:translateY(8px);transition:.2s}.has-dropdown:hover ul,.has-dropdown.is-open ul{opacity:1;visibility:visible;transform:none}.has-dropdown ul a{justify-content:flex-start}.nav-cta,.button{display:inline-flex;align-items:center;justify-content:center;min-height:48px;border-radius:999px;padding:0 22px;border:1px solid transparent;text-decoration:none;font-weight:900;cursor:pointer}.nav-cta,.button-primary{background:linear-gradient(135deg,#ffe6a2,#c59a45);color:#090909!important;box-shadow:0 16px 40px rgba(215,181,109,.22)}.button-secondary,.button-outline{background:rgba(255,255,255,.05);border-color:var(--line);color:var(--gold-2)}.button:hover{transform:translateY(-1px)}.section{padding:84px 0}.section-muted{background:linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,.015))}.hero{padding:92px 0 72px;background:radial-gradient(circle at 82% 18%,rgba(215,181,109,.18),transparent 34%)}.hero-grid{display:grid;grid-template-columns:minmax(0,1.04fr) minmax(320px,.96fr);gap:52px;align-items:center}.eyebrow{margin:0 0 12px;color:var(--gold);font-weight:900;text-transform:uppercase;letter-spacing:.12em;font-size:12px}.hero h1,.page-hero h1,.section-heading h2,.final-cta h2{font-family:Sora,sans-serif;line-height:1.02;letter-spacing:-.02em}.hero h1{font-size:clamp(38px,5.8vw,72px);margin:0}.hero-strong{font-size:clamp(19px,2.5vw,28px);font-weight:800;color:var(--gold-2)}.hero-lead,.hero-note,.section-heading p{color:var(--muted);font-size:18px;line-height:1.7}.hero-actions,.card-actions{display:flex;gap:12px;flex-wrap:wrap}.hero-visual{position:relative}.hero-visual img{border-radius:32px;box-shadow:var(--shadow);aspect-ratio:4/3;object-fit:cover}.floating-promo-card{position:absolute;left:-18px;bottom:-22px;background:linear-gradient(135deg,#fffaf0,#fff0bd);color:#101014;border-radius:24px;padding:24px;box-shadow:var(--shadow);min-width:230px}.floating-promo-card strong{font-family:Sora,sans-serif;font-size:42px}.floating-promo-card span,.floating-promo-card small{display:block;font-weight:900}.trust-strip{margin-top:-26px;position:relative;z-index:2;background:rgba(16,16,20,.9);border:1px solid var(--line);border-radius:20px;padding:18px;display:flex;gap:12px;justify-content:space-between;box-shadow:var(--shadow);flex-wrap:wrap}.trust-strip span{color:var(--gold-2);font-weight:900}.finder-panel,.content-card,.program-card,.campus-card,.contact-panel,.contact-form,.program-summary,.filters,.testimonial-grid article,.feature-grid article,.steps article{background:linear-gradient(180deg,rgba(255,255,255,.065),rgba(255,255,255,.025));border:1px solid rgba(255,255,255,.1);border-radius:var(--radius);box-shadow:0 16px 44px rgba(0,0,0,.25)}.finder-panel{padding:28px;display:flex;align-items:center;justify-content:space-between;gap:22px}.search-box{display:flex;align-items:center;gap:12px;background:#fff;color:#101014;border-radius:999px;padding:0 18px;min-height:54px;min-width:min(440px,100%)}.search-box input{border:0;outline:0;font:inherit;width:100%}.section-heading{max-width:780px;margin-bottom:34px}.centered-heading{text-align:center;margin-inline:auto}.section-heading h2{font-size:clamp(30px,4vw,50px);margin:0 0 12px}.program-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}.program-card{padding:24px;display:flex;flex-direction:column;gap:12px}.program-icon,.feature-grid .ui-icon{width:52px;height:52px;border-radius:16px;display:grid;place-items:center;background:rgba(215,181,109,.12);color:var(--gold)}.program-level{color:var(--gold);font-weight:900;margin:0}.program-card h3,.campus-card h3,.content-card h2,.program-content h2{font-family:Sora,sans-serif;margin:0;font-size:22px}.program-card p,.feature-grid p,.steps p,.campus-card p,.campus-card address,.content-card p,.program-content p,.program-summary dd{color:var(--muted);line-height:1.65}.mini-list{margin:0;padding-left:18px;color:var(--gold-2)}.feature-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}.feature-grid article,.steps article{padding:24px}.campaign-section{background:linear-gradient(135deg,#131006,#251d0b);border-block:1px solid var(--line)}.campaign-grid{display:flex;align-items:center;justify-content:space-between;gap:28px}.campaign-grid h2{font-family:Sora,sans-serif;font-size:clamp(34px,5vw,62px);margin:0}.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;counter-reset:step}.steps span{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:var(--gold);color:#090909;font-weight:900}.gallery-collage{display:grid;grid-template-columns:2fr 1fr 1fr;grid-auto-rows:220px;gap:14px}.gallery-collage figure{margin:0;position:relative;overflow:hidden;border-radius:22px;border:1px solid var(--line);background:#111}.gallery-collage .gallery-featured{grid-row:span 2}.gallery-collage img{width:100%;height:100%;object-fit:cover}.gallery-collage figcaption{position:absolute;left:12px;right:12px;bottom:12px;background:rgba(5,5,6,.72);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:10px;font-weight:900}.testimonial-grid,.campus-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}.testimonial-grid article{padding:22px}.is-pending{border-style:dashed!important;color:var(--muted)}.campus-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.campus-media img,.campus-photo-placeholder{height:260px;width:100%;object-fit:cover;border-radius:22px 22px 0 0}.campus-photo-placeholder{display:grid;place-items:center;background:repeating-linear-gradient(45deg,rgba(215,181,109,.1),rgba(215,181,109,.1) 12px,rgba(255,255,255,.04) 12px,rgba(255,255,255,.04) 24px);color:var(--gold-2);font-weight:900}.campus-body{padding:24px}.final-cta{text-align:center}.page-hero{padding:82px 0;background:radial-gradient(circle at 74% 20%,rgba(215,181,109,.16),transparent 34%),linear-gradient(180deg,#09090b,#101014)}.page-hero h1{font-size:clamp(36px,5vw,64px);margin:0 0 16px}.page-hero p{max-width:780px;color:var(--muted);font-size:18px;line-height:1.7}.filters{padding:18px;margin-bottom:24px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.filters label,.contact-form label{font-weight:900;color:var(--gold-2)}select,input,textarea{width:100%;border:1px solid rgba(255,255,255,.14);background:#fff;color:#101014;border-radius:14px;min-height:48px;padding:0 14px;font:inherit}textarea{padding:14px;min-height:120px}.program-layout{display:grid;grid-template-columns:340px minmax(0,1fr);gap:24px}.program-summary{padding:24px;align-self:start;position:sticky;top:calc(var(--header) + 20px)}.program-summary dl{margin:0 0 20px}.program-summary div{padding:12px 0;border-bottom:1px solid rgba(255,255,255,.1)}.program-summary dt{font-weight:900;color:var(--gold)}.program-summary dd{margin:4px 0 0}.program-content{display:grid;gap:16px}.program-content section,.content-card{padding:24px}.contact-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:22px}.contact-panel,.contact-form{padding:28px}.contact-form{display:grid;gap:10px}.field-error{min-height:20px;color:#ffb6b6;font-size:13px}.form-errors{background:#3c1111;color:#fff;border:1px solid #ff8b8b;border-radius:14px;padding:12px}.consent-field{display:flex!important;align-items:flex-start;gap:10px}.consent-field input{width:auto;min-height:auto;margin-top:5px}.social-row,.footer-social{display:flex;gap:10px;flex-wrap:wrap}.social-row a,.footer-social a{background:rgba(215,181,109,.12);border:1px solid var(--line);padding:10px 14px;border-radius:999px;text-decoration:none}.faq-list{display:grid;gap:12px}.faq-list details{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:16px;padding:18px}.faq-list summary{font-weight:900;cursor:pointer}.site-footer{padding:64px 0 100px;background:#050506;border-top:1px solid var(--line)}.footer-grid{display:grid;grid-template-columns:1.2fr 1.2fr 1fr 1fr;gap:28px}.footer-brand strong,.site-footer h2{font-family:Sora,sans-serif}.footer-legal-row{border-top:1px solid rgba(255,255,255,.1);margin-top:34px;padding-top:18px;display:flex;justify-content:space-between;gap:18px;color:var(--muted)}.floating-whatsapp{position:fixed;right:22px;bottom:22px;z-index:30;background:var(--green);color:#fff;text-decoration:none;border-radius:999px;padding:14px 18px;font-weight:900;box-shadow:var(--shadow)}.mobile-bottom-bar{display:none}*:focus-visible{outline:3px solid var(--gold-2);outline-offset:3px}@media (max-width:1020px){:root{--header:86px}.topbar{display:none}.nav-toggle{display:block}.nav-backdrop{position:fixed;inset:0;background:rgba(0,0,0,.55);opacity:0;visibility:hidden;transition:.2s}.nav-menu.is-open+.noop{display:none}.nav-menu{position:fixed;right:0;top:0;bottom:0;width:min(88vw,380px);display:block;background:#0b0b0d;border-left:1px solid var(--line);padding:96px 18px 24px;transform:translateX(100%);transition:.25s;overflow:auto;box-shadow:var(--shadow)}.nav-menu.is-open{transform:none}.nav:has(.nav-menu.is-open) .nav-backdrop{opacity:1;visibility:visible}.nav-menu li{display:block}.nav-menu a{justify-content:space-between;min-height:50px}.has-dropdown{display:block}.has-dropdown>button{position:absolute;right:0;top:0;height:50px}.has-dropdown ul{position:static;opacity:1;visibility:visible;transform:none;display:none;box-shadow:none;background:rgba(255,255,255,.04);margin:4px 0 12px}.has-dropdown.is-open ul{display:block}.hero-grid,.contact-grid,.program-layout{grid-template-columns:1fr}.program-grid,.feature-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.steps,.footer-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.program-summary{position:static}.gallery-collage{grid-template-columns:1fr 1fr}.campaign-grid{display:block}.soon-link{margin-left:0}}@media (max-width:680px){body{padding-bottom:86px}.container{width:min(100% - 28px,var(--max))}.brand{min-width:0}.brand-mark{width:56px;height:56px}.brand strong{font-size:13px}.hero{padding:46px 0}.hero h1{font-size:38px}.hero-actions .button,.card-actions .button{width:100%}.floating-promo-card{position:relative;left:auto;bottom:auto;margin-top:-14px}.trust-strip{margin-top:0}.finder-panel{display:block}.search-box{margin-top:16px}.program-grid,.feature-grid,.steps,.testimonial-grid,.campus-grid,.filters,.footer-grid{grid-template-columns:1fr}.gallery-collage{display:block}.gallery-collage figure{height:260px;margin-bottom:14px}.footer-legal-row{display:block}.floating-whatsapp{display:none}.mobile-bottom-bar{position:fixed;left:12px;right:12px;bottom:12px;z-index:30;background:rgba(255,250,240,.96);border-radius:22px;padding:10px;display:grid;grid-template-columns:1fr 1fr;gap:10px;box-shadow:var(--shadow)}.mobile-bottom-bar a{display:grid;place-items:center;min-height:52px;border-radius:18px;text-decoration:none;font-weight:900}.mobile-bottom-bar a:first-child{background:var(--green);color:#fff}.mobile-bottom-bar a:last-child{background:#050506;color:#fff}}@media (prefers-reduced-motion:reduce){*,*::before,*::after{scroll-behavior:auto!important;transition:none!important;animation:none!important}}"""
    (ROOT / "styles.css").write_text(css, encoding="utf-8")


def write_script() -> None:
    js = r"""const navToggle=document.querySelector(".nav-toggle");const navMenu=document.querySelector("#nav-menu");const siteHeader=document.querySelector("[data-site-header]");const campusWhatsApp={hidalgo:{name:"Plantel Hidalgo",phone:"524777134804"},centro:{name:"Plantel Centro",phone:"524772659137"}};const programNames={derecho:"Derecho",pedagogia:"Pedagogía",administracion:"Administración",contabilidad:"Contabilidad","ingenieria-industrial":"Ingeniería Industrial","comercio-internacional":"Comercio Internacional y Aduanal","doctorado-educacion":"Doctorado en Educación"};const closeMenu=()=>{navMenu?.classList.remove("is-open");navToggle?.setAttribute("aria-expanded","false");navToggle?.setAttribute("aria-label","Abrir menú");document.body.classList.remove("menu-open");document.querySelectorAll(".has-dropdown.is-open").forEach(item=>{item.classList.remove("is-open");item.querySelector("button")?.setAttribute("aria-expanded","false")})};if(navToggle&&navMenu){navToggle.addEventListener("click",()=>{const isOpen=navMenu.classList.toggle("is-open");navToggle.setAttribute("aria-expanded",String(isOpen));navToggle.setAttribute("aria-label",isOpen?"Cerrar menú":"Abrir menú");document.body.classList.toggle("menu-open",isOpen)});document.querySelector("[data-menu-close]")?.addEventListener("click",closeMenu);navMenu.addEventListener("click",event=>{const target=event.target;if(!(target instanceof Element))return;const dropdownButton=target.closest(".has-dropdown > button");if(dropdownButton){const item=dropdownButton.closest(".has-dropdown");const isOpen=item.classList.toggle("is-open");dropdownButton.setAttribute("aria-expanded",String(isOpen));return}if(target.closest("a"))closeMenu()});document.addEventListener("keydown",event=>{if(event.key==="Escape"&&navMenu.classList.contains("is-open")){closeMenu();navToggle.focus()}});window.addEventListener("resize",()=>{if(window.innerWidth>1020)closeMenu()})}if(siteHeader){const updateHeader=()=>siteHeader.classList.toggle("is-scrolled",window.scrollY>18);updateHeader();window.addEventListener("scroll",updateHeader,{passive:true})}document.querySelectorAll("[data-current-year]").forEach(el=>{el.textContent=String(new Date().getFullYear())});const params=new URLSearchParams(location.search);const programParam=params.get("programa");const programSelect=document.querySelector("#program");if(programParam&&programSelect instanceof HTMLSelectElement&&programNames[programParam]){programSelect.value=programParam}const search=document.querySelector("[data-program-search]");if(search){const cards=document.querySelectorAll("[data-program-card]");search.addEventListener("input",()=>{const value=search.value.trim().toLowerCase();cards.forEach(card=>{card.hidden=value&&!card.textContent.toLowerCase().includes(value)})})}const filters=document.querySelectorAll("[data-filter]");if(filters.length){const cards=document.querySelectorAll("[data-program-card]");const apply=()=>{const values={};filters.forEach(filter=>values[filter.dataset.filter]=filter.value);cards.forEach(card=>{const visible=(!values.level||card.dataset.level===values.level)&&(!values.area||card.dataset.area===values.area)&&(!values.campus||card.dataset.campus===values.campus);card.hidden=!visible})};filters.forEach(filter=>filter.addEventListener("change",apply))}const contactForm=document.querySelector("#contact-form");if(contactForm){const formErrorSummary=contactForm.querySelector("#form-errors");const fields={name:contactForm.querySelector("#name"),phone:contactForm.querySelector("#phone"),program:contactForm.querySelector("#program"),campus:contactForm.querySelector("#campus"),privacy:contactForm.querySelector("#privacy-consent")};const setFieldError=(fieldName,message)=>{const field=fields[fieldName];const error=contactForm.querySelector(`#${fieldName==="privacy"?"privacy":fieldName}-error`);if(field)field.setAttribute("aria-invalid",message?"true":"false");if(error)error.textContent=message};const validateForm=()=>{const errors=[];const name=fields.name?.value.trim()||"";const phone=fields.phone?.value.trim()||"";const phoneDigits=phone.replace(/\D/g,"");const validPhone=/^\d{10}$/.test(phoneDigits)||/^52\d{10}$/.test(phoneDigits);Object.keys(fields).forEach(key=>setFieldError(key,""));if(name.length<3){const message="Escribe tu nombre completo con al menos 3 caracteres.";setFieldError("name",message);errors.push({field:fields.name,message})}if(!validPhone){const message="Ingresa un teléfono mexicano válido de 10 dígitos, con o sin el prefijo +52.";setFieldError("phone",message);errors.push({field:fields.phone,message})}if(!fields.program?.value){const message="Selecciona la carrera o programa que te interesa.";setFieldError("program",message);errors.push({field:fields.program,message})}if(!fields.campus?.value||!campusWhatsApp[fields.campus.value]){const message="Selecciona el plantel al que deseas enviar tu solicitud.";setFieldError("campus",message);errors.push({field:fields.campus,message})}if(!fields.privacy?.checked){const message="Debes aceptar el aviso de privacidad para continuar.";setFieldError("privacy",message);errors.push({field:fields.privacy,message})}if(formErrorSummary){formErrorSummary.hidden=errors.length===0;formErrorSummary.textContent=errors.length?`Revisa ${errors.length} ${errors.length===1?"campo":"campos"} antes de continuar.`:""}return errors};Object.entries(fields).forEach(([fieldName,field])=>{field?.addEventListener(fieldName==="privacy"?"change":"input",()=>{setFieldError(fieldName,"");if(formErrorSummary)formErrorSummary.hidden=true})});contactForm.addEventListener("submit",event=>{event.preventDefault();const errors=validateForm();if(errors.length){formErrorSummary?.focus();errors[0].field?.focus();return}const formData=new FormData(contactForm);const campus=campusWhatsApp[formData.get("campus")];const name=String(formData.get("name")||"").trim();const option=fields.program.selectedOptions[0];const program=option?option.textContent.trim():String(formData.get("program")||"");const whatsappMessage=[`Hola, mi nombre es ${name}.`,`Quiero recibir información sobre ${program} en ${campus.name}.`,"","Me interesa conocer:","• Plan de estudios","• Horarios","• Requisitos","• Promoción vigente","• Fecha de inicio"].join("\n");window.trackSiteEvent?.("generate_lead",{method:"whatsapp_form",program,campus:campus.name});window.open(`https://wa.me/${campus.phone}?text=${encodeURIComponent(whatsappMessage)}`,"_blank","noopener")})}document.addEventListener("click",event=>{const link=event.target instanceof Element?event.target.closest("a"):null;if(!link)return;const href=link.getAttribute("href")||"";if(href.includes("wa.me/"))window.trackSiteEvent?.("click_whatsapp",{destination:href});else if(href.startsWith("tel:"))window.trackSiteEvent?.("click_call",{phone:href.replace("tel:","")});else if(href.includes("maps.app")||href.includes("google.com/maps"))window.trackSiteEvent?.("get_directions",{destination:href})});"""
    (ROOT / "script.js").write_text(js, encoding="utf-8")


def write_readme() -> None:
    text = f"""# Centro Universitario San Pablo

Portal universitario estático compatible con GitHub Pages.

## Fase 1 realizada

- Se creó `backup-fase-1` con los archivos originales antes de modificar.
- Se preparó arquitectura multipágina.
- Se conservan logotipo, fotos, teléfonos, direcciones, WhatsApp, mapas y redes sociales.
- No se publican maestrías porque faltan nombres y datos confirmados.
- Los datos pendientes aparecen como `{PENDING}`.

## Estructura principal

- `index.html`: portada y distribuidor.
- `oferta-academica/`: catálogo y páginas por programa.
- `admisiones/`: proceso, requisitos, costos, fechas y FAQ.
- `universidad/`: información institucional, RVOE y directorio pendiente.
- `vida-universitaria/`: noticias, eventos, galería y egresados.
- `planteles/`: planteles Hidalgo y Centro.
- `contacto/`: formulario con WhatsApp por plantel.
- `legales/`: aviso de privacidad y términos.

## Actualizar datos pendientes

Busca `{PENDING}` en los HTML para completar RVOE, fechas, requisitos, planes de estudio, perfiles, campo laboral, directorio, noticias, eventos y testimonios.

## Publicación

El sitio no requiere compilación. Sube los archivos de la raíz del proyecto a GitHub y usa GitHub Pages desde `/(root)`.
"""
    (ROOT / "README.md").write_text(text, encoding="utf-8")


def write_sitemap() -> None:
    pages = [
        "index.html",
        "oferta-academica/index.html",
        *[p["url"] for p in PROGRAMS],
        "admisiones/index.html",
        "admisiones/requisitos.html",
        "admisiones/costos-promociones.html",
        "admisiones/fechas-inicio.html",
        "admisiones/preguntas-frecuentes.html",
        "universidad/quienes-somos.html",
        "universidad/historia.html",
        "universidad/identidad-institucional.html",
        "universidad/modelo-educativo.html",
        "universidad/rvoe.html",
        "universidad/directorio.html",
        "vida-universitaria/index.html",
        "vida-universitaria/noticias.html",
        "vida-universitaria/eventos.html",
        "vida-universitaria/galeria.html",
        "vida-universitaria/egresados.html",
        "planteles/index.html",
        "planteles/hidalgo.html",
        "planteles/centro.html",
        "contacto/index.html",
        "legales/aviso-privacidad.html",
        "legales/terminos.html",
    ]
    urls = []
    for p in pages:
        loc = SITE + "/" + ("" if p == "index.html" else p)
        if loc.endswith("index.html"):
            loc = loc[:-10]
        urls.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{'1.0' if p == 'index.html' else '0.7'}</priority></url>")
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")


def main() -> None:
    write_styles()
    write_script()
    write_readme()
    write_sitemap()
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    page("index.html", "Centro Universitario San Pablo | Licenciaturas en León", "Estudia una licenciatura presencial en 3 años con opción sabatina, dos planteles en León y promoción de nuevo ingreso.", home())
    page("oferta-academica/index.html", "Oferta académica | Centro Universitario San Pablo", "Consulta licenciaturas y Doctorado en Educación en Centro Universitario San Pablo.", oferta_index())
    for p in PROGRAMS:
        page(p["url"], f"{p['name']} | Centro Universitario San Pablo", p["description"], program_page(p))
    page("admisiones/index.html", "Admisiones | Centro Universitario San Pablo", "Conoce el proceso de inscripción del Centro Universitario San Pablo.", admisiones_index())
    page("admisiones/requisitos.html", "Requisitos de inscripción | Centro Universitario San Pablo", "Documentos y requisitos de inscripción pendientes de confirmación.", simple_page("Requisitos de inscripción", "Admisiones", "Esta página está preparada para publicar documentos solicitados, proceso de inscripción y horarios disponibles."))
    page("admisiones/costos-promociones.html", "Costos y promociones | Centro Universitario San Pablo", "Consulta costos confirmados y promoción de nuevo ingreso.", simple_page("Costos y promociones", "Admisiones", "Licenciaturas desde $1,300 al mes. Nuevo ingreso en licenciaturas: inscripción gratis y primer cuatrimestre por $699. Doctorado en Educación: $1,800 al mes y no aplica promoción de licenciaturas."))
    page("admisiones/fechas-inicio.html", "Fechas de inicio | Centro Universitario San Pablo", "Fechas de inicio pendientes de confirmación.", simple_page("Fechas de inicio", "Admisiones", "Las fechas de inicio se confirmarán directamente con el plantel."))
    page("admisiones/preguntas-frecuentes.html", "Preguntas frecuentes | Centro Universitario San Pablo", "Preguntas frecuentes sobre RVOE, horarios, requisitos, pagos y promoción.", faq_page())
    page("universidad/quienes-somos.html", "Quiénes somos | Centro Universitario San Pablo", "Información institucional del Centro Universitario San Pablo.", simple_page("Quiénes somos", "Universidad", "Centro Universitario San Pablo es una institución educativa en León, Guanajuato."))
    page("universidad/historia.html", "Historia | Centro Universitario San Pablo", "Historia institucional pendiente de confirmación.", simple_page("Historia", "Universidad", "La historia institucional se incorporará cuando sea autorizada."))
    page("universidad/identidad-institucional.html", "Misión, visión y valores | Centro Universitario San Pablo", "Identidad institucional pendiente de confirmación.", simple_page("Misión, visión y valores", "Universidad", "El lema institucional confirmado es SPIRITVS GLADIVS."))
    page("universidad/modelo-educativo.html", "Modelo educativo | Centro Universitario San Pablo", "Modelo educativo pendiente de confirmación.", simple_page("Modelo educativo", "Universidad", "Los programas confirmados son presenciales, cuatrimestrales y cuentan con opción sabatina."))
    rvoe_body = "La institución confirma que las carreras cuentan con RVOE. Las claves, autoridad, fechas de acuerdo, modalidad autorizada, plantel y documentos comprobatorios están pendientes de publicación."
    page("universidad/rvoe.html", "RVOE | Centro Universitario San Pablo", "Registro de RVOE preparado para publicar claves oficiales verificables.", simple_page("RVOE", "Universidad", rvoe_body))
    page("universidad/directorio.html", "Directorio | Centro Universitario San Pablo", "Directorio institucional pendiente de confirmación.", simple_page("Directorio", "Universidad", "El directorio se publicará únicamente con datos autorizados."))
    page("vida-universitaria/index.html", "Vida universitaria | Centro Universitario San Pablo", "Actividades, comunidad y galería del Centro Universitario San Pablo.", simple_page("Vida universitaria", "Comunidad", "Actividades, comunidad, reconocimientos y momentos que forman parte de la experiencia San Pablo."))
    page("vida-universitaria/noticias.html", "Noticias | Centro Universitario San Pablo", "Noticias institucionales pendientes de publicación.", simple_page("Noticias", "Vida universitaria", "Espacio preparado para noticias institucionales autorizadas."))
    page("vida-universitaria/eventos.html", "Eventos | Centro Universitario San Pablo", "Eventos institucionales pendientes de publicación.", simple_page("Eventos", "Vida universitaria", "Espacio preparado para eventos institucionales autorizados."))
    page("vida-universitaria/galeria.html", "Galería | Centro Universitario San Pablo", "Galería de actividades del Centro Universitario San Pablo.", home().split('<section class="section section-muted" id="vida">', 1)[1].split('<section class="section testimonials-section">', 1)[0].join if False else simple_page("Galería", "Vida universitaria", "Galería preparada con fotografías institucionales disponibles."))
    page("vida-universitaria/egresados.html", "Egresados | Centro Universitario San Pablo", "Egresados y testimonios pendientes de confirmación.", simple_page("Egresados", "Vida universitaria", "Se publicarán únicamente historias y testimonios reales con autorización."))
    page("planteles/index.html", "Planteles | Centro Universitario San Pablo", "Conoce Plantel Hidalgo y Plantel Centro en León, Guanajuato.", planteles_section("../"))
    page("planteles/hidalgo.html", "Plantel Hidalgo | Centro Universitario San Pablo", "Dirección y contacto del Plantel Hidalgo.", simple_page("Plantel Hidalgo", "Planteles", f"{PLANTELES['hidalgo']['address']} Teléfono: {PLANTELES['hidalgo']['phone']}. {HOURS}"))
    page("planteles/centro.html", "Plantel Centro | Centro Universitario San Pablo", "Dirección y contacto del Plantel Centro.", simple_page("Plantel Centro", "Planteles", f"{PLANTELES['centro']['address']} Teléfono: {PLANTELES['centro']['phone']}. {HOURS}"))
    page("contacto/index.html", "Contacto | Centro Universitario San Pablo", "Solicita información por WhatsApp sobre carreras, planteles, horarios y promoción.", contact_page("../"))
    page("legales/aviso-privacidad.html", "Aviso de privacidad | Centro Universitario San Pablo", "Aviso de privacidad provisional pendiente de documento autorizado.", simple_page("Aviso de privacidad", "Legales", "Documento legal pendiente de autorización institucional."))
    page("legales/terminos.html", "Términos y condiciones | Centro Universitario San Pablo", "Términos y condiciones pendientes de confirmación.", simple_page("Términos y condiciones", "Legales", "Las condiciones completas de promociones, pagos y servicios deberán incorporarse cuando sean autorizadas."))


if __name__ == "__main__":
    main()
