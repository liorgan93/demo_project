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
                padding: 8px 25px !important;
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

            .st-key-like button {
                background-color: #32CD32;
                background-blend-mode: overlay;
                transition: background-color 0.3s ease;

            }

            .st-key-dislike button {
                background-color: red;
                background-blend-mode: overlay;
                transition: background-color 0.3s ease;

            }
            .st-key-like button:hover {
                background-color: #008000;
                background-blend-mode: overlay;

            }
            .st-key-dislike button:hover {
                background-color: #B22222;
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

