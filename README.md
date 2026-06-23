# Centro Universitario San Pablo

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
