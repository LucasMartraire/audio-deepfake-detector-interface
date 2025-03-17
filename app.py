import streamlit as st
import time
import random

# Configuration de la page
st.set_page_config(page_title="AI Music Detector", page_icon="🎵", layout="wide")

# Style CSS inspiré de Spotify
st.markdown(
    """
    <style>
    body {
        background-color: #181818;
        color: #FFFFFF;
    }
    .stApp {
        background-color: #181818;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .result-box {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
        margin-top: 20px;
    }
    .ai {
        background-color: #FF0000;
        color: white;
    }
    .not-ai {
        background-color: #1DB954;
        color: white;
    }
    .sidebar {
        position: fixed;
        top: 0;
        left: 0;
        width: 80px;
        height: 100%;
        background-color: #000000;
    }
    </style>
    <div class="sidebar"></div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">AI Music Detector</div>', unsafe_allow_html=True)

# Upload de fichier audio
audio_file = st.file_uploader("Drop your music file here", type=["mp3", "wav", "ogg"])

if audio_file is not None:
    st.audio(audio_file, format="audio/mp3")

    # Bouton de lecture avec élément d'attente
    if st.button("Analyze Music"):
        with st.spinner('Processing...'):
            time.sleep(2)  # Simule un temps de traitement
            is_ai_generated = random.choice([True, False])  # Faux résultat pour test

        # Affichage du spectrogramme avec une image locale de secours
        spectrogram_url = "https://upload.wikimedia.org/wikipedia/commons/4/4e/Spectrogram_of_the_Word_Speech.png"
        try:
            st.image(spectrogram_url, caption="Music Spectrogram")
        except Exception as e:
            st.warning("Failed to load online image, using local backup.")
            st.image("spectrogram.png", caption="Music Spectrogram")  # Image locale en backup

        # Message de détection
        if is_ai_generated:
            st.markdown('<div class="result-box ai">This music is AI-generated</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-box not-ai">This music is not AI-generated</div>', unsafe_allow_html=True)
