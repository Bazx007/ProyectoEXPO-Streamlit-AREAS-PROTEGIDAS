import streamlit as st



import base64

# 1. ACÁ DEFINIMOS LA FUNCIÓN (Dejala tal cual está, no cambies nada aquí)
def mostrar_png_nitido(ruta_imagen, max_width_porcentaje=30):
    with open(ruta_imagen, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    
    html_code = f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{encoded}" 
             style="max-width: {max_width_porcentaje}%; height: auto;">
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)


# 2. ACÁ USAMOS LA FUNCIÓN (Aquí es donde pasamos los datos reales)
# Notá cómo agregamos "images/" adelante para que entre a tu carpeta

st.markdown(
    "<h2 style='text-align: center;'>Aanálisis de Datos en la Facultad de Informática</h2>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h1 style='text-align: center;'>Áreas protegidas de la Argentina</h1>",
    unsafe_allow_html=True,
)




st.markdown(
    "<p style='text-align: center;'>Con Python🐍</p>",
    unsafe_allow_html=True,
)


mostrar_png_nitido("images/mapa-reservas-inicio.png", max_width_porcentaje=30)

st.title("")


st.markdown(
    "<h2 style='text-align: center;'>¿De que trata?</h2>",
    unsafe_allow_html=True,
)

st.write("En esta página web se conocen datos sobre las áreas protegidas de Argentina: su distribución geográfica, tamaño, tipo y jurisdicción.")

st.write(  "**¿Qué es un área protegida?**")
st.write( " Las áreas protegidas son espacios geográficos destinados a conservar la naturaleza, los ecosistemas, la biodiversidad y otros elementos de valor ambiental, científico o cultural.  ",
        "legalmente regulado con el fin de preservar a largo plazo el patrimonio cultural o un ecosistema. ")

st.write( "Se utilizaran fuentes como el Instituto Geográfico Nacional (IGN), el uso de estos datos facilita conocer dónde se encuentran las áreas protegidas, cómo se clasifican y qué organismos tienen jurisdicción sobre ellas.")


st.subheader("Nuestros Datos")
st.write("Para entender en base las capacidades de nuestra aplicación, primero me gustaría brindarles el correspondiente conocimiento vinculado al contenido de nuestra app, como funciona y que nos aporta en la creación de aplicaciones web interactivas.")

st.write("Esta aplicacion streamlit divide la informacion en diferentes paginas, cada una conteniendo los diferentes fundamentos que nos permitiran no solo conocer las areas protegidas encontradas en la Argentina geograficamente; Si no tambien nuestro entorno (dataset) y el proceso de gestion de los datos.  ")












st.markdown(
    "<h2 style='text-align: center;'>eligue uno de los siguientes temas</h2>",
    unsafe_allow_html=True,
)

# Cada tarjeta contiene los datos de una página.
secciones = [
    {
        "titulo": "📋 Conocimiento de datos",
        "descripcion": (
            "Conocé el conjunto de datos, sus columnas "
            "y el significado de la información que utilizaremos."
        ),
        "pagina": "pages/01_✅Conociendo basico de nuestro dataset.py",
        "boton": "Conocer los datos",
    },
    {
        "titulo": "📊 Utilizar gráficos",
        "descripcion": (
            "Explorá gráficos que permiten comparar categorías "
            "y comprender la distribución de los datos."
        ),
        "pagina": "pages/02_✅Utilizamos graficos para areas protegidas.py",
        "boton": "Explorar gráficos",
    },
    {
        "titulo": "🗺️ Utilizar mapas",
        "descripcion": (
            "Ubicá las áreas protegidas y explorá su distribución "
            "geográfica mediante mapas interactivos."
        ),
        "pagina": "pages/03_✅INTERACTIVO LA - Mostramos en mapas copy.py",
        "boton": "Explorar mapas",
    },
]

# Una columna para cada tarjeta.
columnas = st.columns(3)

for i, seccion in enumerate(secciones):
    with columnas[i]:
        with st.container(border=True):
            st.subheader(seccion["titulo"])
            st.write(seccion["descripcion"])

            if st.button(
                seccion["boton"],
                key=f"ir_seccion_{i}",
                use_container_width=True,
            ):
                st.switch_page(seccion["pagina"])