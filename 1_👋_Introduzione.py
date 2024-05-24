import streamlit as st
import base64
from PIL import Image

# Metodo per convertire immagine in una stringa base64 utilizzabile
# in un codice html
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
    
st.set_page_config(page_title="Portfolio", layout="centered")

st.sidebar.expander("Sidebar", expanded=True)

with st.sidebar:
    st.title("Contact")
    
    # Converto immagini in stringhe base64 per poterle usare nel markdown
    linkedin_img = load_image("img/linkedin_logo.png")
    github_img = load_image("img/github_logo.png")
    gmail_img = load_image("img/gmail_logo.png")

    # Gmail
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <img src="data:image/png;base64,{gmail_img}" style="width:30px; margin-right: 10px;">
            <span>aleguerrisi01@gmail.com</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # GitHub
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <img src="data:image/png;base64,{github_img}" style="width:30px; margin-right: 10px;">
            <a href="https://github.com/alegue4" target="_blank">Github Profile</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # LinkedIn
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <img src="data:image/png;base64,{linkedin_img}" style="width:30px; margin-right: 10px;">
            <a href="https://www.linkedin.com/in/alessandro-guerrisi" target="_blank">Linkedin Profile</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.title("CV")
    # Pulsante per scaricare il CV
    cv_file_path = "img/CV_Guerrisi_Alessandro.pdf"
    with open(cv_file_path, "rb") as cv_file:
        cv_bytes = cv_file.read()
    st.download_button(
        label="📄 Scarica il mio CV",
        data=cv_bytes,
        file_name="CV_Alessandro_Guerrisi.pdf",
        mime="application/pdf",
    )

col1, col2 = st.columns([1, 2])

with col1:
    profile_pic = Image.open("img/profile_pic.png")
    st.image(profile_pic, use_column_width=True)
with col2:
    # Title
    st.title("Alessandro Guerrisi", anchor=False)
    st.write("""Mi chiamo Alessandro Guerrisi e sono uno studente del corso di laurea triennale di Scienze e Tecnologie Informatiche 
             presso l'Università degli Studi di Milano-Bicocca. Ho una grande passione per l'informatica, soprattutto
             per lo sviluppo sofware e mobile ma anche per la gestione e l'analisi dei dati.""")
# Competenze principali
st.subheader("🔧 Competenze Principali")
st.write("""
- 💻 Sviluppo Android con Android Studio e Java
- 🐍 Sviluppo Web con Streamlit e Python
- 📊 Database come MySQL, MongoDB, Redis
- 🌐 Programmazione in C++ con Qt
""")

# Obiettivi di carriera
st.subheader("🎯 Obiettivi di Carriera")
st.write("""
Il mio obiettivo è contribuire a progetti innovativi che abbiano un impatto significativo, continuando a crescere 
professionalmente e ad apprendere nuove tecnologie. Sono sempre curioso di conoscere ulteriori tecnologie e migliorare 
le mie competenze per rimanere al passo con i rapidi cambiamenti del settore.
""")