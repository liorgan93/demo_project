import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components
import base64
import time

def top_k_choose_page():
    st.set_page_config(page_title="Select Your Songs", layout="wide")
    from Intro import set_background
    set_background("other images/Backround.webp")

    audio_folder = "top_k_songs_audio"
    csv_file_path = "playlists_excel/top_k_songs.csv"
    songs_data = pd.read_csv(csv_file_path)

    persona_name = "kkkkkkkk"

    st.markdown("""
    <style>

        .block-container {
            padding-top: 20px !important;
            padding-bottom: 2px !important;
            margin: 0px !important;
        }

        .custom-container {
            background: linear-gradient(135deg, rgba(30, 30, 80, 0.97), rgba(50, 50, 110, 0.97));
            padding: 0px; 
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 1px;
            margin-top: 1px; 
        }

        .custom-container h3 {
            font-size: 18px;
            margin-top: 15px;
        }

        div[data-testid="stExpander"] {
            min-width: 100% !important;
            background: linear-gradient(135deg, rgba(30, 30, 80, 1), rgba(50, 50, 110, 1));
            color: white !important;
            border-radius: 8px !important;
            margin-bottom: 2px !important; /* רווח מינימלי */
            padding: 3px !important; /* פחות padding */
        }

        div[data-testid="stExpander"] div.streamlit-expanderContent {
            min-width: 100% !important;
            background: rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            padding: 3px !important;
            border-radius: 8px !important;
        }

        div[data-testid="stExpander"] summary {
            min-width: 100% !important;
            font-size: 14px !important;
            padding: 5px !important;
        }

        .stButton button {
            width: 100%;
            font-size: 18px;
            padding: 8px;
            border-radius: 15px;
            background-color: #800080;
            color: white;
            border: 1px solid black;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 10px;
        }

        .stButton button:hover {
            background-color: #660066;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown(f"<div class='custom-container'><h3>Recommend to {persona_name} the Top 3 songs 🎵</h3></div>", unsafe_allow_html=True)


        if "error_msg" not in st.session_state:
            st.session_state.error_msg = ""

        def handle_confirm_click():
            if len(selected_songs) != 3:
                st.session_state.error_msg = "You must select exactly 3 songs before continuing."
            else:
                st.session_state.page = "compare_lists"
                st.session_state.user_choice = selected_songs

        col_next = st.columns([1, 1, 1])
        with col_next[1]:
            selected_songs = st.multiselect("", songs_data["song"].tolist(), max_selections=3)

            st.button("Confirm", key="confirm_button", on_click=handle_confirm_click, use_container_width=True)

        if st.session_state.error_msg:
            st.error(st.session_state.error_msg)

    cols = st.columns(3, gap="small")

    def encode_audio(audio_path):
        try:
            with open(audio_path, "rb") as audio_file:
                encoded_audio = base64.b64encode(audio_file.read()).decode()
            return encoded_audio
        except FileNotFoundError:
            return None

    for idx, row in songs_data.iterrows():
        song_name = row["song"]
        audio_path = os.path.join(audio_folder, f"{song_name}.mp3")

        with cols[idx % 3]:
            with st.expander(f"🎧 Listen to - {song_name}"):
                audio_base64 = encode_audio(audio_path)

                if audio_base64:
                    audio_html = f"""
                    <audio controls style="width: 100%; height: 30px;">
                        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mpeg">
                        הדפדפן שלך לא תומך בהשמעת אודיו.
                    </audio>
                    """
                    components.html(audio_html, height=40)  # הקטנת גובה נוסף
                else:
                    st.error(f"Could not load audio for {song_name}.")
