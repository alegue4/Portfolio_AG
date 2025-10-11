import streamlit as st
from PIL import Image
from utils import setup_sidebar

    
st.set_page_config(page_title="Portfolio", layout="centered")
setup_sidebar()

col1, col2 = st.columns([1, 2])

with col1:
    profile_pic = Image.open("img/profile_pic_update.png")
    st.image(profile_pic, )
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