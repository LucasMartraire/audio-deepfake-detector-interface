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
        background-color: #121212;
        color: #FFFFFF;
    }
    .stApp {
        background-color: #121212;
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
    }
    .ai {
        background-color: #FF0000;
        color: white;
    }
    .not-ai {
        background-color: #1DB954;
        color: white;
    }
    </style>
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

        # Affichage du spectrogramme factice
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Spectrogram-19thC.png/800px-Spectrogram-19thC.png", caption="Music Spectrogram")

        # Message de détection
        if is_ai_generated:
            st.markdown('<div class="result-box ai">This music is AI-generated</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-box not-ai">This music is not AI-generated</div>', unsafe_allow_html=True)
