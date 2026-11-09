import streamlit as st

st.title("Parte 1")
st.header("Visitá los sitios propuestos y contanos")
st.image('images/taller.png')
with st.expander("¿Qué formatos encontraste?"):
    c1,c2 =st.columns(2)
    formatos_archivo = ['csv','ods', 'xls', 'shp', 'xml', 'geojson', 'json', 'pdf', 'kml','zip']
    formatos_abiertos = {formato: {'encontrado': False, 'abierto': False} for formato in formatos_archivo}        

    # Diccionario para almacenar si cada formato es abierto o no
    for formato in formatos_abiertos:
        formatos_abiertos[formato]['encontrado'] = c1.checkbox(formato)
        formatos_abiertos[formato] ['abierto']= c2.checkbox("¿Es abierto?", key=formato)

    mostrar = st.button('Mostrar')
    if mostrar:
        st.write("Estado de los formatos de archivo:")
        for formato in formatos_abiertos:
            if formatos_abiertos[formato]['encontrado']:
                st.write(f"{formato}: {'Abierto' if formatos_abiertos[formato]['abierto'] else 'Cerrado'}")

