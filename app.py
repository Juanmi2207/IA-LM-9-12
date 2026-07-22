import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Análisis Gráfico", layout="wide")

st.title("📊 Análisis Gráfico de Datos")
st.write(
    "Sube un archivo CSV o Excel y explora tus datos con distintos "
    "tipos de gráficos."
)

# --- 1. Cargar archivo ---
archivo = st.file_uploader("Sube tu archivo (.csv o .xlsx)", type=["csv", "xlsx"])

if archivo is not None:
    if archivo.name.endswith(".csv"):
        df = pd.read_csv(archivo)
    else:
        df = pd.read_excel(archivo)

    st.success(f"Archivo cargado: {archivo.name} ({df.shape[0]} filas, {df.shape[1]} columnas)")

    with st.expander("Ver datos crudos"):
        st.dataframe(df, use_container_width=True)

    with st.expander("Estadísticas descriptivas"):
        st.dataframe(df.describe(include="all"), use_container_width=True)

    columnas = df.columns.tolist()
    columnas_numericas = df.select_dtypes(include=np.number).columns.tolist()

    st.divider()
    st.subheader("Configura tu gráfico")

    col1, col2, col3 = st.columns(3)

    with col1:
        tipo_grafico = st.selectbox(
            "Tipo de gráfico",
            ["Barras", "Líneas", "Dispersión (scatter)", "Histograma", "Caja (box)", "Correlación (heatmap)"],
        )

    with col2:
        eje_x = st.selectbox("Eje X", columnas)

    with col3:
        # El eje Y no aplica para histograma ni heatmap
        if tipo_grafico in ["Histograma", "Correlación (heatmap)"]:
            eje_y = None
        else:
            eje_y = st.selectbox("Eje Y", columnas_numericas if columnas_numericas else columnas)

    color_por = st.selectbox("Colorear por (opcional)", ["Ninguno"] + columnas)
    color_por = None if color_por == "Ninguno" else color_por

    st.divider()

    # --- 2. Generar el gráfico según el tipo elegido ---
    try:
        if tipo_grafico == "Barras":
            fig = px.bar(df, x=eje_x, y=eje_y, color=color_por)

        elif tipo_grafico == "Líneas":
            fig = px.line(df, x=eje_x, y=eje_y, color=color_por)

        elif tipo_grafico == "Dispersión (scatter)":
            fig = px.scatter(df, x=eje_x, y=eje_y, color=color_por)

        elif tipo_grafico == "Histograma":
            fig = px.histogram(df, x=eje_x, color=color_por)

        elif tipo_grafico == "Caja (box)":
            fig = px.box(df, x=eje_x, y=eje_y, color=color_por)

        elif tipo_grafico == "Correlación (heatmap)":
            if len(columnas_numericas) < 2:
                st.warning("Se necesitan al menos 2 columnas numéricas para el heatmap de correlación.")
                fig = None
            else:
                corr = df[columnas_numericas].corr()
                fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale="RdBu_r")

        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"No se pudo generar el gráfico: {e}")

else:
    st.info("Esperando que subas un archivo para comenzar el análisis.")
