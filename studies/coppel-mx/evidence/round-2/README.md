# Evidencia visual — Ronda 2

**Estudio:** GEO-COPPEL-001
**Corte:** 14 de octubre de 2026
**Estado:** índice de integridad preparado; revisión visual y de privacidad pendiente.

## Cobertura

Se identificaron 151 capturas PNG correspondientes a R2:

| Motor | Capturas | Consultas cubiertas |
|---|---:|---:|
| ChatGPT Search | 54 | 15/15 |
| Gemini | 51 | 15/15 |
| Perplexity | 46 | 15/15 |
| **Total** | **151** | **45/45 combinaciones** |

Las consultas se identificaron mediante convenciones de nombres
de archivo. Esta correspondencia no constituye una verificación
visual independiente del contenido de las imágenes.

## Índice de integridad

El archivo [EVIDENCE-INDEX.csv](EVIDENCE-INDEX.csv) contiene:

- `round`: ronda del experimento.
- `engine`: motor generativo.
- `query_id`: identificador de consulta.
- `filename`: nombre de la captura.
- `source_path`: ruta relativa al laboratorio local.
- `size_bytes`: tamaño del archivo.
- `sha256`: huella SHA-256 del contenido.

Se verificaron 151 rutas únicas y 151 hashes contra los
archivos originales, sin diferencias ni archivos faltantes
en el momento de la comprobación.

## Alcance de la publicación

Este directorio publica el índice de integridad, no las
151 imágenes originales.

Las rutas de `source_path` son referencias de procedencia
dentro de `geo_coppel_v1`. No son enlaces públicos ni
permiten descargar las capturas desde este repositorio.

Los hashes permiten contrastar copias disponibles de los
archivos originales, pero no sustituyen el acceso a las
imágenes ni certifican su contenido.

## Limitaciones y trabajo pendiente

- Completar la revisión visual de las capturas.
- Revisar privacidad y posibles datos de sesión.
- Verificar exhaustivamente la correspondencia entre
  cada captura y la respuesta registrada.
- Documentar cualquier anonimización o edición futura.
- Mantener R3 como pendiente hasta su ejecución.

Este índice forma parte del corte preliminar R1 + R2
de 90 observaciones. No representa el cierre del estudio.
