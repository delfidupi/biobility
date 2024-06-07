import streamlit as st
import time 
from streamlit_extras.switch_page_button import switch_page

from funciones import insertUser

st.session_state["Usuario encontrado"] = False
st.title("Ingreso de usuario")
dni = st.text_input("DNI")
nombre = st.text_input("Nombre y apellido")
cumpleaños = st.text_input("Fecha de nacimiento (dd/mm/aaaa)")
zona = st.selectbox("Zona de trabajo: Norte/Sur/Oeste/CABA", ("N", "O", "S", "C"))

# Definir el estado de guardado
if 'saved' not in st.session_state:
    st.session_state.saved = False

if st.button("Guardar"):
    if not dni or not nombre or not cumpleaños or not zona:
        st.error("Por favor completa todos los campos")
    else:
        insertUser(dni, nombre, cumpleaños, zona)
        st.session_state.saved = True
        st.success("Datos guardados correctamente")

# Mostrar el botón "Crear un curriculum" solo si los datos han sido guardados
if st.session_state.saved:
    if st.button("Crear un curriculum"):
        with st.spinner('Cargando...'):
            time.sleep(2)  # Espera de 2 segundos
        switch_page("Profesional Usuario")



        


