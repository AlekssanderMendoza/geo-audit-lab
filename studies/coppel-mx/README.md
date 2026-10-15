# Coppel México — GEO Audit Lab

**Estudio:** GEO-COPPEL-001  
**Mercado:** México  
**Motores:** ChatGPT Search, Gemini y Perplexity  
**Corte:** 14 de octubre de 2026  
**Estado:** R1 y R2 completadas; R3 pendiente.

Investigación independiente y exploratoria sobre la aparición de Coppel México en respuestas de motores generativos.

## Estado del experimento

| Ronda | Observaciones | Estado |
|---|---:|---|
| R1 | 45 | Completada |
| R2 | 45 | Completada |
| R3 | 45 previstas | Pendiente |
| **Total** | **90 de 135 previstas** | **Corte preliminar** |

Cada ronda comprende 15 consultas por motor: 12 genéricas y 3 explícitas de marca.

El indicador principal es la tasa de mención espontánea de Coppel en consultas genéricas. La recomendación y la citación al dominio oficial son indicadores secundarios.

## Navegación del estudio

| Área | Recursos |
|---|---|
| Metodología | [Protocolo v1.0](protocol-v1.0.md) · [Consultas](queries-v1.0.csv) · [Codebook](codebook.md) |
| Resultados R1 | [Dataset](results-all-engines-r1.csv) · [Análisis descriptivo](results-all-engines-r1.md) · [ChatGPT histórico — Entrega 01](results-chatgpt-r1.csv) |
| Resultados R2 | [Dataset](results-all-engines-r2.csv) |
| Evidencias R1 | [Documentación e índice](evidence/round-1/README.md) · [Índice CSV](evidence/round-1/EVIDENCE-INDEX.csv) |
| Evidencias R2 | [Documentación e índice](evidence/round-2/README.md) · [Índice CSV](evidence/round-2/EVIDENCE-INDEX.csv) |
| Auditoría | [Citas](citation-audit.md) · [Limitaciones y desviaciones](limitations-and-deviations.md) |
| Trazabilidad | [Manifiesto de evidencias](../../EVIDENCE-MANIFEST.md) · [Historial de cambios](../../CHANGELOG.md) |

## Resultados históricos — Ronda 1

Se registraron 45 observaciones, distribuidas entre los tres motores.

Los siguientes indicadores corresponden exclusivamente a las 12 consultas genéricas por motor.

| Motor | Mención espontánea | Recomendación | Cita oficial |
|---|---:|---:|---:|
| ChatGPT Search | 10/12 (83.3 %) | 9/12 (75.0 %) | 4/12 (33.3 %) |
| Gemini | 8/12 (66.7 %) | 8/12 (66.7 %) | 5/12 (41.7 %) |
| Perplexity | 8/12 (66.7 %) | 8/12 (66.7 %) | 7/12 (58.3 %) |

En las tres consultas explícitas de marca, cada motor registró tres menciones, cero recomendaciones y tres citas oficiales.

Los indicadores no son mutuamente excluyentes.

Estos resultados describen exclusivamente R1. No deben interpretarse como resultados combinados de R1 y R2.

## Corte preliminar — R1 + R2

Las dos primeras rondas comprenden 90 observaciones de las mismas 15 consultas en los tres motores.

Los datasets públicos consolidados contienen 45 registros y 11 columnas por ronda.

Las 90 observaciones fueron reconciliadas con el registro maestro del laboratorio. Esta comprobación interna no equivale a una auditoría independiente de la codificación.

- [Consultar resultados consolidados de R1](results-all-engines-r1.csv)
- [Consultar resultados consolidados de R2](results-all-engines-r2.csv)
- [Consultar limitaciones y desviaciones](limitations-and-deviations.md)

La comparación entre rondas permite describir diferencias observadas entre ejecuciones. No demuestra estabilidad temporal, significancia estadística ni causalidad.

El análisis comparativo completo de R1 y R2 queda pendiente de publicación como Entrega 03.

## Evidencias visuales

### Ronda 1

El inventario local de R1 comprende 177 capturas:

- ChatGPT Search: 70 imágenes.
- Gemini: 59 imágenes.
- Perplexity: 48 imágenes.

Las 107 capturas de Gemini y Perplexity ya están publicadas.
Las 70 capturas de ChatGPT Search se incorporaron e indexaron
en el repositorio local, con verificación SHA-256 satisfactoria.

Las 70 capturas de ChatGPT Search R1 fueron revisadas y aprobadas visualmente por el investigador. Esta revisión no constituye una auditoría independiente.
Por tanto, estas 70 capturas aún no se consideran publicadas en GitHub.

[Consultar evidencias e índice de R1](evidence/round-1/README.md).

### Ronda 2

Se encuentran publicadas 151 capturas correspondientes a:

- ChatGPT Search: 54 imágenes.
- Gemini: 51 imágenes.
- Perplexity: 46 imágenes.

Las capturas de R2 cuentan con un índice CSV de archivos y huellas SHA-256.

[Consultar evidencias e índice de R2](evidence/round-2/README.md).

Las revisiones visuales efectuadas por el investigador no equivalen a una auditoría independiente y exhaustiva de privacidad, integridad o correspondencia entre respuestas y capturas.

## Auditoría de citas

La auditoría focalizada de la Entrega 01 documenta la decisión de conservar `CRED-02: cited=true`, diferenciando una fuente visible del enlace comercial «Ver en Coppel».

La decisión y la evidencia seleccionada se conservan en [citation-audit.md](citation-audit.md).

## Limitaciones y reproducibilidad

El protocolo original permanece congelado en su versión 1.0.

El estudio utiliza un conjunto acotado de consultas y ejecuciones documentadas. No constituye una muestra representativa del comportamiento general de los motores generativos.

La presencia de una cita al dominio oficial no garantiza que todas las afirmaciones de una respuesta estén respaldadas por esa fuente.

Los indicadores de mención, recomendación y citación no equivalen a ventas, tráfico, participación de mercado ni preferencia de consumidores.

La revisión independiente y exhaustiva de la codificación de las respuestas permanece pendiente.

Las discrepancias históricas de integridad y las limitaciones de procedencia se documentan en el [manifiesto de evidencias](../../EVIDENCE-MANIFEST.md) y en [limitaciones y desviaciones](limitations-and-deviations.md).

## Próximos pasos

- Publicar en GitHub las 70 capturas de ChatGPT Search R1, ya incorporadas, indexadas y revisadas visualmente en el repositorio local.
- Elaborar la comparación descriptiva R1 frente a R2 para la Entrega 03.
- Ejecutar y documentar R3 conforme al protocolo.

## Independencia

Este estudio no cuenta con aval de Coppel ni de los proveedores de motores generativos.
