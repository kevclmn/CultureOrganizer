import streamlit as st

# CSS puro - SOLO ESTILOS
st.markdown(
    """
    <style>
    /* Fondo y contenedor principal */
    .login-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 80vh;
    }
    
 
   
    .login-title {
        text-align: center;
        color: #2c3e50;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 8px;
    }
    
    .login-subtitle {
        text-align: center;
        color: #7f8c8d;
        font-size: 14px;
        margin-bottom: 30px;
    }
    
    /* Botón de login personalizado */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 12px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    /* Inputs personalizados */
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e0e5ec;
        padding: 12px 16px;
        transition: all 0.3s;
        font-size: 14px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
        outline: none;
    }
    
    /* Separador decorativo */
    .divider {
        border: none;
        border-top: 2px solid #e8ecf1;
        margin: 25px 0;
    }
    
    /* Enlaces */
    .footer-links {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
        color: #95a5a6;
    }
    
    .footer-links az {
        color: #667eea;
        text-decoration: none;
        font-weight: 500;
    }
    
    .footer-links a:hover {
        text-decoration: underline;
    }
    
    /* Mensajes de éxito/error */
    .stAlert {
        border-radius: 12px;
        border: none;
        padding: 12px 20px;
    }
    
    .stAlert > div {
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML estático para estructura - SIN INTERACTIVIDAD
st.markdown(
    """
    <h1 class="login-title">CULTURE ORGANIZER</h1>
    <p class="login-subtitle">Ingresa tus credenciales para continuar</p>
    <hr class="divider">
    """,
    unsafe_allow_html=True
)

# Widgets NATIVOS de Streamlit (seguros)
with st.form("login_form"):
    username = st.text_input(
        "👤 Usuario",
        placeholder="user@ejemplo.com",
        help="Ingresa tu email de usuario"
    )
    
    password = st.text_input(
        "🔑 Contraseña",
        type="password",
        placeholder="••••••••"
    )
    
    if st.form_submit_button("🚀 Iniciar Sesión"):
        if username == "admin@ejemplo.com" and password == "123456":
            st.success("✅ ¡Login exitoso!")
        else:
            st.error("❌ Credenciales incorrectas")

# HTML estático para el footer
st.markdown(
    """
    <hr class="divider">
    <div class="footer-links">
        <a href="#">¿Olvidaste tu contraseña?</a>
        <span style="margin: 0 10px;">•</span>
        <a href="#">Crear cuenta</a>
    </div>
    <p style="text-align: center; color: #bdc3c7; font-size: 12px; margin-top: 20px;">
        © 2026 Culture Organizer. Todos los derechos reservados.
    </p>
    """,
    unsafe_allow_html=True
)

