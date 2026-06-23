import os
from pathlib import Path

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

import build_phase1_site as base

ROOT = Path(__file__).resolve().parents[1]
PENDING = base.PENDING


def pending_block(title, note=""):
    comment = f"<!-- PENDIENTE DE CONFIRMACIÓN: {note or title} -->"
    return f'<section class="content-card is-pending"><h2>{title}</h2><p>{PENDING}</p>{comment}</section>'


def form_section(prefix, title="Solicita información de este programa"):
    return f"""
    <section class="section">
      <div class="container contact-grid">
        <div class="contact-panel">
          <p class="eyebrow">Asesoría personalizada</p>
          <h2>{title}</h2>
          <p>El mensaje se enviará al WhatsApp del plantel seleccionado.</p>
          <p><strong>Plantel Hidalgo:</strong> <a href="tel:{base.PLANTELES['hidalgo']['tel']}">{base.PLANTELES['hidalgo']['phone']}</a></p>
          <p><strong>Plantel Centro:</strong> <a href="tel:{base.PLANTELES['centro']['tel']}">{base.PLANTELES['centro']['phone']}</a></p>
        </div>
        {contact_form(prefix)}
      </div>
    </section>"""


def contact_form(prefix):
    options = "".join(f'<option value="{p["slug"]}">{p["name"]}</option>' for p in base.PROGRAMS)
    return f"""
      <form class="contact-form" id="contact-form" action="#" method="post" novalidate>
        <div class="form-errors" id="form-errors" role="alert" aria-live="polite" tabindex="-1" hidden></div>
        <label for="name">Nombre completo</label>
        <input id="name" name="name" type="text" autocomplete="name" required aria-describedby="name-error">
        <span class="field-error" id="name-error" aria-live="polite"></span>
        <label for="phone">WhatsApp</label>
        <input id="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="477 000 0000" required aria-describedby="phone-error phone-hint">
        <small id="phone-hint">Ingresa 10 dígitos; puedes usar +52.</small>
        <span class="field-error" id="phone-error" aria-live="polite"></span>
        <label for="program">Programa de interés</label>
        <select id="program" name="program" required aria-describedby="program-error"><option value="">Selecciona una opción</option>{options}</select>
        <span class="field-error" id="program-error" aria-live="polite"></span>
        <label for="campus">Plantel de interés</label>
        <select id="campus" name="campus" required aria-describedby="campus-error"><option value="">Selecciona un plantel</option><option value="hidalgo">Plantel Hidalgo</option><option value="centro">Plantel Centro</option></select>
        <span class="field-error" id="campus-error" aria-live="polite"></span>
        <label for="message">Mensaje</label>
        <textarea id="message" name="message" rows="4" placeholder="Cuéntanos qué información necesitas"></textarea>
        <label class="consent-field" for="privacy-consent"><input id="privacy-consent" name="privacy-consent" type="checkbox" required aria-describedby="privacy-error"><span>He leído el <a href="{prefix}legales/aviso-privacidad.html">aviso de privacidad</a> y autorizo el uso de mis datos para recibir información.</span></label>
        <span class="field-error" id="privacy-error" aria-live="polite"></span>
        <button class="button button-primary" type="submit">Enviar solicitud por WhatsApp</button>
      </form>"""


def program_page(p):
    is_degree = p["level"] == "Licenciatura"
    promo = "Inscripción gratis y primer cuatrimestre por $699 para nuevo ingreso en licenciaturas." if is_degree else "La promoción de licenciaturas no aplica al Doctorado en Educación."
    related = [x for x in base.PROGRAMS if x["slug"] != p["slug"] and (x["level"] == p["level"] or x["area"] == p["area"])][:3]
    related_cards = "".join(
        f'<article class="program-card"><p class="program-level">{r["level"]}</p><h3>{r["name"]}</h3><p>{r["description"]}</p><a class="button button-outline" href="{r["url"].split("/")[-1]}">Ver programa</a></article>'
        for r in related
    )
    reasons = {
        "Derecho": ["Comprender el marco legal", "Desarrollar criterio profesional", "Prepararte para asesoría y defensa jurídica"],
        "Pedagogía": ["Acompañar procesos educativos", "Diseñar estrategias de aprendizaje", "Participar en instituciones educativas"],
        "Administración": ["Organizar recursos", "Dirigir equipos", "Tomar decisiones con enfoque profesional"],
        "Contabilidad": ["Interpretar información financiera", "Cuidar registros contables", "Apoyar decisiones administrativas"],
        "Ingeniería Industrial": ["Mejorar procesos", "Optimizar productividad", "Participar en operaciones empresariales"],
        "Comercio Internacional y Aduanal": ["Comprender comercio exterior", "Analizar logística", "Participar en importación y exportación"],
        "Doctorado en Educación": ["Fortalecer el perfil académico", "Profundizar en educación", "Preparar investigación avanzada"],
    }[p["name"]]
    reason_items = "".join(f"<article><h3>{item}</h3><p>{p['description']}</p></article>" for item in reasons)
    content = f"""
    <section class="page-hero program-hero">
      <div class="container">
        <p class="eyebrow">{p['level']}</p>
        <h1>{p['name']}</h1>
        <p>{p['description']}</p>
        <div class="hero-actions">
          <a class="button button-primary" href="#formulario-programa">Recibir costos y horarios</a>
          <a class="button button-secondary" href="#plan">Ver plan de estudios</a>
          <a class="button button-outline" href="../planteles/index.html">Agendar visita</a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container program-layout">
        <aside class="program-summary">
          <h2>Datos rápidos</h2>
          <dl>
            <div><dt>Nombre oficial</dt><dd>{p['name']}</dd></div>
            <div><dt>Duración</dt><dd>{p['duration']}</dd></div>
            <div><dt>Sistema</dt><dd>Cuatrimestral</dd></div>
            <div><dt>Modalidad</dt><dd>Presencial</dd></div>
            <div><dt>Opción sabatina</dt><dd>Sí</dd></div>
            <div><dt>Plantel</dt><dd>{PENDING}</dd></div>
            <div><dt>RVOE</dt><dd>Cuenta con RVOE; clave pendiente</dd></div>
            <div><dt>Costos</dt><dd>{p['cost']}</dd></div>
          </dl>
          <a class="button button-primary" href="#formulario-programa">Consultar disponibilidad</a>
        </aside>
        <div class="program-content">
          <section class="content-card"><h2>Descripción</h2><p>{p['description']}</p></section>
          <section class="content-card"><h2>Razones para estudiar {p['name']}</h2><div class="feature-grid compact-grid">{reason_items}</div></section>
          {pending_block("Perfil de ingreso", "perfil de ingreso")}
          {pending_block("Perfil de egreso", "perfil de egreso")}
          {pending_block("Campo laboral", "campo laboral")}
          <section class="content-card is-pending" id="plan"><h2>Plan de estudios por cuatrimestre</h2><p>{PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: plan de estudios oficial por cuatrimestre --></section>
          <section class="content-card is-pending"><h2>Horarios</h2><p>Opción sabatina confirmada. Horarios específicos por programa y plantel: {PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: horarios por carrera --></section>
          <section class="content-card is-pending"><h2>Planteles disponibles</h2><p>{PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: plantel disponible para este programa --></section>
          <section class="content-card is-pending"><h2>RVOE</h2><p>El programa cuenta con RVOE. Clave, autoridad, fecha de acuerdo, modalidad autorizada, plantel y documento oficial: {PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: datos documentales de RVOE --></section>
          <section class="content-card"><h2>Costos y promoción</h2><p><strong>{p['cost']}.</strong></p><p>{promo}</p><p>La información puede estar sujeta a cambios y confirmación directa con el plantel.</p></section>
          {pending_block("Requisitos", "requisitos de inscripción")}
          {pending_block("Fecha de inicio", "fecha de inicio")}
          {pending_block("Formas de titulación", "formas de titulación")}
          {pending_block("Revalidación de materias", "revalidación de materias")}
          <section class="content-card faq-list"><h2>Preguntas frecuentes</h2><details><summary>¿El programa cuenta con RVOE?</summary><p>Sí. La clave oficial está pendiente de confirmación para publicación.</p></details><details><summary>¿Tiene opción sabatina?</summary><p>Sí. El horario específico debe confirmarse con el plantel.</p></details><details><summary>¿Puedo descargar el plan?</summary><p>La descarga se habilitará únicamente cuando exista un PDF oficial.</p></details></section>
          <section class="content-card"><h2>Programas relacionados</h2><div class="program-grid related-grid">{related_cards}</div></section>
        </div>
      </div>
    </section>
    <div id="formulario-programa">{form_section('../')}</div>
"""
    base.page(p["url"], f"{p['name']} | Centro Universitario San Pablo", p["description"], content)


def admisiones_pages():
    process = '<div class="steps"><article><span>1</span><h3>Explora tu carrera</h3><p>Revisa la oferta académica confirmada.</p></article><article><span>2</span><h3>Solicita información</h3><p>Un asesor te comparte costos, horarios y plantel disponible.</p></article><article><span>3</span><h3>Reúne tus documentos</h3><p class="is-pending">PENDIENTE DE CONFIRMACIÓN</p></article><article><span>4</span><h3>Completa tu inscripción</h3><p>El plantel confirmará los pasos finales.</p></article></div>'
    base.page("admisiones/index.html", "Admisiones | Centro Universitario San Pablo", "Proceso de admisión, requisitos, costos, promociones y contacto.", f"""
    <section class="page-hero"><div class="container"><p class="eyebrow">Admisiones</p><h1>Da el primer paso para estudiar en San Pablo</h1><p>Te orientamos para elegir carrera, plantel, horarios y requisitos.</p></div></section>
    <section class="section"><div class="container">{process}</div></section>
    <section class="section section-muted"><div class="container feature-grid"><article><h2>Próximo periodo</h2><p class="is-pending">{PENDING}</p></article><article><h2>Requisitos</h2><p class="is-pending">{PENDING}</p></article><article><h2>Costos</h2><p>Licenciaturas desde $1,300 al mes. Doctorado: $1,800 al mes.</p></article><article><h2>Promociones</h2><p>Inscripción gratis y primer cuatrimestre por $699 para nuevo ingreso en licenciaturas.</p></article></div></section>
    {base.planteles_section('../')}
    <section class="section"><div class="container content-card"><h2>Preguntas frecuentes</h2><p>Consulta las respuestas principales en la sección de preguntas frecuentes.</p><a class="button button-outline" href="preguntas-frecuentes.html">Ver preguntas frecuentes</a></div></section>
    {form_section('../', 'Solicita apoyo de admisiones')}
""")
    base.page("admisiones/requisitos.html", "Requisitos de inscripción | Centro Universitario San Pablo", "Documentos solicitados para inscripción.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Admisiones</p><h1>Requisitos de inscripción</h1><p>Documentos oficiales por confirmar.</p></div></section><section class="section"><div class="container feature-grid"><article class="is-pending"><h2>Documentos solicitados</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Proceso de inscripción</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Horarios disponibles</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Formas de pago</h2><p>{PENDING}</p></article></div></section>')
    base.page("admisiones/costos-promociones.html", "Costos y promociones | Centro Universitario San Pablo", "Costos confirmados y promoción de nuevo ingreso.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Costos y promociones</p><h1>Invierte en tu futuro profesional</h1><p>Información confirmada sujeta a cambios y confirmación del plantel.</p></div></section><section class="section"><div class="container feature-grid"><article><h2>Colegiatura</h2><p>Licenciaturas desde $1,300 al mes.</p></article><article><h2>Primer cuatrimestre</h2><p>$699 para nuevo ingreso en licenciaturas.</p></article><article><h2>Inscripción</h2><p>Inscripción gratis para nuevo ingreso en licenciaturas.</p></article><article><h2>Doctorado</h2><p>$1,800 al mes. No aplica la promoción de licenciaturas.</p></article><article class="is-pending"><h2>Restricciones</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Vigencia</h2><p>{PENDING}</p></article><article><h2>Programas participantes</h2><p>Licenciaturas confirmadas. El Doctorado en Educación no participa en la promoción.</p></article></div></section>')
    base.page("admisiones/fechas-inicio.html", "Fechas de inicio | Centro Universitario San Pablo", "Fechas de inicio pendientes de confirmación.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Fechas de inicio</p><h1>Próximos periodos</h1><p>Las fechas de inicio se encuentran pendientes de confirmación.</p></div></section><section class="section"><div class="container feature-grid"><article class="is-pending"><h2>Próxima fecha</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Fecha límite</h2><p>{PENDING}</p></article><article><h2>Horarios</h2><p>{base.HOURS}</p></article><article class="is-pending"><h2>Estado de inscripciones</h2><p>{PENDING}</p></article></div></section>')
    base.page("admisiones/preguntas-frecuentes.html", "Preguntas frecuentes | Centro Universitario San Pablo", "Preguntas frecuentes de admisiones.", base.faq_page())


def universidad_pages():
    base.page("universidad/quienes-somos.html", "Quiénes somos | Centro Universitario San Pablo", "Presentación institucional del Centro Universitario San Pablo.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Universidad</p><h1>Quiénes somos</h1><p>Centro Universitario San Pablo es una institución educativa en León, Guanajuato, con oferta académica presencial y atención cercana.</p></div></section><section class="section"><div class="container feature-grid"><article><h2>Propósito</h2><p>Brindar formación profesional accesible con acompañamiento cercano.</p></article><article><h2>Atención cercana</h2><p>Orientación directa para elegir programa, plantel y horarios.</p></article><article><h2>Oferta académica</h2><p>Licenciaturas y Doctorado en Educación confirmados.</p></article><article><h2>Planteles</h2><p>Plantel Hidalgo y Plantel Centro en León.</p></article><article><h2>Compromiso educativo</h2><p>Programas presenciales, cuatrimestrales y con opción sabatina.</p></article></div></section>')
    timeline = ''.join(f'<article class="is-pending"><h2>{title}</h2><p>{PENDING}</p></article>' for title in ["Fundación", "Crecimiento", "Apertura de planteles", "Logros"])
    base.page("universidad/historia.html", "Historia | Centro Universitario San Pablo", "Historia institucional pendiente de confirmación.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Historia</p><h1>Trayectoria institucional</h1><p>No se publican fechas o logros sin confirmación.</p></div></section><section class="section"><div class="container feature-grid">{timeline}</div></section>')
    base.page("universidad/identidad-institucional.html", "Misión, visión y valores | Centro Universitario San Pablo", "Identidad institucional pendiente de confirmación.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Identidad institucional</p><h1>Misión, visión y valores</h1><p>El lema confirmado es SPIRITVS GLADIVS.</p></div></section><section class="section"><div class="container feature-grid"><article class="is-pending"><h2>Misión</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Visión</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Valores</h2><p>{PENDING}</p></article><article><h2>Lema</h2><p>SPIRITVS GLADIVS</p></article><article class="is-pending"><h2>Significado del logotipo</h2><p>{PENDING}</p></article></div></section>')
    base.page("universidad/modelo-educativo.html", "Modelo educativo | Centro Universitario San Pablo", "Modelo educativo con información confirmada.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Modelo educativo</p><h1>Formación profesional con acompañamiento cercano</h1><p>Programas presenciales, sistema cuatrimestral y opción sabatina.</p></div></section><section class="section"><div class="container feature-grid"><article><h2>Formación profesional</h2><p>Oferta académica orientada al desarrollo profesional.</p></article><article><h2>Acompañamiento</h2><p>Atención cercana durante el proceso de informes e inscripción.</p></article><article><h2>Modalidad</h2><p>Presencial.</p></article><article class="is-pending"><h2>Enfoque práctico</h2><p>{PENDING}</p></article><article><h2>Opción sabatina</h2><p>Confirmada; horarios específicos pendientes.</p></article></div></section>')
    rows = ''.join(f'<tr><td>{p["name"]}</td><td>{PENDING}</td><td>{PENDING}</td><td>{PENDING}</td><td>Presencial</td><td>{PENDING}</td><td>{PENDING}</td></tr>' for p in base.PROGRAMS)
    base.page("universidad/rvoe.html", "RVOE | Centro Universitario San Pablo", "Registro de RVOE preparado para datos oficiales.", f'<section class="page-hero"><div class="container"><p class="eyebrow">RVOE</p><h1>Información verificable por programa</h1><p>La institución confirma que las carreras cuentan con RVOE. No se publican claves falsas.</p></div></section><section class="section"><div class="container table-wrap"><table><thead><tr><th>Programa</th><th>Clave</th><th>Autoridad</th><th>Fecha del acuerdo</th><th>Modalidad autorizada</th><th>Plantel</th><th>Documento oficial</th></tr></thead><tbody>{rows}</tbody></table></div></section>')
    base.page("universidad/directorio.html", "Directorio | Centro Universitario San Pablo", "Directorio institucional pendiente de autorización.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Directorio</p><h1>Directorio institucional</h1><p>No se publican datos personales sin autorización.</p></div></section><section class="section"><div class="container table-wrap is-pending"><table><thead><tr><th>Nombre</th><th>Cargo</th><th>Área</th><th>Correo</th><th>Teléfono</th></tr></thead><tbody><tr><td>{PENDING}</td><td>{PENDING}</td><td>{PENDING}</td><td>{PENDING}</td><td>{PENDING}</td></tr></tbody></table></div></section>')


def vida_pages():
    gallery = """
    <div class="gallery-collage">
      <figure class="gallery-featured"><button class="gallery-open" type="button"><img src="../assets/comunidad-academica.webp" width="1600" height="1200" alt="Comunidad académica reunida" loading="lazy" decoding="async"></button><figcaption>Comunidad académica.</figcaption></figure>
      <figure><button class="gallery-open" type="button"><img src="../assets/congreso-estudiantes.webp" width="2048" height="1536" alt="Estudiantes en congreso académico" loading="lazy" decoding="async"></button><figcaption>Congresos.</figcaption></figure>
      <figure><button class="gallery-open" type="button"><img src="../assets/graduacion-grupo.webp" width="1600" height="1200" alt="Grupo de egresados en graduación" loading="lazy" decoding="async"></button><figcaption>Graduaciones.</figcaption></figure>
      <figure><button class="gallery-open" type="button"><img src="../assets/reconocimiento-egresada.webp" width="1142" height="1600" alt="Egresada con reconocimiento" loading="lazy" decoding="async"></button><figcaption>Reconocimientos.</figcaption></figure>
      <figure><button class="gallery-open" type="button"><img src="../assets/actividad-cultural.webp" width="2048" height="1536" alt="Actividad cultural universitaria" loading="lazy" decoding="async"></button><figcaption>Actividades.</figcaption></figure>
    </div>"""
    base.page("vida-universitaria/index.html", "Vida universitaria | Centro Universitario San Pablo", "Actividades, congresos, graduaciones y comunidad San Pablo.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Vida universitaria</p><h1>Experiencia San Pablo</h1><p>Actividades, congresos, graduaciones, reconocimientos y comunidad.</p></div></section><section class="section"><div class="container feature-grid"><article><h2>Actividades</h2><p>Momentos de convivencia y aprendizaje.</p></article><article><h2>Congresos</h2><p>Participación en espacios académicos.</p></article><article><h2>Graduaciones</h2><p>Reconocimiento al esfuerzo académico.</p></article><article><h2>Reconocimientos</h2><p>Entrega de reconocimientos institucionales.</p></article><article class="is-pending"><h2>Noticias recientes</h2><p>{PENDING}</p></article></div></section>')
    card = f'<article class="program-card is-pending"><h2>{PENDING}</h2><p>Fecha, título, resumen e imagen pendientes.</p><a class="button button-outline" href="#">Leer más</a></article>'
    base.page("vida-universitaria/noticias.html", "Noticias | Centro Universitario San Pablo", "Noticias institucionales pendientes.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Noticias</p><h1>Noticias recientes</h1><p>No se inventan noticias. Este espacio queda preparado para publicaciones oficiales.</p></div></section><section class="section"><div class="container program-grid">{card}{card}{card}</div></section>')
    event = f'<article class="program-card is-pending"><h2>{PENDING}</h2><p>Fecha, hora, plantel, descripción y estado pendientes.</p></article>'
    base.page("vida-universitaria/eventos.html", "Eventos | Centro Universitario San Pablo", "Eventos institucionales pendientes.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Eventos</p><h1>Calendario de eventos</h1><p>Se publicarán únicamente eventos confirmados.</p></div></section><section class="section"><div class="container program-grid">{event}{event}{event}</div></section>')
    base.page("vida-universitaria/galeria.html", "Galería | Centro Universitario San Pablo", "Galería con fotografías reales de la comunidad San Pablo.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Galería</p><h1>Momentos San Pablo</h1><p>Fotografías reales con categorías, textos alternativos y vista ampliada.</p></div></section><section class="section"><div class="container"><div class="filters"><button class="button button-outline" type="button">Comunidad</button><button class="button button-outline" type="button">Congresos</button><button class="button button-outline" type="button">Graduaciones</button></div>{gallery}</div></section>')
    base.page("vida-universitaria/egresados.html", "Egresados | Centro Universitario San Pablo", "Egresados, testimonios e historias pendientes.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Egresados</p><h1>Comunidad de egresados</h1><p>Se publicarán únicamente testimonios e historias con autorización.</p></div></section><section class="section"><div class="container feature-grid"><article class="is-pending"><h2>Testimonios</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Historias</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Logros</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Vinculación</h2><p>{PENDING}</p></article><article class="is-pending"><h2>Bolsa de trabajo futura</h2><p>{PENDING}</p></article></div></section>')


def plantel_page(key):
    c = base.PLANTELES[key]
    image = '<div class="campus-photo-placeholder">Fotografía exterior pendiente</div>' if key == "hidalgo" else '<img src="../assets/plantel-emiliano-zapata.webp" width="960" height="1280" alt="Espacio institucional del Plantel Centro" loading="lazy" decoding="async">'
    base.page(f"planteles/{key}.html", f"{c['name']} | Centro Universitario San Pablo", f"Dirección, teléfono y horarios de {c['name']}.", f"""
    <section class="page-hero"><div class="container"><p class="eyebrow">Planteles</p><h1>{c['name']}</h1><p>{c['address']}</p></div></section>
    <section class="section"><div class="container campus-grid"><article class="campus-card"><div class="campus-media">{image}</div><div class="campus-body"><h2>Información del plantel</h2><p><strong>Dirección:</strong> {c['address']}</p><p><strong>Teléfono:</strong> <a href="tel:{c['tel']}">{c['phone']}</a></p><p><strong>Horarios:</strong> {base.HOURS}</p><p class="is-pending"><strong>Carreras disponibles:</strong> {PENDING}</p><p class="is-pending"><strong>Referencias:</strong> {PENDING}</p><div class="card-actions"><a class="button button-outline" href="tel:{c['tel']}">Llamar</a><a class="button button-primary" href="https://wa.me/{c['wa']}" target="_blank" rel="noopener">WhatsApp</a><a class="button button-outline" href="{c['map']}" target="_blank" rel="noopener">Cómo llegar</a></div></div></article><article class="content-card is-pending"><h2>Galería del plantel</h2><p>{PENDING}</p><!-- PENDIENTE DE CONFIRMACIÓN: fotografía exterior y galería oficial --></article></div></section>
    {form_section('../', 'Agenda una visita al plantel')}
""")


def planteles_pages():
    base.page("planteles/index.html", "Planteles | Centro Universitario San Pablo", "Planteles Hidalgo y Centro en León.", base.planteles_section("../") + form_section("../", "Agenda una visita"))
    plantel_page("hidalgo")
    plantel_page("centro")


def legal_pages():
    legal = '<div class="feature-grid">' + ''.join(f'<article class="is-pending"><h2>{x}</h2><p>{PENDING}</p></article>' for x in ["Responsable", "Domicilio", "Datos recopilados", "Finalidad", "Transferencias", "Derechos ARCO", "Contacto", "Fecha de actualización"]) + '</div>'
    base.page("legales/aviso-privacidad.html", "Aviso de privacidad | Centro Universitario San Pablo", "Plantilla de aviso de privacidad pendiente de autorización.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Legal</p><h1>Aviso de privacidad</h1><p>No se redactan datos legales no confirmados.</p></div></section><section class="section"><div class="container">{legal}</div></section>')
    base.page("legales/terminos.html", "Términos y condiciones | Centro Universitario San Pablo", "Plantilla de términos pendiente de autorización.", f'<section class="page-hero"><div class="container"><p class="eyebrow">Legal</p><h1>Términos y condiciones</h1><p>Las condiciones legales deberán incorporarse cuando sean autorizadas.</p></div></section><section class="section"><div class="container">{legal}</div></section>')


def contact_page():
    base.page("contacto/index.html", "Contacto | Centro Universitario San Pablo", "Solicita información por WhatsApp.", f"""
    <section class="page-hero"><div class="container"><p class="eyebrow">Contacto</p><h1>Recibe información personalizada</h1><p>Selecciona carrera y plantel para enviar tu solicitud al WhatsApp correspondiente.</p></div></section>
    <section class="section"><div class="container contact-grid"><div class="contact-panel"><h2>Datos de contacto</h2><p><strong>Hidalgo:</strong> <a href="tel:{base.PLANTELES['hidalgo']['tel']}">{base.PLANTELES['hidalgo']['phone']}</a></p><p><strong>Centro:</strong> <a href="tel:{base.PLANTELES['centro']['tel']}">{base.PLANTELES['centro']['phone']}</a></p><p><strong>Horarios:</strong> {base.HOURS}</p><p class="social-row"><a href="{base.SOCIALS['facebook']}" target="_blank" rel="noopener">Facebook</a><a href="{base.SOCIALS['instagram']}" target="_blank" rel="noopener">Instagram</a></p><p><a class="button button-outline" href="{base.PLANTELES['centro']['map']}" target="_blank" rel="noopener">Ver mapa</a></p></div>{contact_form('../')}</div></section>
""")


def datos_pendientes():
    text = f"""# Datos pendientes de confirmación

El sitio está preparado para completar esta información sin inventar datos.

- RVOE: claves, autoridad, fecha del acuerdo, modalidad autorizada, plantel y documento oficial por programa.
- Planes de estudio: mapa curricular por cuatrimestre y PDF oficial descargable.
- Fechas: próximo inicio, fecha límite y estado de inscripciones.
- Requisitos: documentos solicitados y proceso formal de inscripción.
- Costos: desglose completo, formas de pago y condiciones.
- Promociones: restricciones, vigencia y documentos aplicables.
- Testimonios: nombre, carrera, generación, fotografía, autorización y texto real.
- Historia: fundación, crecimiento, apertura de planteles y logros con fechas confirmadas.
- Misión, visión y valores.
- Directorio: nombre, cargo, área, correo y teléfono autorizados.
- Convenios.
- Formas de titulación.
- Revalidaciones.
- Fotografías: exteriores oficiales de planteles y galerías adicionales.
- Aviso de privacidad: responsable, domicilio, finalidades, derechos ARCO y fecha de actualización.
- Información legal y términos.
- Maestrías: nombres oficiales, duración, modalidad, RVOE, costos y plantel antes de publicar.
"""
    (ROOT / "DATOS-PENDIENTES.md").write_text(text, encoding="utf-8")


def append_styles():
    css = """

.compact-grid{grid-template-columns:repeat(3,minmax(0,1fr));margin-top:16px}
.compact-grid article{padding:18px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);border-radius:18px}
.related-grid{grid-template-columns:repeat(3,minmax(0,1fr))}
.table-wrap{overflow:auto;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:22px;padding:12px}
table{width:100%;border-collapse:collapse;min-width:760px}
th,td{padding:14px;border-bottom:1px solid rgba(255,255,255,.1);text-align:left;vertical-align:top}
th{color:var(--gold-2);font-family:Sora,sans-serif}
.gallery-open{display:block;width:100%;height:100%;border:0;padding:0;background:transparent;color:inherit;cursor:pointer}
.image-lightbox{position:fixed;inset:0;z-index:80;background:rgba(0,0,0,.86);display:none;align-items:center;justify-content:center;padding:24px}
.image-lightbox.is-open{display:flex}
.image-lightbox img{max-height:86vh;max-width:92vw;border-radius:18px;box-shadow:var(--shadow)}
.image-lightbox button{position:fixed;right:22px;top:22px;width:48px;height:48px;border-radius:50%;border:1px solid var(--line);background:#fff;color:#111;font-size:28px}
@media (max-width:760px){.compact-grid,.related-grid{grid-template-columns:1fr}table{min-width:680px}}
"""
    path = ROOT / "styles.css"
    current = path.read_text(encoding="utf-8")
    if ".table-wrap" not in current:
        path.write_text(current + css, encoding="utf-8")


def patch_script_lightbox():
    path = ROOT / "script.js"
    current = path.read_text(encoding="utf-8")
    if "image-lightbox" in current:
        return
    extra = r"""

const galleryButtons=document.querySelectorAll(".gallery-open");
if(galleryButtons.length){
  const lightbox=document.createElement("div");
  let lastTrigger=null;
  lightbox.className="image-lightbox";
  lightbox.setAttribute("role","dialog");
  lightbox.setAttribute("aria-modal","true");
  lightbox.setAttribute("aria-label","Vista ampliada de fotografía");
  lightbox.innerHTML='<button type="button" aria-label="Cerrar imagen">×</button><img alt="">';
  document.body.appendChild(lightbox);
  const image=lightbox.querySelector("img");
  const closeButton=lightbox.querySelector("button");
  const close=()=>{lightbox.classList.remove("is-open");document.body.classList.remove("menu-open");lastTrigger?.focus()};
  galleryButtons.forEach(button=>button.addEventListener("click",()=>{const source=button.querySelector("img");if(!source)return;lastTrigger=button;image.src=source.src;image.alt=source.alt;lightbox.classList.add("is-open");document.body.classList.add("menu-open");closeButton.focus()}));
  lightbox.addEventListener("click",event=>{if(event.target===lightbox)close()});
  closeButton.addEventListener("click",close);
  document.addEventListener("keydown",event=>{if(event.key==="Escape"&&lightbox.classList.contains("is-open"))close()});
}
"""
    path.write_text(current + extra, encoding="utf-8")


def main():
    for p in base.PROGRAMS:
        program_page(p)
    admisiones_pages()
    universidad_pages()
    vida_pages()
    planteles_pages()
    contact_page()
    legal_pages()
    datos_pendientes()
    append_styles()
    patch_script_lightbox()


if __name__ == "__main__":
    main()
