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

# Title
st.markdown("<h2 style='text-align: center;'>Progetti</h2>", unsafe_allow_html=True)
with st.expander("**PROGETTI**", expanded=True):
    st.write("In questa sezione vanno inseriti i progetti")
        
with st.expander("**PROGETTI UNIVERSITARI**", expanded=True):
    cpp_img = load_image("img/cpp_logo.png")
    qt_img = load_image("img/qt_logo.png")
    android_img = load_image("img/android_logo.png")
    java_img = load_image("img/java_logo.png")
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <div style="margin-right: 10px;">
                <h2>Uffizi</h2>
                <p><b>Data</b>: Gennaio 2024 - Febbraio 2024</p>
                <p><b>Tipologia</b>: Progetto eseguito individualmente.</p>
                <p><b>C++</b>: Definizione della classe di un Set contente dati di tipo generico (sia
                    dati primitivi che dati custom). La classe deve permettere aggiunta, rimozione e ricerca di dati
                    all'interno del Set senza utilizzare strutture a lista.</p>
                <p><b>Qt</b>: Implementazione di una GUI per visualizzazione, ricerca e modifica di un Set
                    di dipinti estratti da un file CSV.</p>
                <a href="https://github.com/alegue4/Uffizi_Cpp_Qt" target="_blank">Github Repository</a>
            </div>
            <div style="margin-right: 10px">
                <img src="data:image/png;base64,{cpp_img}" style="width:80px; margin-left: 15px; margin-bottom: 20px">
                <img src="data:image/png;base64,{qt_img}" style="width:80px; margin-left: 15px; margin-right: 10px;">
            </div>
        </div>
        <hr style="margin-bottom:10px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="margin-right: 10px;">
                <h2>Pokèdex</h2>
                <p><b>Data</b>: Gennaio 2024 - Febbraio 2024</p>
                <p><b>Tipologia</b>: Progetto eseguito individualmente.</p>
                <p><b>C++</b>: Definizione della classe di un grafo orientato che deve permettere aggiunta, rimozione e
                    ricerca di nodi e archi presenti nel grafo. Non vengono usate strutture a lista</p>
                <p><b>Qt</b>: Implementazione di una GUI per visualizzazione, ricerca e filtraggio di una tabella
                    di Pokèmon. E' inoltre presente una schermata per confrontare le statistiche tra 2 Pokèmon
                    distinti</p>
                <a href="https://github.com/alegue4/Pokemon_Cpp_Qt" target="_blank">Github Repository</a>
            </div>
            <div style="margin-right: 10px">
                <img src="data:image/png;base64,{cpp_img}" style="width:80px; margin-left: 15px; margin-bottom: 20px">
                <img src="data:image/png;base64,{qt_img}" style="width:80px; margin-left: 15px; margin-right: 10px;">
            </div>
        </div>
        <hr style="margin-bottom:10px;">
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="margin-right: 10px;">
                <h2>SportQ</h2>
                <p><b>Data</b>: Dicembre 2023 - Gennaio 2024</p>
                <p><b>Tipologia</b>: Progetto eseguito in gruppo.</p>
                <p><b>Descrizione</b>: Realizzazione di App mobile con Android Studio e utilizzando Java.
                    In questa applicazione è possibile cercare dei campi da gioco/centri sportivi vicini ed
                    aggiungerli alla propria lista di preferiti. Vengono utilizzate, PlacesAPI e Google Maps SDK per
                    ottenere la lista di campi disponibili nella propria zona e per ottenere una mappa interattiva.
                    Viene inoltre utilizzato Firebase per il salvataggio e la gestione degli utenti iscritti.</p>
                <a href="https://github.com/alegue4/SportQ" target="_blank">Github Repository</a>
            </div>
            <div style="margin-right: 10px">
                <img src="data:image/png;base64,{android_img}" style="width:80px; margin-left: 15px; margin-bottom: 20px">
                <img src="data:image/png;base64,{java_img}" style="width:80px; margin-left: 15px; margin-right: 10px;">
            </div>
        </div>

        """,
        unsafe_allow_html=True
    )

