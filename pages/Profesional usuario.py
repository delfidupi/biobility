import streamlit as st
from funciones import insertCurriculum, dni_exists

if "Usuario_encontrado" not in st.session_state:
    st.session_state["Usuario_encontrado"] = False

st.title("Ingreso de usuario")
dni = st.text_input("DNI")

if st.button('Buscar'):
    if dni_exists(dni):
        st.session_state["Usuario_encontrado"] = True
        st.session_state["dni"]= dni
    else:
        st.error("Usuario no encontrado") 
        st.session_state["Usuario_encontrado"] =False

if st.session_state.get("Usuario_encontrado", False):
    st.subheader('Carga tus datos profesionales')
    especialidad = st.selectbox("Especialidad: Bioinformatica (B), Protesis (P), Genética (G), Imagenes biomedicas (I)", ("B", "P", "G", "I"))
    turno = st.selectbox("Turno: Mañana (M), Tarde (T), Noche (N)", ("M", "T", "N"))
    presencialidad= st.selectbox("Presencialidad", ("Si", "No"))
    estudios = st.text_input("¿Donde te recibiste?")
    experienciaLaboral = st.selectbox("¿Tenes experiencia laboral?", ("Si", "No"))

# Definir el estado de guardado
if 'saved' not in st.session_state:
    st.session_state.saved = False

# Definir el estado de guardado
if 'saved' not in st.session_state:
    st.session_state.saved = False

if st.button("Guardar"):
    if not dni or not especialidad or not turno or not presencialidad or not estudios or not experienciaLaboral:
        st.error("Por favor completa todos los campos")
    else:
        insertCurriculum(dni, especialidad, turno, presencialidad, estudios, experienciaLaboral)
        st.session_state.saved = True
        st.session_state['Usuario_encontrado'] = False
        st.success("Datos guardados correctamente")

# Mostrar el botón "Crear un curriculum" solo si los datos han sido guardados
if st.session_state.saved:
    if st.button("Crear un curriculum"):
        with st.spinner('Cargando...'):
            time.sleep(2)  # Espera de 2 segundos
        switch_page("Profesional Usuario")
