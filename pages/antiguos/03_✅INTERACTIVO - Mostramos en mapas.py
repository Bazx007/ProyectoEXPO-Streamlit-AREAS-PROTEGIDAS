import folium
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import html

# -----------------------------------
# carga del dataset
# -----------------------------------

area = pd.read_csv("area_protegida.csv")

# Convertir columnas a valores numericos
for columna in ["lat", "lng", "tap", "jap"]:
    area[columna] = pd.to_numeric(
        area[columna], errors="coerce"
    )

# Eliminar registros sin coordenadas validas
area = area.dropna(subset=["lat", "lng"])

area = area[
    area["lat"].between(-90, 90) &
    area["lng"].between(-180, 180)
]



# para generar el mapa

def generar_mapa():

    tiles = (
        "https://wms.ign.gob.ar/geoserver/gwc/service/tms/"
        "1.0.0/capabaseargenmap@EPSG%3A3857@png/"
        "{z}/{x}/{-y}.png"
    )

    attr = "Instituto Geografico Nacional (IGN)"

    mapa = folium.Map(
        location=[-33.457606, -65.346857],
        control_scale=True,
        zoom_start=5,
        tiles=tiles,
        attr=attr,
        tms=True
    )

    return mapa



# diccionario para las categorias
# -----------------------------------

tipos = {
    "Información no disponible": 0,
    "Parque": 1,
    "Reserva": 2,
    "Monumento Nacional": 3
}

jurisdicciones = {
    "Información no disponible": [-1, 0],
    "Nacional": [2],
    "Provincial": [3],
    "Municipal": [4],
    "Privado": [5]
}

colores_tap = {
    0: "gray",
    1: "red",
    2: "green",
    3: "blue"
}





# -----------------------------------
# 4. para los marcadores
# -----------------------------------

def agregar_marcador(fila):

    nombre = str(fila["nam"])

    # Obtener el color segun el tipo de area
    color = colores_tap.get(fila["tap"], "gray")

    # Nombres de las categorias
    nombres_tap = {
        0: "Información no disponible",
        1: "Parque",
        2: "Reserva",
        3: "Monumento Nacional"
    }

    nombres_jap = {
        -1: "Información no disponible",
        0: "Información no disponible",
        2: "Nacional",
        3: "Provincial",
        4: "Municipal",
        5: "Privado"
    }

    tipo = nombres_tap.get(
        fila["tap"], "Desconocido"
    )

    jurisdiccion = nombres_jap.get(
        fila["jap"], "Desconocido"
    )

    # Crear ventana informativa
    popup = folium.Popup(
        f"""
        <b>{html.escape(nombre)}</b>
        <p>Tipo: {tipo}</p>
        <p>Jurisdicción: {jurisdiccion}</p>
        """,
        max_width=250
    )

    # Crear marcador con color dinamico
    folium.CircleMarker(
        location=[fila["lat"], fila["lng"]],
        radius=6,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.8,
        tooltip=nombre,
        popup=popup
    ).add_to(mapa)



# -----------------------------------
# para la interfaz
# -----------------------------------

st.title("Identificacion de las areas protegidas de Argentina")

with st.expander("Exploremos nuestras diferentes áreas protegidas", expanded=True):

    mapa = generar_mapa()

    ac1, ac2 = st.columns([0.3, 0.7])

    with ac1:

        st.subheader("Tipo de área")

        tap_seleccionados = []

        for nombre, codigo in tipos.items():

            if st.checkbox(nombre, key=f"tap_{codigo}"):
                tap_seleccionados.append(codigo)

        st.divider()

        st.subheader("Jurisdicción")

        jap_seleccionados = []

        for nombre, codigos in jurisdicciones.items():

            if st.checkbox(nombre, key=f"jap_{nombre}"):
                jap_seleccionados.extend(codigos)


    # combinar el filtrado
    # -----------------------------------

    filtrado = area.copy()

    if tap_seleccionados:
        filtrado = filtrado[
            filtrado["tap"].isin(tap_seleccionados)
        ]

    if jap_seleccionados:
        filtrado = filtrado[
            filtrado["jap"].isin(jap_seleccionados)
        ]


    # para los puntos
    # -----------------------------------

    filtrado.apply(agregar_marcador, axis=1)


    # aqui se muestra el mapa
    # -----------------------------------

with ac2:

    st.write(
        f"Áreas encontradas: {len(filtrado)}"
    )

    st_folium(
        mapa,
        width=None,
        height=550,
        key="mapa_areas"
    )

    # Leyenda de colores
    st.markdown("**Referencias del mapa:**")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("🔴 Parque")
        st.markdown("🟢 Reserva")

    with col2:
        st.markdown("🔵 Monumento Nacional")
        st.markdown("⚪ Información no disponible")
