import pandas as pd
import streamlit as st



areas =  pd.read_csv('area_protegida.csv')


st.title("Áreas Protegidas de Argentina")

tab_coding, tab_datos, tap_preguntas = st.tabs([
    "codeando y testeando",
    "Datos",
    "preguntas"
    
])


with tab_coding:


# texto
    st.title("conocimiento basico de nuestro dataset")
    st.subheader("¿Cuáles son los códigos de verificación en nuestro mapa y de dónde los encontramos?")
    st.write("Saber cuáles son los diferentes tipos de áreas protegidas que podemos contener dentro de nuestro entorno es un conocimiento fundamental que nos permite comprender en qué condiciones se manejan (si son tipos de áreas o jurisdicciones) y muestran nuestros puntos de intereses (áreas protegidas) en el mapa.")
    st.title("Parte 1")
    st.header("Conocemos nuestro dataset")
    
    
    #expander con codigo y print
    with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
     filas, columnas = areas.shape
     filas, columnas = areas.shape
     st.write(f'Tiene { filas} filas y {columnas} columnas')


    
    
    with st.expander("¿cuales son los tipos de areas de jurisdiccion mas abundantes?"):
      filtr2 = areas["jap"].value_counts()
      st.write(filtr2)
      with st.expander("¿Cuáles son los tipos de categorías de nuestras areas y para que funcionan?"):
          st.markdown("""
                    **categorias y sus clasificaciones:**

    **Tipo de área (`tap`):**

    - **0:** Información no disponible.
    - **1:** Parque.
    - **2:** Reserva.
    - **3:** Monumento Nacional.

    **Jurisdicción (`jap`):**

    - **-1 o 0:** Información no disponible.
    - **2:** Nacional.
    - **3:** Provincial.
    - **4:** Municipal.
    - **5:** Privado.
    """)
          st.write("Nuestro dataset utilizara códigos numéricos para la identificación de las diversas categorías de tipos de áreas protegidas. Estos números permiten organizar, filtrar y representar los registros dentro de la aplicación.")


       
    

    
    st.title("parte 2")
    st.header("Las latitudes y longitudes de nuestro mapa, y que información podemos gestionar a través de ellas")
    st.markdown("""
        **Deberías conocer muy bien que son las latitudes y longitudes:**
    
        - **Latitud:** calcula el hemisferio norte y el hemisferio sur.
        - **longitud:** calcula el hemisferio oeste y el hemisferio este.
        """)
    st.write("Bien, no va más lejos de cómo nos manejamos normalmente a la hora de querer ubicarnos en un “lugar fijo” o definir una zona en la que queramos investigar.")

    with st.expander("entonces; ¿cual es el valor maximo total de las longitudes y latitudes?"):
     filtr1 = areas["lat"].max()
     filtr2 = areas["lng"].max()
     st.write(filtr1, filtr2)
     
 

    st.write("utilizaremos “value_counts()” que pertenece a las funciones cálculos de pandas.")
    st.write("Esto nos permitirá saber cuántas veces aparece cada valor único en una columna o DataFrame (contará cuantas veces se repite jap en nuestro dataframe).")
    st.write("entonces; de todas las areas de jurisdiccion jap, ¿cual es su subtipo mas frecuente? ")
    with st.expander("¿Cuál es el Parques Nacional ubicado más hacia el sur? (tap == 1 y jap == 2)? ¿Y de las Reservas Provinciales (tap == 2 y jap == 3)?"):
        a = areas["lat"].min()
        filtr = areas[(areas["tap"] == 1)&(areas.jap == 2)]
        c = filtr[filtr["lat"] > -56.6900008745]
        d = c["nam"]
        st.write(d.max())

        filtr = areas[(areas["tap"] == 2)&(areas.jap == 3)]
        c = filtr[filtr["lat"] > -56.6900008745]
        d = c["nam"]
        st.write(d.max())



    st.subheader("Fijamos un punto promedio")
    st.write("Si quiero saber cuáles son todas las áreas nacionales ubicadas hacia el sur, lo primero sería establecer o conocer cual es justo el punto promedio de nuestro mapa de Argentina, que en este caso es -35")
    with st.expander("buscamos todas las areas nacionales (tap == 2) que sean menores a la latitud -35"):
         filtr = areas[areas["tap"] == 2]
         filtr2W = filtr["lat"].mean()
         
         filtr1 = areas[areas["lat"] < -35]
         filtr2 = filtr1[filtr1["tap"] == 2]
         st.write(filtr2W)
         st.write(filtr2.value_counts())

    st.subheader("Existen más “códigos” de verificación")
    st.write("Ya supimos filtrar según nuestros códigos de filtración jap y tap. Pero también podemos buscar nuestras areas por otros datos, por ejemplo; Gid")
    st.markdown("""      
                 - **gid:** es un identificador de grupo numérico único, permaneciente a cada área protegida dentro de nuestro panel(dataset). calcula el hemisferio norte y el hemisferio sur.
                 """)
    with st.expander("¿cual es la area protegida cuyo codigo gid es 262?"):
         filtr1 = areas[areas["gid"] == 262]
         filtr2 = filtr1["nam"]
         st.write(filtr2)

    pass

with tab_datos:
    st.subheader("Datos de las áreas protegidas")

    st.write(f"Cantidad de registros: {len(areas)}")

    st.dataframe(
        areas[["lat","lng","gid", "entidad", "objeto", "fna", "gna", "nam","tap","jap", "caa", "fdc", "sag", "area"]]
    )

with tap_preguntas:



 st.set_page_config(page_title="Juego de Preguntas", page_icon="🎮")
 st.title("🎮 Juego de Preguntas")

# ============================================================
# Definimos las preguntas
# ============================================================
 preguntas = [
    {
        "pregunta": "¿que clase de jurisdiccion es la area Delta del Parana?",
        "opciones": ["Nacional", "Provincial", "Municipal"],
        "correcta": 0
    },
    {
        "pregunta": "que tipo de area y jurisdiccion contiene La Calera ",
        "opciones": ["parque municipal", "reserva nacional", "monumento provincial"],
        "correcta": 1
    },
    {
        "pregunta": "a cual area le pertenece el gid; 213 ",
        "opciones": ["Perito Moreno", "Sierras de Belén", "Arroyo Los Gauchos"],
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