import requests
import tempfile
import os

import streamlit as st



st.set_page_config(page_title="AI Music Detector",
                   page_icon="🎵",
                   layout="wide")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #1E1E1E, #2D005F, #9000FF); /* Black to Purple gradient */
        color: #FFFFFF;
    }
    .stApp {
        background: linear-gradient(135deg, #1E1E1E, #2D005F, #9000FF);
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 30px;
        color: #FF0080; /* Pinkish Purple */
    }
    .result-box {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(255, 0, 128, 0.5); /* Pink glow */
        margin-top: 20px;
    }
    .ai {
        background-color: #FF0066; /* Bright pink */
        color: white;
    }
    .not-ai {
        background-color: #4B0082; /* Deep purple */
        color: white;
    }
    .sidebar {
        position: fixed;
        top: 0;
        left: 0;
        width: 80px;
        height: 100%;
        background-color: #0A001F; /* Dark purple */
    }
    </style>
    <div class="sidebar"></div>
    """,
    unsafe_allow_html=True
)

# st.title("<p style='text-align:center;'> AI-Generated Music Detector </p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color:#C00060;'> 🎵 AI-Generated Music Detector 🎵 </h1><br><br>", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }

    .bounce {
        animation: bounce 2s infinite;
    }
    </style>
    <div class="bounce">
        <p style='text-align:center;'> Upload an audio file to check if it's AI-generated! </p><br>
    </div>
    """,
    unsafe_allow_html=True
)




uploaded_file = st.file_uploader("Choose an audio file:",
                                 type=["wav", "mp3"])



if uploaded_file:
    #st.success("✨​✨​  File uploaded successfully!  ✨​✨​")
    st.audio(uploaded_file)

    # send the file_path to the api:


    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

    response = requests.post("https://adf-190527601687.europe-west9.run.app/predict", files=files)


    if response.status_code == 200:
        result = response.json()

        print(result)

        if result == "This sound has been AI generated":
            st.markdown(
            """
            <style>
            body {
                background: linear-gradient(45deg, #FF0000, #FF8C00);  /* Red to Orange Gradient */
                color: white;  /* Set text color to white for contrast */
            }
            .stApp {
                background: linear-gradient(45deg, #FF0000, #FF8C00); /* Apply gradient to entire Streamlit app */
            }
            </style>
            """,
            unsafe_allow_html=True
            )

            st.header(result)

        else:
            st.header(result)

    else:
        print(response)
