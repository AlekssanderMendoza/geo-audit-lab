# Evidencia visual — Ronda 2

**Estudio:** GEO-COPPEL-001
**Corte:** 14 de octubre de 2026
**Estado:** 151 capturas incorporadas al repositorio local; integridad SHA-256 verificada; revisión visual preliminar completada.

## Cobertura

| Motor | Capturas | Consultas cubiertas |
|---|---:|---:|
| ChatGPT Search | 54 | 15/15 |
| Gemini | 51 | 15/15 |
| Perplexity | 46 | 15/15 |
| **Total** | **151** | **45/45 combinaciones** |

Las consultas se identificaron mediante convenciones de nombres de archivo. La revisión visual preliminar no constituye una verificación individual exhaustiva de la correspondencia entre cada captura y su respuesta registrada.

## Organización de las evidencias

Las imágenes se encuentran organizadas en:

- `chatgpt/`: 54 capturas.
- `gemini/`: 51 capturas.
- `perplexity/`: 46 capturas.

Los archivos conservan sus nombres originales.

## Índice de integridad

El archivo [EVIDENCE-INDEX.csv](EVIDENCE-INDEX.csv) contiene:

- `round`: ronda del experimento.
- `engine`: motor generativo.
- `query_id`: identificador de consulta.
- `filename`: nombre de la captura.
- `source_path`: ruta relativa al laboratorio local.
- `size_bytes`: tamaño del archivo.
- `sha256`: huella SHA-256 del contenido.

Se verificaron 151 rutas únicas y 151 hashes contra los archivos originales, sin diferencias ni archivos faltantes en el momento de la comprobación.

También se contrastaron los hashes SHA-256 de las 151 imágenes copiadas al repositorio con los originales del laboratorio, sin diferencias.

## Alcance de la publicación

Este directorio está preparado para publicar las 151 imágenes originales junto con su índice de integridad. Su disponibilidad pública dependerá de completar el commit y el push correspondientes.

Las rutas de `source_path` son referencias de procedencia dentro de `geo_coppel_v1`; no son enlaces públicos. Las imágenes publicadas se localizarán en las subcarpetas por motor.

Los hashes permiten comprobar la integridad de los archivos, pero no certifican por sí solos su contenido ni su correspondencia metodológica.

## Revisión visual y privacidad

Se realizó una revisión visual preliminar de las 151 capturas mediante mosaicos.

No se identificaron datos personales evidentes ni credenciales visibles en esa revisión. Se observaron elementos de interfaz, fuentes, referencias comerciales y, en algunas capturas, resultados geolocalizados.

La revisión mediante mosaicos tiene limitaciones de resolución y no garantiza la detección de todos los detalles pequeños o sensibles.

No se aplicaron modificaciones ni anonimización a las imágenes incorporadas.

## Limitaciones y trabajo pendiente

- Verificar exhaustivamente la correspondencia entre cada captura y la respuesta registrada.
- Mantener documentadas las limitaciones de la revisión visual y de privacidad.
- Documentar cualquier anonimización o edición futura, si fuese necesaria.
- Mantener R3 como pendiente hasta su ejecución.

Estas evidencias forman parte del corte preliminar R1 + R2 de 90 observaciones. No representan el cierre del estudio.
