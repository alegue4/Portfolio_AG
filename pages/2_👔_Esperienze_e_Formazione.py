import streamlit as st
import base64

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
    cv_file_path = "img/CV_Alessandro_Guerrisi.pdf"
    with open(cv_file_path, "rb") as cv_file:
        cv_bytes = cv_file.read()
    st.download_button(
        label="📄 Scarica il mio CV",
        data=cv_bytes,
        file_name="CV_Alessandro_Guerrisi.pdf",
        mime="application/pdf",
    )

# Esperienze lavorative
st.markdown("<h2 style='text-align: center;'>Esperienze lavorative</h2>", unsafe_allow_html=True)
with st.expander("Collaboratore Studentesco, Biblioteca Università degli Studi di Milano-Bicocca", expanded=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img/bicocca_logo.png", use_column_width=True)
    with col2:
        st.write("**Periodo**: Settembre 2023 - Novembre 2023")
        st.write("""**Descrizione**: Collaboratore studentesco presso la biblioteca 
                 della Sede Centrale dell'Università degli Studi di Milano-Bicocca. Organizzazione e 
                 ricollocazione libri, assistenza generale a studenti per l'utilizzo dei 
                 servizi della biblioteca.""")

# Formazione
st.markdown("<h2 style='text-align: center;'>Formazione</h2>", unsafe_allow_html=True)
with st.expander("Laurea Triennale in Scienze e Tecnologie Informatiche, Milano-Bicocca", expanded=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img/bicocca_logo.png", use_column_width=True)
    with col2:
        st.write("**Periodo**: Ottobre 2021 - Ottobre 2024")
        st.write("""**Descrizione**: Studente frequentante l'ultimo anno di triennale, con soli 2 esami 
                 mancanti e scrittura tesi in corso. Ho conosciuto le basi dell'informatica, come lo sviluppo
                 software e mobile, creazione e gestione di database, reti e sistemi operativi, algoritmi e tempi
                 di esecuzione.""")

with st.expander("Perito elettronico ed elettrotecnico, ITIS Ettore Conti", expanded=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img/conti_logo.png", use_column_width=True)
    with col2:
        st.write("**Periodo**: Settembre 2015 - Giugno 2020")
        st.write("""**Descrizione**: Diploma di perito elettronico ed elettrotecnico con votazione 89/100.
                 Durante il mio percorso di studi ho sviluppato le principali competenze:""")
        st.write("""
        - **Progettazione e realizzazione di circuiti elettronici**: Dalla progettazione al e testing di circuiti analogici e digitali.
        - **Programmazione di microcontrollori**: Utilizzo di linguaggi di programmazione come C e utilizzo di Arduino
        """)

# Certificazioni
st.markdown("<h2 style='text-align: center;'>Certificazioni</h2>", unsafe_allow_html=True)
with st.expander("Certificazione Cambridge Livello B2"):
    st.write("**Periodo**: Gennaio 2020 - Dicembre 2020")
    st.write("""**Descrizione**: Certficazione Cambridge livello B2""")
