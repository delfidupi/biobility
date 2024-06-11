import streamlit as st
from funciones import insertPostulacion, id_empresa_exist

if "Empresa_encontrada" not in st.session_state:
    st.session_state["Empresa_encontrada"] = False


st.markdown(
    """
    <h1 style="font-family: 'Roboto', sans-serif; color: #494666;">
        Publique un puesto
    </h1>
    """,
    unsafe_allow_html=True
)
id_empresa = st.text_input("CUIT")
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

if st.button('Buscar'):
    if id_empresa_exist(id_empresa):
        st.session_state["Empresa_encontrada"] = True
        st.session_state["CUIT"]= id_empresa
    else:
        st.error("Empresa no encontrada") 
        st.session_state["Empresa_encontrada"] =False

if st.session_state.get("Empresa_encontrada", False):
    st.subheader('Carga los datos del puesto disponible')
    especialidad = st.selectbox("Especialidad que se necesita: Bioinformatica (B), Protesis (P), Genética (G), Imagenes biomedicas (I)", ("B", "P", "G", "I"))
    turno = st.selectbox("Turno que se necesita: Mañana (M), Tarde (T), Noche (N)", ("M", "T", "N"))
    presencialidad= st.selectbox("Presencialidad", ("Si", "No"))
    experienciaLaboral = st.selectbox("¿Necesita experiencia laboral?", ("Si", "No"))
    descripcion = st.text_input("Breve descripción del puesto: ")
    contacto = st.text_input("Numero de contacto para aspirantes: ")

    if st.button("Guardar"):
        if not id_empresa or not especialidad or not turno or not presencialidad or not experienciaLaboral or not descripcion or not contacto:
            st.error("Por favor completa todos los campos")
        else:
            insertPostulacion(id_empresa, especialidad, turno, presencialidad, experienciaLaboral, descripcion, contacto)
            st.session_state['Empresa_encontrada'] = False
            st.markdown(
                """
                <div style="font-size:20px;">
                    ¡Muchas gracias! Espero que pronto encontremos al candidato perfecto para el puesto que ofreces. Le dejaremos su teléfono de contacto para que se comunique contigo.
                </div>
                """,
                unsafe_allow_html=True
            )
            
            




    
            
