import streamlit as st
import time 
from streamlit_extras.switch_page_button import switch_page
from datetime import datetime


from funciones import insertUser

st.session_state["Usuario encontrado"] = False
st.markdown(
    """
    <h1 style="font-family: 'Roboto', sans-serif; color: #494666;">
        Ingreso de usuario
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e0f7ff;
        position: relative;
    }
    .logo-container {
        position: absolute;
        top: 10px;
        right: 10px;
    }
    .logo-img {
        width: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="logo-container">
        <img src="https://github.com/delfidupi/biobility/blob/main/logo.jpg?raw=true">
    </div>
    """,
    unsafe_allow_html=True
)
# Campos de entrada
dni = st.text_input("DNI")
nombre = st.text_input("Nombre y apellido")
cumpleaños = st.date_input("Fecha de nacimiento", value=datetime(2000, 1, 1), min_value=datetime(1900, 1, 1), max_value=datetime.today())
zona = st.selectbox("Zona de trabajo: Norte/Sur/Oeste/CABA", ("N", "O", "S", "C"))

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
    if not dni or not nombre or not cumpleaños or not zona:
        st.error("Por favor completa todos los campos")
    else:
        insertUser(dni, nombre, cumpleaños, zona)
        with st.spinner('Cargando...'):
            time.sleep(4)  # Espera de 2 segundos
        switch_page("Profesional Usuario")




        


