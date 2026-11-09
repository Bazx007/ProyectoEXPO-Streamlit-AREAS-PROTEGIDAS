import streamlit as st
import pandas as pd
import plotly.express as px


areas = pd.read_csv('area_protegida.csv')
st.title("Gráfico")

  
filtr3 = areas["tap"].value_counts()
fig = px.bar(
    data_frame = filtr3, x = filtr3.index, y = filtr3.values, title = "grafico con la frecuencia de los subtipo jurisdccion")
with st.expander("1.Gráfico: crear un grafico potly bar que identifique todos los tipos jurisdiccion (tap) ¿cual es el tipo de area de jurisdiccion mas frecuente?"):
# Mostrar el gráfico
  st.plotly_chart(fig)  

filtr2 = areas[areas["lng"] > -63]
filtr3 = filtr2["tap"]
pig = px.pie(
    data_frame = filtr3, values = filtr3.index, names = filtr3.values, title = "grafico de jurisdicciones tap mayores al promedio")
with st.expander("2.grafico: ¿Cuál es el tipo de área protegida (tap) mayor a la longitud (lng) promedio mas frecuente?"):

  st.plotly_chart(pig) 

filtr1 = areas[(areas["tap"] == 1)&(areas.jap == 2)]
filtr2 = filtr1[filtr1["lat"] > -34]
filtr4 = filtr2.sort_values("lat")
filtr3 = filtr4["nam"]
dig = px.bar(
    y=filtr3.values,
    x=filtr4["lat"],
    orientation="h",
    title="Parques nacionales al norte de la latitud media")
with st.expander('3.grafico: utilizando potly line; queremos generar un grafico que muestre todas las areas protegidas; parques nacionales ("tap 1" y "jap 2") ubicadas al norte ¿cual es el parque nacional con mas latitud?'):

   st.plotly_chart(dig)