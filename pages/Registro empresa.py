import streamlit as st
from funciones import insertEmpresa

st.session_state["Empresa encontrado"] = False
st.title("Registrar Empresa")
id_empresa = st.text_input("CUIT")
nombre = st.text_input("Nombre")
zona = st.selectbox("Zona de la empresa: Norte/Sur/Oeste/CABA", ("N", "O", "S", "C"))

if st.button("Guardar"):
    if not id_empresa or not nombre or not zona:
        st.error("Por favor completa todos los campos")
    else:
        insertEmpresa(id_empresa, nombre, zona)
        with st.spinner('Cargando...'):
            time.sleep(4)  # Espera de 2 segundos
        switch_page("Puestos disponibles")

