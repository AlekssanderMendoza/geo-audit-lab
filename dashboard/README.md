# Dashboard exploratorio — GEO Audit Lab

## Estudio

**Identificador:** GEO-COPPEL-001
**Mercado:** México
**Corte de datos:** 14 de octubre de 2026
**Estado:** R1 y R2 completadas; R3 pendiente.

Dashboard exploratorio de la presencia de Coppel México en
respuestas de ChatGPT Search, Gemini y Perplexity.

## Datos

La aplicación utiliza los CSV originales del repositorio:

- `studies/coppel-mx/results-all-engines-r1.csv` (45 observaciones).
- `studies/coppel-mx/results-all-engines-r2.csv` (45 observaciones).

**Total registrado: 90 observaciones.**

Cada ronda contiene 12 consultas genéricas y 3 de marca por motor.

## Instalación

Desde la raíz del repositorio, con Python 3.14:

1. Crear el entorno: `python3 -m venv .venv`
2. Activarlo en macOS/Linux: `source .venv/bin/activate`
3. Instalar dependencias: `python -m pip install -r requirements.txt`
4. Ejecutar: `streamlit run dashboard/app.py`

## Funcionalidades

- Comparación de indicadores entre R1 y R2.
- Desglose por motor generativo.
- Filtros por motor, ronda y tipo de consulta.
- Visualización de porcentajes y denominadores.

## Indicadores

- **Mención:** aparición explícita de Coppel.
- **Recomendación:** recomendación explícita de Coppel.
- **Cita oficial:** referencia al dominio oficial de Coppel.

Los indicadores no son mutuamente excluyentes.

La mención espontánea se mide exclusivamente en consultas genéricas.
Las consultas de marca son exploratorias y no cuentan como
menciones espontáneas.

## Limitaciones

Los resultados no representan el comportamiento general de los motores.
Las diferencias entre rondas no prueban causalidad, significancia
estadística ni estabilidad temporal.

La revisión independiente y exhaustiva de la codificación está pendiente.
R3 no se ha ejecutado.

El dashboard no sustituye el protocolo, el diccionario de codificación
ni el manifiesto de evidencias del repositorio.

## Independencia

Investigación independiente sin aval de Coppel ni de los proveedores
de motores generativos.
