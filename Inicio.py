import importlib
import sys
from pathlib import Path
import streamlit as st
from funciones import dni_exists, insertUser, insertEmpresa, id_empresa_exist
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import requests
from io import BytesIO


st.set_page_config(page_title="Biobility")

# URL de la imagen en GitHub
image_url = "https://github.com/delfidupi/biobility/blob/main/logo.jpg?raw=true"

# Descargar la imagen desde la URL
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Convertir la imagen a formato base64 para incrustarla en HTML
import base64
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# CSS para personalizar la apariencia
st.markdown(f"""
    <style>
    .header-container {{
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .header-logo {{
        width: 100px;
        margin-right: 20px;
    }}
    .header-title {{
        font-size: 2.5em;
        font-weight: bold;
    }}
    </style>
    <div class="header-container">
        <img src="data:image/jpeg;base64,{img_str}" class="header-logo">
        <div class="header-title">Biobility</div>
    </div>
    """, unsafe_allow_html=True)

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

st.markdown(
    """
    ¿Buscas u ofreces un trabajo en el apasionante mundo de la Ingeniería Biomédica? ¡Has llegado al lugar adecuado!
    Biobility es la plataforma perfecta para conectar a talentosos profesionales como tú con las mejores empresas del sector. Nuestra misión es simplificar tu búsqueda de empleo, ofreciéndote una amplia gama de oportunidades laborales en el campo de la Ingeniería Biomédica.

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

# Función para obtener los DNIs almacenados en las cookies
def get_recent_dnis():
    recent_dnis = st.session_state.get('recent_dnis', [])
    return recent_dnis

# Función para almacenar un nuevo DNI en las cookies
def add_recent_dni(dni):
    recent_dnis = get_recent_dnis()
    if dni not in recent_dnis:
        recent_dnis.append(dni)
        st.session_state['recent_dnis'] = recent_dnis

# Crear pestañas para cambiar entre Usuario y Empresa
tab1, tab2 = st.tabs(["Soy Usuario", "Soy Empresa"])

with tab1:
    st.header("👤 Usuarios")
    dni = st.text_input("Ingrese su DNI", key="dni_usuario")

    if dni:
        if dni_exists(dni):
            st.success("DNI registrado. ¿Qué te gustaría hacer?")
            if st.button("Crear Currículum"):
                switch_page("Profesional Usuario")
            if st.button("Ver Puestos que Coinciden"):
                switch_page("Matches")
        else:
            st.warning("DNI no registrado. Redirigiendo a la página de registro...")
            switch_page("Registro Usuario")

with tab2:
    st.header("🏢 Empresas")
    cuit = st.text_input("Ingrese su CUIT", key="cuit_empresa")

    if cuit:
        if id_empresa_exist(cuit):
            st.success("CUIT registrado. ¿Qué te gustaría hacer?")
            if st.button("Publicar Puesto"):
                switch_page("Puestos disponibles")
        else:
            st.warning("CUIT no registrado. Redirigiendo a la página de registro...")
            switch_page("Registro Empresa")

# Pie de página
st.markdown(
    """
    ---
    **Biobility** - Simplificando tu búsqueda de empleo en el campo de la Ingeniería Biomédica.
    """
)


