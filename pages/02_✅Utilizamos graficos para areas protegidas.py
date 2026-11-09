import streamlit as st
import pandas as pd
import plotly.express as px


areas = pd.read_csv('area_protegida.csv')



st.title("Áreas Protegidas de Argentina")

tab_coding, tab_datos, tap_preguntas = st.tabs([
    "codeando y testeando",
    "Datos",
    "preguntas"
    
])


with tab_coding:

   #titulo
     st.title("Comencemos a utilizar gráficos")
     st.write("Gracias a plotly, seremos capaces por medio de las herramientas que nos otorga, visualizar en forma de gráficos/esquemas toda la información como datos y cálculos analíticos que queramos representar de nuestras áreas protegidas.")
     st.subheader("¿De qué manera podemos visualizar los gráficos?")
     st.write("Plotly trae consigo diferentes “herramientas” cada una de ella visualizando nuestros gráficos de diferente forma según lo necesitemos.")
     st.markdown("""      
                   - **en forma de barra:** (plotly bar).
                   - **en forma de torta:** (plotly pie).
                   - **en forma de linea:** (plotly line).
                   - **en forma de dispersion:** (plotly scatter).
                   """)

     st.title("parte 1")
     st.subheader("Utilicemos plotly bar")


#graficos p1  
     st.write("Si queremos identificar de manera visual una comparacion entre datos, en este caso entre las categorias que diferencian nuestras areas, plotly podria ser una buena opcion.")
     filtr3 = areas["tap"].value_counts()
     fig = px.bar(
     data_frame = filtr3, x = filtr3.index, y = filtr3.values, title = "grafico con la frecuencia de los subtipo jurisdccion")

     with st.expander("creemos un grafico plotly bar con todos los tipos jurisdiccion (tap) y identifiquemos: ¿cual es el tipo de area de jurisdiccion mas frecuente?"):
# Mostrar el gráfico
      st.plotly_chart(fig)  
      st.write("Como se puede observar, las barras que se asoman de manera vertical representan un porcentaje, en este caso la frecuencia en la que aparecen las areas de categoria jurisdiccion en nuestro mapa.")
      st.write("resolviendo el caso, siendo la jurisdiccion de tipo nacional (tap =2) la mas frecuente.")


    #graficos p2
     st.title("parte 2")
     st.subheader("utilizemos plotly pie")
     st.write("Si queremos ahora, saber y comparar por ejemplo: la frecuencia de todos los subtipos de nuestras áreas protegidas, podemos usar un gráfico torta “plotly pie” que muestra los datos por porcentaje")
     st.write("Ya que lo que queremos es “comparar” lo ideal sería buscar un gráfico plotly que nos permita visualizar dicha comparación entre los subtipos de nuestras áreas, plotly pie puede ser una buena elección ya que puede mostrar una comparativa entre los subtipos mediante colores y porcentajes.")

     filtr2 = areas[areas["lng"] > -63]
     filtr3 = filtr2["tap"]
     pig = px.pie(
     data_frame = filtr3, values = filtr3.index, names = filtr3.values, title = "grafico de jurisdicciones tap mayores al promedio")
     with st.expander("Con plotly pie identifiquemos¿Cuál es el tipo de área protegida (tap) mayor a la longitud (lng) promedio mas frecuente?"):
         st.plotly_chart(pig) 
         st.write("Como se puede ver en el gráfico, aparece cada subtipo asignado por un color y porcentaje, que determina que tantas veces aparecen ubicados hacia el este están.  En esta ocasión, el subtipo por tipo de área, mas frecuente es de “reservas” (tap 2)")


#graficos p3
     st.title("parte 3")
     st.subheader("Tomemos dos categorias de areas protegidas y hagamos un grafico plotly bar")

     st.write("Si queremos ver un gráfico tomando dos categorias de tipo parques nacionales (''tap 1'' y ''jap 2'') ubicados hacia el norte, para comparar y saber cuál de todos está más alejado hacia el norte según latitud, podemos usar un procedimiento parecido al ejemplo anterior, pero para variar, esta vez utilicemos plotly line.")

     st.markdown(
     "<p style='text-align: center;'>Para obtener el resultado, primero se establecio el promedio entre las latitudes; -34</p>",
     unsafe_allow_html=True,
     )

     filtr1 = areas[(areas["tap"] == 1)&(areas.jap == 2)]
     filtr2 = filtr1[filtr1["lat"] > -34]
     filtr4 = filtr2.sort_values("lat")
     filtr3 = filtr4["nam"]
     dig = px.line(
     y=filtr3.values,
     x=filtr4["lat"],
     orientation="h",
     title="Parques nacionales al norte de la latitud media")
     with st.expander('utilizando plotly line y ubicandonos al norte, generemos un grafico que muestre todas las areas protegidas tipo parques nacionales ("tap 1" y "jap 2") y identifiquemos:¿cual es el parque nacional mas lejano?'):

         st.plotly_chart(dig)
         st.write("Y estableciendo que buscaremos exactamente los parques nacionales, también hay que tener en cuenta que queremos los nombres de dichas áreas protegidas utilizando la columna con los nombres correspondientes de nuestro dataset (nam).")



with tab_datos:
    st.subheader("Datos de las áreas protegidas")

    st.write(f"Cantidad de registros: {len(areas)}")

    st.dataframe(
        areas[["lat","lng","gid", "entidad", "objeto", "fna", "gna", "nam","tap","jap", "caa", "fdc", "sag", "area"]]
    )
 


# ============================================================
# Definimos las preguntas
# ============================================================
with tap_preguntas:

 st.set_page_config(page_title="Juego de Preguntas", page_icon="🎮")


# ============================================================
# Definimos las preguntas
# ============================================================
 with st.expander("GRAFICOS TIPO TORTA (PLOTLY PIE)"):
  preguntas = [
    {
        "pregunta": "¿En que forma los graficos Plotly pie muestran y comparan la informacion?",
        "opciones": ["solo con colores", "solo con porcentajes", "todas las anteriores"],
        "correcta": 2
    },
    {
        "pregunta": "Si con plotly queremos mostrar la frecuencia de datos entre las areas de categoria jurisdiccion (jap); que resultado saldra",
        "opciones": ["comparacion entre la cantidad de todos los tipos de jurisdiccion existentes", "todas las areas protegidas de tipo jurisdiccion en argentina", "comparacion numerica entre categoria jurisdiccion y categoria tipo de areas"],
        "correcta": 0
    },
    {
        "pregunta": "porque no conviene hacer un grafico comparando los datos de los nombres de las areas protegidas (columna 'nam') ",
        "opciones": ["Por la falta de comparacion en la redundancia de datos", "porque los nombres no representan una clasificacion numerica", "no se"],
        "correcta": 1
    },

    
]


# ============================================================
# Una pregunta por bloque, con su propio botón de verificar
# ============================================================
  for i, p in enumerate(preguntas):
     st.subheader(f"Pregunta {i + 1}")
     st.write(p["pregunta"])

    # El radio guarda la elección del estudiante
     eleccion = st.radio(
        "Elegí una opción:",
        p["opciones"],
        key=f"pregunta_{i}",
        index=None,
    )

    # Cada pregunta tiene su propio botón
     if st.button("Verificar", key=f"btn_{i}"):
        if eleccion is None:
            st.warning("⚠️ Elegí una opción antes de verificar.")
        elif eleccion == p["opciones"][p["correcta"]]:
            st.balloons()
            st.success("✅ ¡Correcto!")
        else:
            correcta = p["opciones"][p["correcta"]]
            st.error(f"❌ Incorrecto. La respuesta correcta era: **{correcta}**")

     st.divider()





 with st.expander("GRÁFICOS DE BARRAS"):

        preguntas_barras = [
            {
                "pregunta": "¿Qué permite comparar un gráfico de barras?",
                "opciones": [
                    "Valores entre categorías",
                    "Únicamente ubicaciones geográficas",
                    "Solo textos",
                ],
                "correcta": 0,
            },
            {
                "pregunta": "¿Qué representa la altura de cada barra?",
                "opciones": [
                    "que se esta calculando y comparando valores numerico",
                    "el valor o frecuencia de la categoría",
                    "la cantidad de valores de texto que la categoria trae consigo",
                ],
                "correcta": 1,
            },
            {
                "pregunta": "utilizando las barras; ¿si queremos comparar con que frecuencia aparecen todos los tipos de jurisdiccion ubicados al oeste ¿de que nos debemos asegurar primero?",
                "opciones": [
                    "saber cual de las barras es menor que las demas",
                    "asegurarnos que areas tiene un mayor valor numerico en negativo para asi compararlas",
                    "buscar las areas segun la mitad de las longitudes en el mapa para definir el oeste",
                ],
                "correcta": 2,
            },
            
        ]

        for i, p in enumerate(preguntas_barras):
            st.subheader(f"Pregunta {i + 1}")
            st.write(p["pregunta"])

            eleccion = st.radio(
                "Elegí una opción:",
                p["opciones"],
                key=f"barras_pregunta_{i}",
                index=None,
            )

            if st.button("Verificar", key=f"barras_btn_{i}"):
                if eleccion is None:
                    st.warning("⚠️ Elegí una opción antes de verificar.")
                elif eleccion == p["opciones"][p["correcta"]]:
                    st.balloons()
                    st.success("✅ ¡Correcto!")
                else:
                    correcta = p["opciones"][p["correcta"]]
                    st.error(
                        f"❌ Incorrecto. La respuesta correcta era: **{correcta}**"
                    )

            st.divider()
















