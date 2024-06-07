import streamlit as st
from funciones import insertCurriculum, dni_exists
import time
from streamlit_extras.switch_page_button import switch_page

# Estado inicial de la sesión
if "Usuario_encontrado" not in st.session_state:
    st.session_state["Usuario_encontrado"] = False

if 'saved' not in st.session_state:
    st.session_state.saved = False

st.title("Ingreso de usuario")
dni = st.text_input("DNI")

# Mostrar botón "Buscar" inicialmente
if st.button('Buscar'):
    if dni_exists(dni):
        st.session_state["Usuario_encontrado"] = True
        st.session_state["dni"] = dni
    else:
        st.error("Usuario no encontrado")
        st.session_state["Usuario_encontrado"] = False

# Mostrar formulario de datos profesionales si el usuario es encontrado
if st.session_state["Usuario_encontrado"]:
    st.subheader('Carga tus datos profesionales')
    especialidad = st.selectbox("Especialidad: Bioinformatica (B), Protesis (P), Genética (G), Imagenes biomedicas (I)", ("B", "P", "G", "I"))
    turno = st.selectbox("Turno: Mañana (M), Tarde (T), Noche (N)", ("M", "T", "N"))
    presencialidad = st.selectbox("Presencialidad", ("Si", "No"))
    estudios = st.text_input("¿Donde te recibiste?")
    experienciaLaboral = st.selectbox("¿Tenes experiencia laboral?", ("Si", "No"))
    
    # Mostrar botón "Guardar" después de completar los datos
    if st.button("Guardar"):
        if not dni or not especialidad or not turno or not presencialidad or not estudios or not experienciaLaboral:
            st.error("Por favor completa todos los campos")
        else:
            insertCurriculum(dni, especialidad, turno, presencialidad, estudios, experienciaLaboral)
            st.session_state.saved = True
            st.session_state["Usuario_encontrado"] = False
            st.success("Datos guardados correctamente")
            if st.session_state.saved:
                if st.button("Ver puestos disponibles para vos"):
                    with st.spinner('Cargando...'):
                        time.sleep(2)  # Espera de 2 segundos
                    switch_page("Matches")  # Esto debería ser reemplazado con tu lógica para cambiar de página
