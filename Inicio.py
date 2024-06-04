import importlib
import sys
from pathlib import Path
import streamlit as st
from funciones import dni_exists, insertUser, insertEmpresa, id_empresa_exist
from streamlit_extras.switch_page_button import switch_page



st.set_page_config(
    page_title="Biobility",
    page_icon="🔎",
)

st.write("# Biobility 🔎")

st.sidebar.success("Seleccioná lo que estas buscando!")

st.markdown(
    """
    ¿Buscas u ofreces un trabajo en el apasionante mundo de la Ingeniería Biomédica? ¡Has llegado al lugar adecuado!
    Biobility es la plataforma perfecta para conectar a talentosos profesionales como tú con las mejores empresas del sector. Nuestra misión es simplificar tu búsqueda de empleo, ofreciéndote una amplia gama de oportunidades laborales en el campo de la Ingeniería Biomédica.

    **👈Seleccioná lo que estas buscando** 
    ### ¿Qué te ofrecemos?
    - Búsqueda personalizada: Utiliza nuestros filtros avanzados para encontrar trabajos/empleados que se adapten a lo que buscas. 
    - Perfil profesional: Crea un perfil destacado que resalte tus logros, habilidades y experiencia, para que las empresas te encuentren fácilmente.
    - Conexión directa: Conocé al instante las ofertas laborales que coinciden con lo que buscas. 
    - Seguridad y confidencialidad: Tu privacidad es nuestra prioridad. Garantizamos la seguridad de tus datos y mantenemos toda tu información personal de manera confidencial.

    ### ¿Cómo funciona?
    - Si buscas trabajo registrate como usuario y luego ingresa tu información profesional en la pestaña correspondiente.
    - Si ofreces trabajo registrate como empresa e ingresa la información acerca del puesto de trabajo.

    ### ¡Regístrate hoy mismo y comienza a dar el siguiente paso en tu carrera profesional con Biobility!
"""
)
        
col1, col2 = st.columns(2)


with col1:
    st.header("Usuario")
    dni = st.text_input("Ingrese su DNI", key="dni_usuario")
    if st.button("Ingresar como Usuario"):
        if dni_exists(dni):
            st.success("Usuario encontrado")
            switch_page("Profesional Usuario")
        else:
            st.warning("Usuario no registrado")
            if st.button("Registrarse"):
                switch_page("Registro_Usuario")

with col2:
    st.header("Empresa")
    cuit = st.text_input("Ingrese su CUIT", key="cuit_empresa")
    if st.button("Ingresar como Empresa"):
        if id_empresa_exist(cuit):
            st.page_link(r"C:\Users\delfi\OneDrive - Universidad Austral\Desktop\ciencia de datos_app\pages\Puestos disponibles.py",label="Carga un puesto")
        else:
            st.warning("Empresa no registrada")
            st.page_link(r"C:\Users\delfi\OneDrive - Universidad Austral\Desktop\ciencia de datos_app\pages\Registro empresa.py",label="Registrar tu empresa")

