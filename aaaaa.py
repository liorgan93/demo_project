import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Songs Demo", layout="wide")

def page_with_fixed_columns():
    from Intro import set_background
    set_background("other images/Backround.webp")

    audio_folder = "top_k_songs_audio"
    csv_file_path = "playlists_excel/top_k_songs.csv"
    songs_data = pd.read_csv(csv_file_path)

    persona_name = "dddddd"

    st.markdown(f"<h1 style='text-align:center;'>Recommend songs to {persona_name} 🎵</h1>", unsafe_allow_html=True)

    selected_songs = st.multiselect("Select exactly 3 songs:", songs_data["song"].tolist(), max_selections=3)

    # פתרון CSS לבעיה שלך:
    st.markdown("""
        <style>
            @media (max-width: 768px) {
                div[data-testid="column"] {
                    width: unset !important;
                    flex-direction: row !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for idx, row in songs_data.iterrows():
        song_name = row["song"]
        audio_path = os.path.join(audio_folder, f"{song_name}.mp3")

        with cols[idx % 3]:
            st.markdown(f"<h4>🎵 {song_name}</h4>", unsafe_allow_html=True)

            try:
                audio_file = open(audio_path, "rb").read()
                st.audio(audio_file, format="audio/mp3")
            except FileNotFoundError:
                st.error(f"Audio for {song_name} not found.")

    def handle_confirm_click():
        if len(selected_songs) != 3:
            st.error("You must select exactly 3 songs before continuing.")
        else:
            st.session_state.page = "compare_lists"
            st.session_state.user_choice = selected_songs

    st.button("Confirm", key="confirm_button", on_click=handle_confirm_click)

