import streamlit as st
from utils import setup_sidebar, load_image

st.set_page_config(page_title="Portfolio", layout="centered")
setup_sidebar()

# Title
st.markdown("<h2 style='text-align: center;'>Progetti</h2>", unsafe_allow_html=True)
cpp_img = load_image("img/cpp_logo.png")
qt_img = load_image("img/qt_logo.png")
android_img = load_image("img/android_logo.png")
java_img = load_image("img/java_logo.png")
python_img = load_image("img/python_logo.png")
streamlit_img = load_image("img/streamlit_logo.png")
sr_inv_img = load_image("img/sr_inv_logo_bianco.png")

with st.expander("**PROGETTI ESTERNI**", expanded=True):
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <div style="margin-right: 10px; flex: 1;">
                <h2>SR_Inv</h2>
                <p><b>Data</b>: Luglio 2024 - In Corso</p>
                <p><b>Tipologia</b>: Progetto eseguito in gruppo.</p>
                <p><b>Descrizione</b>: Web App che permette l'analisi di dati finanziari, andamento del mercato e la gestione
                di un portafoglio in cui salvare guadagni e perdite in seguito agli investimenti effettuati. Il progetto è in 
                collaborazione con un gruppo di amici provenienti da altri settori, nel quale io mi occupo del lato informatico.
                Essendo il progetto ancora in corso e riservato al gruppo SR_Inv purtroppo non saranno presenti la Repository Github 
                e neanche l'URL del sito.</p>
                <p><b>Tecnologie utilizzate</b>: Python, Streamlit, NeonDB</p>
            </div>
            <div style="display: flex; flex-direction: column; align-items: center; margin-left: 15px;">
                <img src="data:image/png;base64,{sr_inv_img}" style="width:80px; margin-bottom: 20px">
                <img src="data:image/png;base64,{python_img}" style="width:80px; margin-bottom: 20px">
                <img src="data:image/png;base64,{streamlit_img}" style="width:80px; margin-bottom: 20px">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
        
with st.expander("**PROGETTI UNIVERSITARI**", expanded=True):
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <div style="margin-right: 10px; flex: 1;">
                <h2>Uffizi</h2>
                <p><b>Data</b>: Gennaio 2024 - Febbraio 2024</p>
                <p><b>Tipologia</b>: Progetto eseguito individualmente.</p>
                <p><b>Descrizione</b>:
                </p>
                <ul>
                    <li><b>C++</b>: Definizione della classe di un Set contente dati di tipo generico (sia
                    dati primitivi che dati custom). La classe deve permettere aggiunta, rimozione e ricerca di dati
                    all'interno del Set senza utilizzare strutture a lista.</li>
                </ul>
                <ul>
                    <li><b>Qt</b>: Implementazione di una GUI per visualizzazione, ricerca e modifica di un Set
                    di dipinti estratti da un file CSV.</li>
                </ul>
                <p><b>Tecnologie utilizzate</b>: C++, Qt</p>
                <a href="https://github.com/alegue4/Uffizi_Cpp_Qt" target="_blank">Github Repository</a>
            </div>
            <div style="display: flex; flex-direction: column; align-items: center; margin-left: 15px;">
                <img src="data:image/png;base64,{cpp_img}" style="width:80px; margin-bottom: 20px">
                <img src="data:image/png;base64,{qt_img}" style="width:80px; margin-bottom: 20px">
            </div>
        </div>
        <hr style="margin-bottom:10px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="margin-right: 10px; flex: 1;">
                <h2>Pokèdex</h2>
                <p><b>Data</b>: Gennaio 2024 - Febbraio 2024</p>
                <p><b>Tipologia</b>: Progetto eseguito individualmente.</p>
                <p><b>Descrizione</b>:</p>
                <ul>
                    <li><b>C++</b>: Definizione della classe di un grafo orientato che deve permettere aggiunta, rimozione e
                    ricerca di nodi e archi presenti nel grafo. Non vengono usate strutture a lista</li>
                </ul>
                <ul>
                    <li><b>Qt</b>: Implementazione di una GUI per visualizzazione, ricerca e filtraggio di una tabella
                    di Pokèmon. E' inoltre presente una schermata per confrontare le statistiche tra 2 Pokèmon
                    distinti</li>
                </ul>
                <p><b>Tecnologie utilizzate</b>: C++, Qt</p>
                <a href="https://github.com/alegue4/Pokemon_Cpp_Qt" target="_blank">Github Repository</a>
            </div>
            <div style="display: flex; flex-direction: column; align-items: center; margin-left: 15px;">
                <img src="data:image/png;base64,{cpp_img}" style="width:80px; margin-bottom: 20px">
                <img src="data:image/png;base64,{qt_img}" style="width:80px; margin-bottom: 20px">
            </div>
        </div>
        <hr style="margin-bottom:10px;">
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="margin-right: 10px; flex: 1;">
                <h2>SportQ</h2>
                <p><b>Data</b>: Dicembre 2023 - Gennaio 2024</p>
                <p><b>Tipologia</b>: Progetto eseguito in gruppo.</p>
                <p><b>Descrizione</b>: Realizzazione di App mobile con Android Studio e utilizzando Java.
                    In questa applicazione è possibile cercare dei campi da gioco/centri sportivi vicini ed
                    aggiungerli alla propria lista di preferiti. Vengono utilizzate, PlacesAPI e Google Maps SDK per
                    ottenere la lista di campi disponibili nella propria zona e per ottenere una mappa interattiva.
                    Viene inoltre utilizzato Firebase per il salvataggio e la gestione degli utenti iscritti.</p>
                <p><b>Tecnologie utilizzate</b>: Java, Android Studio, Firebase DB, Architettura MVVM</p>
                <a href="https://github.com/alegue4/SportQ" target="_blank">Github Repository</a>
            </div>
            <div style="display: flex; flex-direction: column; align-items: center; margin-left: 15px;">
                <img src="data:image/png;base64,{android_img}" style="width:80px; margin-bottom: 20px">
                <img src="data:image/png;base64,{java_img}" style="width:80px; margin-bottom: 20px;">
            </div>
        </div>

        """,
        unsafe_allow_html=True
    )

