import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd

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


lagos = pd.read_csv('lagos_arg.csv')
st.title("Mapa")
mapa = generar_mapa()

def agregar_marca_aerop(row):
    
    #st.write(color)
    folium.Marker(
        [row['lat'], row['lng']],
        popup=row['Nombre'],
        icon=folium.Icon()
        ).add_to(mapa)

ac1,ac2 = st.columns([0.3, 0.7])
r_areas = ac1.checkbox("Grandes")
if r_areas:
    a_larg = lagos[lagos['Sup Tamaño']=='grande']
    a_larg.apply(agregar_marca_aerop, axis=1)
r_parques = ac1.checkbox("Medianos")
if r_parques:
    a_med = lagos[lagos['Sup Tamaño']=='medio']
    a_med.apply(agregar_marca_aerop, axis=1)
r_monu = ac1.checkbox("Pequeños")
if r_monu:
    a_small = lagos[lagos['Sup Tamaño']=='chico']
    a_small.apply(agregar_marca_aerop, axis=1)
with ac2:
    st_folium(mapa, key='lagos')
