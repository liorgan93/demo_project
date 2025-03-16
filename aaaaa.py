import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Select Your Songs", layout="wide")

def top_k_choose_page():
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
            padding: 0px; /* הפחתת הפדינג */
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 1px; /* ביטול רווחים מיותרים */
            margin-top: 1px; /* מוסיף רווח מהחלק העליון */
        }

        /* כותרת עליונה - קטנה יותר עם יותר רווח למעלה */
        .custom-container h3 {
            font-size: 18px;
            margin-top: 15px;
        }

        /* Expander דחוס יותר */
        div[data-testid="stExpander"] {
            background: linear-gradient(135deg, rgba(30, 30, 80, 0.97), rgba(50, 50, 110, 0.97));
            color: white !important;
            border-radius: 8px !important;
            margin-bottom: 2px !important; /* רווח מינימלי */
            padding: 3px !important; /* פחות padding */
        }

        /* צמצום התוכן של ה-expander */
        div[data-testid="stExpander"] div.streamlit-expanderContent {
            background: rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            padding: 3px !important;
            border-radius: 8px !important;
            font-size: 14px; /* גופן קטן יותר */
        }

        /* כותרת בתוך ה-expander קטנה יותר */
        div[data-testid="stExpander"] summary {
            font-size: 14px !important;
            padding: 3px !important;
        }

        /* צמצום מרווחים בין האלמנטים בעמודות */
        div.st-emotion-cache-1fcmnav {
            padding: 0px !important;
            margin: 0px !important;
        }

        /* עיצוב כפתור */
        .stButton > button {
            display: block;
            margin-left: auto;
            margin-right: auto;
            background-color: #4CAF50;
            color: white;
            border-radius: 15px;
            padding: 5px 15px; /* כפתור יותר קטן */
            font-size: 14px;
        }

        .stButton > button:hover {
            background-color: #45a049;
        }

    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown(f"<div class='custom-container'><h3>Recommend to {persona_name} the Top 3 songs 🎵</h3></div>", unsafe_allow_html=True)

        selected_songs = st.multiselect("", songs_data["song"].tolist(), max_selections=3)

        if "error_msg" not in st.session_state:
            st.session_state.error_msg = ""

        def handle_confirm_click():
            if len(selected_songs) != 3:
                st.session_state.error_msg = "You must select exactly 3 songs before continuing."
            else:
                st.session_state.page = "compare_lists"
                st.session_state.user_choice = selected_songs

        st.button("Confirm", key="confirm_button", on_click=handle_confirm_click)

        if st.session_state.error_msg:
            st.error(st.session_state.error_msg)

    cols = st.columns(3, gap="small")


    # נתיב לתיקיית האודיו
    audio_folder = "top_k_songs_audio"

    # נניח ש-songs_data הוא DataFrame עם עמודה 'song' שמכילה את שמות השירים
    for idx, row in songs_data.iterrows():
        song_name = row["song"]
        audio_path = os.path.join(audio_folder, f"{song_name}.mp3")

        # יש לוודא שהנתיב נגיש דרך השרת
        if os.path.exists(audio_path):
            audio_url = f"/tmp/{song_name}.mp3"  # נתיב שייחשף דרך Streamlit
            os.system(f"cp {audio_path} /tmp/{song_name}.mp3")  # העתקת הקובץ לתיקיית זמנית

            audio_html = f"""
            <audio controls style="width: 100%; height: 30px;">
                <source src="{audio_url}" type="audio/mpeg">
                הדפדפן שלך לא תומך בהשמעת אודיו.
            </audio>
            """
            with st.expander(f"🎧 Listen to {song_name}"):
                components.html(audio_html, height=40)
        else:
            st.error(f"Could not load audio for {song_name}.")

