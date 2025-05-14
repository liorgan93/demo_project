import streamlit as st
import pandas as pd
import time
import ast
from Intro import set_background
from classsification_functions import classify_user_by_preferences



def button_click():
    st.session_state.page = "Intro_know_or_dont"

def persona_choose_page():
    placeholder = st.empty()
    placeholder.empty()
    time.sleep(8)
    set_background("other images/Background.webp")
    st.session_state.songs_df['like/dislike'] = st.session_state.song_feedback
    st.session_state.songs_df['weights'] = st.session_state.songs_df['weights'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    st.session_state.chosen_person_number, scores = classify_user_by_preferences(st.session_state.songs_df)
    if "persona" not in st.session_state:
        names = pd.read_csv("playlists_excel/names.csv")
        names_list = names[names["cluster"] == st.session_state.chosen_person_number]["name"].tolist()
        st.session_state.persona = ", ".join(names_list)

    st.markdown(
        """
        <style>
        body {
            background-color: #f7f7f7;
            font-family: 'Arial', sans-serif;
            color: #333;
            margin: 0;
            padding: 0;
        }

        .container {
            background-color: #ffffff;
            border-radius: 30px;
            padding: 1px;
            text-align: center;
            font-family: Arial, sans-serif;
            width: 80%;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        .block-container {
            padding-top: 20px !important;
            margin-top: 20px !important;
            padding-bottom: 0px !important;
            margin-bottom: 0px !important;
        }

        .title {
            font-size: 30px;
            font-weight: 900;
            background: linear-gradient(to bottom, #000000, #222222, #444444); /* שחור עם עומק */
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 
                2px 2px 5px rgba(0, 0, 0, 0.3), 
                4px 4px 10px rgba(0, 0, 0, 0.2); /* הוספת ברק */
        }

        .sub_title {
            font-size: 15px;
            color: black;
            font-weight: bold;
            margin-bottom: 15px;
            letter-spacing: 2px;
        }

        img {
            border-radius: 15px;
            max-height: 40vh;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease-in-out;
            margin-bottom: 0px;
            }

        img:hover {
            transform: scale(1.05);
        }

        .stButton button {
            width: 100%;
            font-size: 18px;
            padding: 15px;
            border-radius: 15px;
            background-color: #800080;
            color: white;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 0px !important;
        }

        .stButton button:hover {
            background-color: #660066;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
            <div class="container">
                <div class="title">Meet {st.session_state.persona}!</div>
                <div class="sub_title"> based on your musical taste you can be friends! </div>
            </div>
            """,
        unsafe_allow_html=True,
    )

    try:
        col1, col2, col3 = st.columns([0.3, 0.4, 0.3])
        with col2:
            st.image(f"personas_images/{st.session_state.persona}.jpg", use_container_width=True)
    except FileNotFoundError:
        st.error(f"Could not load the image for {st.session_state.persona}. Please check the file path.")


    col_next = st.columns([1, 1, 1])
    with col_next[1]:
        st.button("Next", key="songs_persona_like", on_click=button_click, use_container_width=True)
