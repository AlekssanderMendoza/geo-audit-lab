from pathlib import Path

import pandas as pd
import streamlit as st
from filters import render_filters

st.set_page_config(
    page_title="GEO Audit Lab | Coppel México",
    page_icon="🧪",
    layout="wide",
)

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "studies" / "coppel-mx"

METRICS = {
    "coppel_mentioned": "Mención",
    "coppel_recommended": "Recomendación",
    "coppel_cited": "Cita oficial",
}


@st.cache_data
def load_data():
    frames = []

    for round_number in (1, 2):
        path = DATA_DIR / f"results-all-engines-r{round_number}.csv"
        frame = pd.read_csv(path)

        if len(frame) != 45:
            raise ValueError(
                f"Ronda {round_number}: se esperaban 45 registros."
            )

        if not frame["round"].eq(round_number).all():
            raise ValueError(
                f"Ronda {round_number}: identificador inconsistente."
            )

        frames.append(frame)

    return pd.concat(frames, ignore_index=True)


st.title("🧪 GEO AUDIT LAB")
st.subheader("Coppel México | Entrega 03")
st.markdown("### Mencionar no es recomendar, y recomendar no es citar")

try:
    data = load_data()
except (OSError, ValueError, KeyError) as error:
    st.error(f"No fue posible validar los datos: {error}")
    st.stop()

# Controles de exploración.
filtered_data, selected_type = render_filters(data)

if filtered_data.empty:
    st.warning("No hay observaciones para los filtros seleccionados.")
    st.stop()

# Las visualizaciones utilizan exclusivamente la selección activa.
generic = filtered_data

if selected_type == "generic":
    st.caption("Vista filtrada: consultas genéricas · mención espontánea")
else:
    st.caption(
        "Vista exploratoria: la selección incluye consultas de marca. "
        "La mención no debe interpretarse como espontánea."
    )

st.caption(
    f"Observaciones seleccionadas: {len(generic)} "
    f"de {len(data)} registros originales."
)

st.caption(
    f"{len(data)} observaciones · "
    f"{data['engine'].nunique()} motores · "
    f"{data['round'].nunique()} rondas · "
    "R3 pendiente"
)

st.markdown("### Indicadores de la selección")

if selected_type == "generic":
    st.caption("Mención espontánea, recomendación y cita oficial.")
else:
    st.caption(
        "Mención, recomendación y cita oficial. "
        "Esta selección no representa exclusivamente menciones espontáneas."
    )

results = generic.groupby("round")[list(METRICS)].agg(["sum", "count"])

for column, label in METRICS.items():
    parts = []

    for round_number in sorted(generic["round"].unique()):
        count = int(results.loc[round_number, (column, "sum")])
        total = int(results.loc[round_number, (column, "count")])
        rate = 100 * count / total

        parts.append(
            f"R{round_number}: {count}/{total} ({rate:.1f} %)"
        )

    st.write(f"**{label}:** " + " → ".join(parts))

st.info(
    "Las tres métricas son binarias y no excluyentes. "
    "El KPI principal del estudio utiliza exclusivamente consultas genéricas. "
    "Las vistas con consultas de marca son exploratorias."
)

st.caption("SEO · GEO · DATA ANALYTICS")

# Primera visualización: comparación de métricas entre rondas.
import plotly.express as px

chart_rows = []

for round_number in sorted(generic["round"].unique()):
    round_data = generic.loc[generic["round"] == round_number]

    for column, label in METRICS.items():
        chart_rows.append(
            {
                "Indicador": label,
                "Ronda": f"R{round_number}",
                "Porcentaje": 100 * round_data[column].mean(),
                "Casos": int(round_data[column].sum()),
                "Total": len(round_data),
            }
        )

chart_data = pd.DataFrame(chart_rows)

fig = px.bar(
    chart_data,
    x="Indicador",
    y="Porcentaje",
    color="Ronda",
    barmode="group",
    color_discrete_map={
        "R1": "#176B5B",
        "R2": "#34D399",
    },
    custom_data=["Casos", "Total"],
    text="Porcentaje",
    title=(
        "Mención, recomendación y cita oficial | "
        + " vs. ".join(
            f"R{number}" for number in sorted(generic["round"].unique())
        )
    ),
)

fig.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside",
    cliponaxis=False,
    hovertemplate=(
        "%{x}<br>"
        "%{fullData.name}: %{y:.1f}%<br>"
        "%{customdata[0]}/%{customdata[1]} observaciones"
        "<extra></extra>"
    )
)

fig.update_layout(
    yaxis_title="Porcentaje de respuestas",
    xaxis_title="",
    yaxis_range=[0, 110],
    legend_title_text="Ronda",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)

st.markdown("### Comparación visual")
st.plotly_chart(fig, width="stretch")

st.caption(
    f"Base de esta visualización: {len(generic)} observaciones seleccionadas. "
    "Las métricas no son mutuamente excluyentes."
)

# Segunda visualización: menciones espontáneas por motor.
engine_data = (
    generic.groupby(["engine", "round"])["coppel_mentioned"]
    .agg(["sum", "count"])
    .reset_index()
)

engine_data["Porcentaje"] = (
    100 * engine_data["sum"] / engine_data["count"]
)

engine_data["Ronda"] = engine_data["round"].map({
    1: "R1",
    2: "R2",
})

engine_data = engine_data.rename(columns={
    "engine": "Motor",
    "sum": "Menciones",
    "count": "Consultas",
})

engine_fig = px.bar(
    engine_data,
    x="Motor",
    y="Porcentaje",
    color="Ronda",
    barmode="group",
    category_orders={
        "Motor": ["ChatGPT", "Gemini", "Perplexity"],
        "Ronda": ["R1", "R2"],
    },
    color_discrete_map={
        "R1": "#176B5B",
        "R2": "#34D399",
    },
    custom_data=["Menciones", "Consultas"],
    text="Porcentaje",
    title=(
        "Mención espontánea de Coppel por motor"
        if selected_type == "generic"
        else "Mención de Coppel por motor"
    ),
)

engine_fig.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside",
    hovertemplate=(
        "%{x}<br>"
        "%{fullData.name}: %{y:.1f}%<br>"
        "%{customdata[0]}/%{customdata[1]} consultas"
        "<extra></extra>"
    ),
)

engine_fig.update_layout(
    yaxis_title="Porcentaje de consultas seleccionadas",
    xaxis_title="",
    yaxis_range=[0, 110],
    legend_title_text="Ronda",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)

st.markdown(
    "### Mención espontánea por motor"
    if selected_type == "generic"
    else "### Mención de Coppel por motor"
)
st.plotly_chart(engine_fig, width="stretch")

st.caption(
    "Resultados calculados sobre los motores y rondas seleccionados. "
    f"Tipo de consulta: {selected_type}. R3 pendiente."
)

# Tercera visualización: tres métricas por motor y ronda.
detail_rows = []

for (engine, round_number), subset in generic.groupby(
    ["engine", "round"]
):
    for column, label in METRICS.items():
        detail_rows.append(
            {
                "Motor": engine,
                "Ronda": f"R{round_number}",
                "Indicador": label,
                "Porcentaje": 100 * subset[column].mean(),
                "Casos": int(subset[column].sum()),
                "Total": len(subset),
            }
        )

detail_data = pd.DataFrame(detail_rows)

detail_fig = px.bar(
    detail_data,
    x="Indicador",
    y="Porcentaje",
    color="Ronda",
    facet_col="Motor",
    facet_col_wrap=min(3, detail_data["Motor"].nunique()),
    barmode="group",
    category_orders={
        "Motor": sorted(detail_data["Motor"].unique().tolist()),
        "Indicador": ["Mención", "Recomendación", "Cita oficial"],
        "Ronda": ["R1", "R2"],
    },
    color_discrete_map={
        "R1": "#176B5B",
        "R2": "#34D399",
    },
    custom_data=["Casos", "Total"],
    text="Porcentaje",
    title="Mención, recomendación y cita oficial por motor",
)

detail_fig.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside",
    cliponaxis=False,
    hovertemplate=(
        "%{x}<br>"
        "%{fullData.name}: %{y:.1f}%<br>"
        "%{customdata[0]}/%{customdata[1]} consultas"
        "<extra></extra>"
    )
)

detail_fig.update_yaxes(range=[0, 105])
detail_fig.update_xaxes(title_text="")

detail_fig.for_each_annotation(
    lambda annotation: annotation.update(
        text=annotation.text.split("=")[-1]
    )
)

detail_fig.update_layout(
    height=520,
    yaxis_title="Porcentaje de consultas seleccionadas",
    legend_title_text="Ronda",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)

st.markdown("### Mención, recomendación y cita oficial por motor")
st.plotly_chart(detail_fig, width="stretch")

st.caption(
    "Los denominadores corresponden a cada motor y ronda seleccionados. "
    "Los tres indicadores no deben sumarse entre sí."
)
