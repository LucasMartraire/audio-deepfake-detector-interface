import streamlit as st
import time
import random
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import io

# Fonction pour générer et afficher un spectrogramme
def spectrogram_interface(audio_file):
    if audio_file is not None:
        # Lire les données binaires et les convertir en un fichier compatible librosa
        audio_bytes = audio_file.read()
        audio_buffer = io.BytesIO(audio_bytes)

        # Charger l'audio depuis le fichier uploadé
        y, sr = librosa.load(audio_buffer, sr=None)

        # Calculer le spectrogramme
        D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

        # Afficher le spectrogramme avec Matplotlib
        fig, ax = plt.subplots(figsize=(10, 4))
        librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', cmap='magma')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Spectrogram')
        plt.xlabel('Time')
        plt.ylabel('Frequency')

        # Sauvegarde temporaire pour vérifier si l'image est bien créée
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)

        # Afficher l’image directement
        st.image(buf, caption="Music Spectrogram", use_column_width=True)

# Configuration de la page
st.set_page_config(page_title="AI Music Detector", page_icon="🎵", layout="wide")

st.markdown('<div class="title">AI Music Detector</div>', unsafe_allow_html=True)

# Upload de fichier audio
audio_file = st.file_uploader("Drop your music file here", type=["mp3", "wav", "ogg"])

if audio_file is not None:
    st.audio(audio_file, format="audio/mp3")

    if st.button("Analyze Music"):
        with st.spinner('Processing...'):
            time.sleep(2)
            is_ai_generated = random.choice([True, False])

        # Affichage du spectrogramme généré
        spectrogram_interface(audio_file)

        if is_ai_generated:
            st.markdown('<div class="result-box ai">This music is AI-generated</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-box not-ai">This music is not AI-generated</div>', unsafe_allow_html=True)
