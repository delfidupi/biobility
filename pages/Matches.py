import streamlit as st
from funciones import dni_exists, match 
from streamlit_extras.switch_page_button import switch_page


if "Usuario_encontrado" not in st.session_state:
    st.session_state["Usuario_encontrado"] = False
    
st.title("Ingreso de usuario")
dni = st.text_input("DNI")

if st.button('Buscar'):
    if dni_exists(dni):
        st.session_state["Usuario_encontrado"] = True
        st.session_state["dni"]= dni
        if st.session_state.get("Usuario_encontrado", False):
            st.subheader('Los puestos disponibles que coinciden con tu perfil son:')
            puestos = match(st.session_state["dni"])  # Asegúrate de que esta función ejecute la consulta SQL y devuelva un DataFrame con las columnas nombre, descripcion y contacto
            if not puestos.empty:  # Check if the DataFrame is not empty
                for index, row in puestos.iterrows():
                    st.write(f"🔵 Nombre: {row['nombre']}")
                    st.write(f"Descripción: {row['descripcion']}")
                    st.write(f"Contacto: {row['contacto']}")
                    st.write("---")  # Separador entre puestos
                st.globos()
            else:
                st.write("No se encontraron puestos disponibles.")
    else:
        st.error("Usuario no encontrado") 
        st.session_state["Usuario_encontrado"] =False

