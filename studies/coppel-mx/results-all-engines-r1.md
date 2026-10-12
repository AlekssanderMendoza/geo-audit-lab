# Resultados consolidados — Ronda 1

**Estudio:** GEO-COPPEL-001
**Mercado:** México
**Motores:** ChatGPT Search (`ChatGPT` en el CSV), Gemini y Perplexity
**Archivo:** `results-all-engines-r1.csv`

## Alcance

La ronda 1 contiene 45 observaciones: 15 consultas por motor,
de las cuales 12 son genéricas y 3 mencionan explícitamente Coppel.

El protocolo v1.0 contempla 135 ejecuciones distribuidas
en tres rondas. Las rondas 2 y 3 están pendientes.

## Resultados descriptivos

Los indicadores siguientes utilizan únicamente consultas genéricas.

| Motor | Mención | Recomendación | Cita oficial |
|---|---:|---:|---:|
| ChatGPT Search | 10/12 (83.3 %) | 9/12 (75.0 %) | 4/12 (33.3 %) |
| Gemini | 8/12 (66.7 %) | 8/12 (66.7 %) | 5/12 (41.7 %) |
| Perplexity | 8/12 (66.7 %) | 8/12 (66.7 %) | 7/12 (58.3 %) |

En las tres consultas explícitas de marca, cada motor registró
3 menciones, 0 recomendaciones y 3 citas. Estas consultas se
excluyen de la tasa primaria de mención espontánea.

Los indicadores no son mutuamente excluyentes.

## Procedencia del dataset

El CSV público se derivó de
`data/processed/observations_round1_normalized.csv`
del laboratorio local, mediante unión por `query_id`
con `queries-v1.0.csv`.

Contiene 45 registros y 11 columnas. Los indicadores binarios
se representan mediante `1` (verdadero) y `0` (falso).

No incluye notas libres, rutas locales, capturas ni metadatos
detallados de sesión.

Los 15 registros de ChatGPT se contrastaron con
`results-chatgpt-r1.csv`: no se encontraron diferencias
en los tres indicadores evaluados.

## Interpretación y limitaciones

- Investigación independiente, exploratoria y no representativa.
- Las consultas se seleccionaron intencionalmente.
- Una cita significa que se identificó una referencia visible
  al dominio oficial como fuente, según el codebook;
  no demuestra por sí sola que una afirmación esté respaldada.
- No se ha verificado la equivalencia de las condiciones
  de ejecución entre motores; los metadatos de sesión
  están incompletos.
- Las clasificaciones proceden del proceso de codificación
  del estudio; no constituyen una auditoría independiente integral.
- Las diferencias descriptivas no permiten establecer
  significancia estadística, causalidad o estabilidad temporal.
- No se infieren efectos en ventas, tráfico o preferencia de marca.
- Las rondas 2 y 3 siguen pendientes.

Consulte `protocol-v1.0.md`, `codebook.md` y
`limitations-and-deviations.md` para el contexto metodológico.
