import streamlit as st

from funciones import insertUser

st.session_state["Usuario encontrado"] = False
st.title("Ingreso de usuario")
dni = st.text_input("DNI")
nombre = st.text_input("Nombre y apellido")
cumpleaños = st.text_input("Fecha de nacimiento (dd/mm/aaaa)")
zona = st.selectbox("Zona de trabajo: Norte/Sur/Oeste/CABA", ("N", "O", "S", "C"))

if st.button("Guardar"):
    if not dni or not nombre or not cumpleaños or not zona:
        st.error("Por favor completa todos los campos")
    else:
        insertUser(dni, nombre, cumpleaños, zona)
