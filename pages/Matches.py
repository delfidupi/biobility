import streamlit as st
from funciones import dni_exists, match 

if "Usuario_encontrado" not in st.session_state:
    st.session_state["Usuario_encontrado"] = False

if st.session_state.get("Usuario_encontrado", False):
    st.subheader('Los puestos disponibles que coinciden con tu perfil son:')
    puestos = match(st.session_state["dni"])  # Asegúrate de que esta función ejecute la consulta SQL y devuelva un DataFrame con las columnas nombre, descripcion y contacto
    if not puestos.empty:  # Check if the DataFrame is not empty
        for index, row in puestos.iterrows():
            st.write(f"Nombre: {row['nombre']}")
            st.write(f"Descripción: {row['descripcion']}")
            st.write(f"Contacto: {row['contacto']}")
            st.write("---")  # Separador entre puestos
    else:
        st.write("No se encontraron puestos disponibles.")
