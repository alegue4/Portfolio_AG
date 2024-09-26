import streamlit as st
import base64

# Metodo per convertire immagine in una stringa base64 utilizzabile
# in un codice html
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
    
def setup_sidebar():
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
        cv_file_path = "cv/CV Alessandro Guerrisi DE.pdf"
        with open(cv_file_path, "rb") as cv_file:
            cv_bytes = cv_file.read()
        st.download_button(
            label="📄 Scarica il mio CV",
            data=cv_bytes,
            file_name="CV_Alessandro_Guerrisi.pdf",
            mime="application/pdf",
        )