import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

#------ configuracion de variable mapa --------------

# !!!!IMPO aqui genero el principal mapa junto a las rayitas para argentina, ahora: "generar mapa" es la variable que carga el mapa.
def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m

# cargo el dataset
area = pd.read_csv("area_protegida.csv")


#------- los filtros sobre nuestro mapa --------------

#ubicacion del expander
with st.expander("1mapa:filtrar visualmente con un mapa todos las areas protegidas tipo parque(tap = 1)"):

    #el filtro
    filtr1 = area[area["tap"] == 1]

    # asigniar nueva variable con nuestra otra variable que almacena el mapa
mapa = generar_mapa()

    #  aca se marcan los parques en el mapa segun el filtro que se asigne
for _, fila in filtr1.iterrows():

        folium.Marker(
            location=[fila["lat"], fila["lng"]],
            radius=6,
            icon=folium.Icon(),
            fill_color="red",
            popup=fila["nam"]
        ).add_to(mapa)
        # esta sentencia al final adjunta el filtro a nuestra nueva avriable...
    # mostrar mapa en streamlit y terminar el expander con st_folium
    
st_folium(
        mapa,
        width=None,
        height=550
    )






#--------- otro filtro ---------

with st.expander("2mapa:filtrar y diferenciar por color todas las areas protegidas tipo area parque(tap = 1) y jurisdiccion provincial (jap = 3)"):

    filtr1 = area[area["tap"] == 1]

    filtr2 = area[area["jap"] == 3]
    # Crear mapa
    mapa2 = generar_mapa()

    # filtro por los subtipos de area protegida (filtr1 = tap 1 y filtr2 = jap 3)
for _, fila in filtr1.iterrows():

    folium.CircleMarker(
        location=[fila["lat"], fila["lng"]],
        radius=6,
        color="red",
        fill=True,
        fill_color="red",
        popup=fila["nam"]
    ).add_to(mapa2)

for _, fila in filtr2.iterrows():

    folium.CircleMarker(
        location=[fila["lat"], fila["lng"]],
        radius=6,
        color="blue",
        fill=True,
        fill_color="blue",
        popup=fila["nam"]
    ).add_to(mapa2)

st_folium(
        mapa2,
        width=None,
        height=550
    )