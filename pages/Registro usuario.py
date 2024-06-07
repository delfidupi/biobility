import streamlit as st
import time 
from streamlit_extras.switch_page_button import switch_page
from datetime import datetime


from funciones import insertUser

st.session_state["Usuario encontrado"] = False
st.title("Ingreso de usuario")
dni = st.text_input("DNI")
nombre = st.text_input("Nombre y apellido")
cumpleaños = st.date_input("Fecha de nacimiento", value=datetime(2000, 1, 1), min_value=datetime(1900, 1, 1), max_value=datetime.today())
zona = st.selectbox("Zona de trabajo: Norte/Sur/Oeste/CABA", ("N", "O", "S", "C"))


if st.button("Guardar"):
    if not dni or not nombre or not cumpleaños or not zona:
        st.error("Por favor completa todos los campos")
    else:
        insertUser(dni, nombre, cumpleaños, zona)
        with st.spinner('Cargando...'):
            time.sleep(4)  # Espera de 2 segundos
        switch_page("Profesional Usuario")




        


