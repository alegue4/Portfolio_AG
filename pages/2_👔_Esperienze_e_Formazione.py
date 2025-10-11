import streamlit as st
from utils import setup_sidebar
    
st.set_page_config(page_title="Portfolio", layout="centered")
setup_sidebar()

# Esperienze lavorative
st.markdown("<h2 style='text-align: center;'>Esperienze lavorative</h2>", unsafe_allow_html=True)
with st.expander("Collaboratore Studentesco, Biblioteca Università degli Studi di Milano-Bicocca", expanded=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img/bicocca_logo.png")
    with col2:
        st.write("**Periodo**: Settembre 2023 - Novembre 2023")
        st.write("""**Descrizione**: Collaboratore studentesco presso la biblioteca 
                 della Sede Centrale dell'Università degli Studi di Milano-Bicocca. Organizzazione e 
                 ricollocazione libri, assistenza generale a studenti per l'utilizzo dei 
                 servizi della biblioteca.""")

# Formazione
st.markdown("<h2 style='text-align: center;'>Formazione</h2>", unsafe_allow_html=True)
with st.expander("Master in Informatics at USI with Università degli Studi di Milano-Bicocca", expanded=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img/usi_logo.png")
        st.image("img/bicocca_logo.png")
    with col2:
        st.write("**Periodo**: October 2024 - expected July 2026")
        st.write("""**Descrizione**: Studente frequentante l'ultimo anno di triennale, con soli 2 esami 
                 mancanti e scrittura tesi in corso. Ho conosciuto le basi dell'informatica, come lo sviluppo
                 software e mobile, creazione e gestione di database, reti e sistemi operativi, algoritmi e tempi
                 di esecuzione.""")
        
with st.expander("Laurea Triennale in Scienze e Tecnologie Informatiche, Milano-Bicocca", expanded=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img/bicocca_logo.png")
    with col2:
        st.write("**Periodo**: Ottobre 2021 - Ottobre 2024")
        st.write("""**Descrizione**: Studente frequentante l'ultimo anno di triennale, con soli 2 esami 
                 mancanti e scrittura tesi in corso. Ho conosciuto le basi dell'informatica, come lo sviluppo
                 software e mobile, creazione e gestione di database, reti e sistemi operativi, algoritmi e tempi
                 di esecuzione.""")

with st.expander("Perito elettronico ed elettrotecnico, ITIS Ettore Conti", expanded=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img/conti_logo.png")
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
with st.expander("Certificazione IELTS Livello C1 - Valutazione 7.5"):
    st.write("**Periodo**: Luglio 2025 - Agosto 2025")
    st.write("**Descrizione**: Certficazione IELTS livello C1 con valutazione complessiva pari a 7.5")
    st.write("Punteggio Listening: 8.0 Punteggio Reading: 8.0 Punteggio Writing: 6.0 Punteggio Speaking: 7.0")