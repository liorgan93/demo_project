import streamlit as st
import pandas as pd
import os
import base64
import time

st.set_page_config(page_title="Select Your Songs", layout="wide")

def top_k_choose_page():
    from Intro import set_background
    set_background("other images/Backround.webp")

    images_folder = "‏‏top_k_songs_images"
    audio_folder = "top_k_songs_audio"
    csv_file_path = "playlists_excel/top_k_songs.csv"
    songs_data = pd.read_csv(csv_file_path)

    st.markdown(
        """
        <style>
            body {
                background-color: #f5f5f5;
                color: #333333;
            }
            .song-card {
                background: #ffffff;
                border-radius: 20px;
                padding: 15px;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s;
            }
            .song-card:hover {
                transform: scale(1.05);
            }
            .song-title {
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            .song-audio {
                margin-top: 10px;
            }
            .multiselect-container {
                margin-bottom: 20px;
            }
            .confirm-button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 20px;
                cursor: pointer;
                font-size: 16px;
            }
            .confirm-button:hover {
                background-color: #45a049;
            }
            img {
                object-fit: cover;
                width: 300px; 
                height: 300px;
                border-radius: 25px; 
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    persona_name = st.session_state.persona
    st.markdown(f"<h1 style='text-align: center;'>Recommend to {persona_name} the Top 3 songs that you think he would like 🎵</h1>", unsafe_allow_html=True)

    if "error_msg" not in st.session_state:
        st.session_state.error_msg = ""

    selected_songs = st.multiselect("",songs_data["song"].tolist(),max_selections=3)

    cols = st.columns(3)
    for idx, row in songs_data.iterrows():
        song_name = row["song"]
        image_path = os.path.join(images_folder, f"{song_name}.jpg")
        audio_path = os.path.join(audio_folder, f"{song_name}.mp3")

        with cols[idx % 3]:
            st.markdown(
                f"""
                <div style='display: flex; justify-content: center;'>
                    <img src='data:image/jpeg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}' 
                    style='width:300px;height:300px;border-radius:25px;'/>
                </div>
                """,
                unsafe_allow_html=True
            )

            try:
                audio_file = open(audio_path, "rb").read()
                st.audio(audio_file, format="audio/aac")
            except FileNotFoundError:
                st.error(f"Could not load audio for {song_name}.")

    def handle_confirm_click():
        if len(selected_songs) != 3:
            st.session_state.error_msg = "You must select exactly 3 songs before continuing."
        else:
            st.session_state.page = "compare_lists"
            st.session_state.user_choice = selected_songs

    st.button("Confirm", key="confirm_button", on_click=handle_confirm_click)

    if st.session_state.error_msg:
        st.error(st.session_state.error_msg)

    st.markdown(
        """
        <style>
            .stButton > button {
                display: block;
                margin-left: auto;
                margin-right: auto;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
