import streamlit as st
from funciones import insertEmpresa
import time 
from streamlit_extras.switch_page_button import switch_page

st.session_state["Empresa encontrado"] = False
st.markdown(
    """
    <h1 style="font-family: 'Roboto', sans-serif; color: #494666;">
        Registrar Empresa
    </h1>
    """,
    unsafe_allow_html=True
)
id_empresa = st.text_input("CUIT")
nombre = st.text_input("Nombre")
zona = st.selectbox("Zona de la empresa: Norte/Sur/Oeste/CABA", ("N", "O", "S", "C"))
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e0f7ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Guardar"):
    if not id_empresa or not nombre or not zona:
        st.error("Por favor completa todos los campos")
    else:
        insertEmpresa(id_empresa, nombre, zona)
        with st.spinner('Cargando...'):
            time.sleep(4)  # Espera de 2 segundos
        switch_page("Puestos disponibles")

