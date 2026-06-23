# Centro Universitario San Pablo

Landing page institucional estática para consultar oferta académica, promociones, planteles y solicitar información por WhatsApp.

## Archivos principales

- `index.html`: contenido, SEO, datos estructurados, formulario y secciones.
- `styles.css`: diseño responsive y accesibilidad visual.
- `script.js`: navegación, validación, WhatsApp, galería y eventos.
- `analytics.js`: configuración opcional de Google Analytics 4.
- `assets/`: logotipo, fotografías originales y versiones WebP optimizadas.
- `robots.txt`, `sitemap.xml` y `.nojekyll`: publicación e indexación en GitHub Pages.

## Actualizar promociones y costos

1. Busca en `index.html` los textos `$699`, `$1,300` y `$1,800`.
2. Actualiza portada, ficha académica, sección de promoción y preguntas frecuentes.
3. No publiques una vigencia hasta recibir la fecha oficial.
4. Revisa también la nota legal del pie de página.

## Actualizar carreras

1. Modifica la tarjeta correspondiente dentro de `#oferta` en `index.html`.
2. Mantén sincronizada la opción del campo `#program` del formulario.
3. Actualiza el objeto `Course` correspondiente dentro del bloque JSON-LD del `<head>`.
4. Si existe un plan descargable, agrega un enlace con `data-plan-download` y `data-program="Nombre del programa"` para medir la descarga.

## Capturar RVOE

Busca `PENDIENTE DE CONFIRMACIÓN` dentro de `index.html`. Para cada programa completa:

- Clave de RVOE.
- Autoridad que lo otorgó.
- Fecha del acuerdo.
- Modalidad autorizada.
- Plantel correspondiente.
- Enlace al documento comprobatorio.

No elimines la nota pendiente hasta contar con el documento oficial.

## Actualizar fechas, requisitos y pagos

Edita `#requisitos` y las preguntas frecuentes en `index.html`. Confirma antes de publicar:

- Próximo inicio y fecha límite.
- Documentos solicitados.
- Horarios por carrera y plantel.
- Formas de pago.
- Revalidación y titulación.
- Vigencia de promociones.

## Actualizar teléfonos y WhatsApp

Los números aparecen en tres lugares:

1. `index.html`: enlaces `tel:`, `wa.me`, footer y JSON-LD.
2. `script.js`: objeto `campusWhatsApp`.
3. Mensajes y botones de cada plantel.

Usa el formato internacional `52 + 10 dígitos` para WhatsApp y diez dígitos para `tel:`.

## Actualizar planteles

1. Edita la tarjeta dentro de `#planteles`.
2. Actualiza dirección, teléfono, horario, Google Maps y carreras disponibles.
3. Actualiza también `PostalAddress` en el JSON-LD y los datos del footer.
4. Sustituye los placeholders únicamente por fotografías oficiales.

## Configurar Google Analytics 4

1. Abre `analytics.js`.
2. Coloca el identificador real en `GA4_MEASUREMENT_ID`:

```js
const GA4_MEASUREMENT_ID = "G-XXXXXXXXXX";
```

Sin identificador, el sitio no descarga Google Analytics ni envía datos. Los eventos preparados son:

- `click_whatsapp`
- `click_call`
- `form_submit`
- `generate_lead`
- `get_directions`
- `view_academic_offer`
- `view_plan`
- `download_plan`

## Optimizar nuevas fotografías

Con Python y Pillow disponibles, ejecuta:

```powershell
python scripts/optimize_images.py
```

El proceso conserva los JPG originales y crea WebP completos y variantes de 640 px. Después agrega `width`, `height`, `srcset`, `sizes`, `loading="lazy"` y `decoding="async"` en `index.html`.

## Publicar en GitHub Pages

1. Sube los archivos de la raíz del proyecto, no la carpeta contenedora.
2. En GitHub abre `Settings > Pages`.
3. Selecciona la rama de publicación y la carpeta `/(root)`.
4. Espera el despliegue y abre `https://lupixito.github.io/centro-universitario-san-pablo/`.

El sitio no requiere compilación, servidor, framework ni configuración adicional.

## Antes de publicar

- Reemplaza el aviso de privacidad provisional por el documento autorizado.
- Captura las claves y documentos oficiales de RVOE.
- Confirma fechas, requisitos, formas de pago y vigencias.
- Agrega testimonios solamente con autorización.
- Comprueba todos los números y enlaces de mapas.
