import streamlit as st


def render_filters(data):
    """Renderiza filtros y devuelve los registros seleccionados."""

    st.sidebar.header("Explorar resultados")

    engines = sorted(data["engine"].unique().tolist())

    selected_engines = st.sidebar.multiselect(
        "Motores generativos",
        options=engines,
        default=engines,
    )

    selected_rounds = st.sidebar.multiselect(
        "Rondas",
        options=[1, 2],
        default=[1, 2],
        format_func=lambda value: f"R{value}",
    )

    selected_type = st.sidebar.selectbox(
        "Tipo de consulta",
        options=["generic", "brand", "all"],
        format_func=lambda value: {
            "generic": "Genéricas",
            "brand": "De marca",
            "all": "Todas",
        }[value],
    )

    filtered = data.loc[
        data["engine"].isin(selected_engines)
        & data["round"].isin(selected_rounds)
    ].copy()

    if selected_type != "all":
        filtered = filtered.loc[
            filtered["query_type"] == selected_type
        ].copy()

    return filtered, selected_type
