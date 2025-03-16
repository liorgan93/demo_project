import streamlit as st
import pandas as pd
from Intro import set_background
import time

def get_songs_by_persona(persona_name):
    set_background("other images/Backround.webp")
    df = pd.read_csv('playlists_excel/personas_songs.csv')
    songs = df[df['persona'] == persona_name]['song'].tolist()
    return songs

def songs_persona_like_page():
    songs_list = get_songs_by_persona(st.session_state.persona)

    if "song_index" not in st.session_state:
        st.session_state.song_index = 0

    current_index = st.session_state.song_index

    if current_index >= len(songs_list):
        st.session_state.page = "method_choose"
        st.rerun()
    else:
        song_title = songs_list[current_index]
        st.markdown(
            """
            <style>
            .container {
                background: linear-gradient(90deg, #3b5998, #4a69bd); 
                color: white;
                border-radius: 25px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
                max-width: 500px;
                margin: 20px auto;
                font-family: Arial, sans-serif;
                font-size: 22px;
                border: 3px solid #a0c4ff;
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
            
            .st-key-know_song button:hover {
                    background-color: green;
                    background-blend-mode: overlay;
                }
                
            .st-key-dont_know_song button:hover {
                background-color: red;
                background-blend-mode: overlay;
                }
                
            .feedback-container {
                margin-top: 20px;
                background: #222;
                padding: 10px;
                border-radius: 10px;
                text-align: center;
            }
            
            img {
                border-radius: 15px;
                width: 500px; 
                height: 250px; 
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                display: block;
                margin: auto;
            }
            
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class=\"container\">
                <div class=\"song-title\">{song_title}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Load image
        col1, col2, col3 = st.columns([1, 5, 1])

        with col2:
            image_path = f"‏‏personas_songs_images/{song_title}.jpg"
            st.image(image_path, use_container_width=True)


        audio_path = f"personas_songs_audio/{song_title}.mp3"
        audio_file = open(audio_path, "rb").read()
        st.audio(audio_file, format="audio/aac")


        def handle_know_song():
            st.session_state.song_index += 1

        def handle_dont_know_song():
            st.session_state.song_index += 1

        col1, col2, col3 = st.columns(3)

        with col1:
            st.button("❌", key="dont_know_song", on_click=handle_dont_know_song)

        with col3:
            st.button("✅", key="know_song", on_click=handle_know_song)

