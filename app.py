import streamlit as st
import time
import random

st.title("Détection de musique générée par l'IA")

# Upload de fichier audio
audio_file = st.file_uploader("Déposez une musique ici", type=["mp3", "wav", "ogg"])

if audio_file is not None:
    st.audio(audio_file, format="audio/mp3")

    # Bouton de lecture avec élément d'attente
    if st.button("Analyser la musique"):
        with st.spinner('Analyse en cours...'):
            time.sleep(2)  # Simule un temps de traitement
            is_ai_generated = random.choice([True, False])  # Faux résultat pour test

        # Affichage du spectrogramme factice
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Spectrogram-19thC.png/800px-Spectrogram-19thC.png", caption="Spectrogramme de la musique")

        # Message de détection
        if is_ai_generated:
            st.markdown('<div style="background-color: red; padding: 10px; text-align: center; font-size: 20px; color: white;">Cette musique est générée par l\'IA</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="background-color: green; padding: 10px; text-align: center; font-size: 20px; color: white;">Cette musique n'est pas générée par l'IA</div>', unsafe_allow_html=True)
