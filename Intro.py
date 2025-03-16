import streamlit as st
import base64
import time

def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
        page_background = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpeg;base64,{encoded_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #FFFFFF;
        }}
        </style>
        """
        st.markdown(page_background, unsafe_allow_html=True)

def Intro_page():
    time.sleep(0.5)
    set_background("other images/Backround.webp")

    st.markdown(
        """
        <style>
        .container {
            background: linear-gradient(135deg, #2a5ba8, #4c82c7, #3b6fb3);
            color: white;
            border-radius: 25px;
            padding: 8px;
            padding-bottom: 10px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            max-width: 400px;
            margin: auto;
            font-family: 'Poppins', sans-serif;
        }
        .block-container {
            padding-top: 25px !important;
            margin-top: 25px !important;
        }
        .header {
            font-size: 26px;
            font-weight: 600;
            margin-bottom: 20px;
            color: #ffffff;
        }
        .description {
            font-size: 22px;
            font-weight: 300;
            margin-bottom: 20px;
            color: #ffffff;
        }
        .footer {
            font-size: 16px;
            margin-top: 20px;
            color: #ffffff;
        }
        .green-text {
            color: #50c878;
            font-weight: 600;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.9);
        }
        .red-text {
            color: #FF4747; 
            font-weight: 600;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.9);
        }
        </style>
        <div class="container">
            <div class="header"> Like or Dislike? <br> Let's explore your music taste! </div>
            <div class="description">
                <span class="green-text">Like the song?</span>&nbsp;&nbsp;Tap 👍 <br>
                <span class="red-text">Not your vibe?</span>&nbsp;&nbsp;Tap 👎
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    def handle_start_click():
        st.session_state.page = "song_user_classification"

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("Let's go!", key="start-btn", on_click=handle_start_click, use_container_width=True)


import streamlit as st
import pandas as pd
from Intro import set_background
import time


def song_user_classification_page():
    time.sleep(0.2)
    set_background("other images/Backround.webp")
    songs_df = pd.read_csv('playlists_excel/classification_songs.csv')

    if "song_feedback" not in st.session_state:
        st.session_state.song_feedback = {}
    if "current_song_index" not in st.session_state:
        st.session_state.current_song_index = 0

    current_index = st.session_state.current_song_index

    if current_index < len(songs_df):
        current_song = songs_df.loc[current_index, 'song']
        st.markdown(
            """
            <style>
            .container {
                background: linear-gradient(90deg, #3b5998, #4a69bd); 
                color: white;
                border-radius: 25px;
                padding: 13px;
                margin: auto;
                text-align: center;
                box-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
                max-width: 500px;
                margin: 20px auto;
                font-family: Arial, sans-serif;
                font-size: 22px;
                border: 3px solid #a0c4ff;
                margin-bottom: 3px !important;
            }
            .block-container {
                padding-top: 7px !important;
                margin-top: 7px !important;
            }
            .song-title {
                font-size: 18px;
                font-weight: bold;
                color: #ecf0f1;
                text-shadow: 3px 3px 6px rgba(0,0,0,0.7), 0 0 10px rgba(255, 255, 255, 0.6);
            }
            .stButton button {
                padding: 10px 30px !important;
                border-radius: 15px !important;
                margin: 10px auto !important;
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
            }
            .feedback-container {
                margin-top: 20px;
                background: #222;
                padding: 10px;
                border-radius: 10px;
                text-align: center;
            }

            .st-key-like button:hover {
                background-color: green;
                background-blend-mode: overlay;
            }

            .st-key-dislike button:hover {
                background-color: red;
                background-blend-mode: overlay;
            }
            img {
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                margin: auto;
                display: flex;
                flex-direction: column;
            }
            </style>

            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <div class="container">
                <div class="song-title">{current_song}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        image_path = f"classification_songs_images/{current_song}.jpeg"
        col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

        with col2:
            image_path = f"classification_songs_images/{current_song}.jpeg"
            st.image(image_path, use_container_width=True)

        audio_path = f"‏‏classification_songs_audio/{current_song}.mp3"
        audio_file = open(audio_path, "rb").read()
        st.audio(audio_file, format="audio/aac")

        def handle_like():
            st.session_state.song_feedback[current_song] = "Like"
            st.session_state.current_song_index += 1
            if st.session_state.current_song_index >= len(songs_df):
                st.session_state.page = "persona_choose"

        def handle_dislike():
            st.session_state.song_feedback[current_song] = "Dislike"
            st.session_state.current_song_index += 1
            if st.session_state.current_song_index >= len(songs_df):
                st.session_state.page = "persona_choose"

        col1, col2, col3 = st.columns(3)

        with col1:
            st.button("👎", key="dislike", on_click=handle_dislike)

        with col3:
            st.button("👍", key="like", on_click=handle_like)

        st.markdown("Your Feedback So Far:")
        if "song_feedback" in st.session_state:
            for song, feedback in st.session_state.song_feedback.items():
                st.write(f"🎵 **{song}**: {feedback}")
        else:
            st.write("No feedback recorded yet.")

