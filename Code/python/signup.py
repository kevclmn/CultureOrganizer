# Registro / Login de usuarios
import mysql.connector
import streamlit as st
import verification as vf




mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="102104",
  database="culture_organizer",
)
cursor=mydb.cursor()
signup_page = st.Page("signup.py", title="Sign Up")

st.markdown(        #HTML Estático
    """
    <h1 class="login-title">CULTURE ORGANIZER</h1>
    <p class="login-subtitle">Ingresa tus credenciales para continuar</p>
    <hr class="divider">
    """,
    unsafe_allow_html=True
)

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
      if vf.char_verify("username",username) == True and vf.verify("username",username)==False:        
        cursor.execute(
                f"SELECT password FROM users WHERE username='{username}'"
                )
        password2=cursor.fetchone()[0]
        if password==password2:
          st.success("✅ ¡Login exitoso!")
          ### AÑADIR PASO A LA PAGINA PRINCIPAL
        else:
          st.error("Contraseña incorrecta, intentelo de nuevo")   
      else:
        st.error("Usuario no encontrado")

#st.switch_page("/pages/signup.py")
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
        © 2026 Culture Organizer.
    </p>
    """,
    unsafe_allow_html=True
)
