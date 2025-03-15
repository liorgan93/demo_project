import streamlit as st
import base64
from Intro import set_background


def get_base64_image(image_path):
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read()).decode()


def home_page():
    def click_button():
        st.session_state.page = "Intro"

    set_background("other images/Backround.webp")

    image_base64 = get_base64_image("other images/Music_notes.png")

    st.markdown(
        f"""
        <style>
        .container {{
            background: linear-gradient(135deg, rgba(10, 10, 40, 0.9), rgba(20, 20, 60, 0.95));
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0px 0px 20px rgba(0, 0, 100, 0.8);
            text-align: center;
            margin: auto;
            width: 80%;
            max-width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow-x: hidden;
        }}
        .title-text {{
            font-size: 64px;
            font-weight: bold;
            text-shadow: 4px 4px 15px rgba(0,150,255,0.9);
            color: #B3E5FC;
        }}
        .subtitle-text {{
            font-size: 28px;
            text-shadow: 2px 2px 10px rgba(173,216,230,0.8);
            color: #81D4FA;
            margin-bottom: 20px;
        }}
        .treble-clef {{
            margin-bottom: 0px;
            max-width: 100%;
        }}
        </style>
        <div class="container">
            <img src="data:image/webp;base64,{image_base64}" alt="Opening Image" class="treble-clef">
            <p class="title-text">🎶 Welcome to the Music Recommendation Experience 🎶</p>
            <p class="subtitle-text">Demonstrating the performance of Algorithm Y for music recommendation systems. This comparison between human intuition and data-driven solutions will be done by analyzing the differences between your song choices and the algorithm’s recommendations based on Spotify data</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    start = get_base64_image("other images/start.png")

    st.markdown("""
        <style>
        .st-key-start_button button{
            width: 150px;
            height: 150px;
            background-color: transparent;
            border: none;
            cursor: pointer;
            border-radius: 50%;
            transition: transform 0.6s ease-in-out, box-shadow 0.3s;
            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.5);
            background-image: url('data:image/webp;base64,""" + start + """');
            background-size: cover;
            margin: auto;
            display: flex;
            flex-direction: column;

        }
        .st-key-start_button button:hover {
            transform: rotate(360deg) scale(1.1);
            box-shadow: 0px 0px 30px rgba(255, 255, 255, 0.8);
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        st.button("", key="start_button", on_click=click_button)


    st.markdown("""
        <style>
        .button-container {
            display: flex;
            gap: 0px;
            align-items: center;
        }
        .stButton > button {
            margin: 0px !important;
            padding: 0px 0px;
            border-radius: 0;
        }
        .stButton {
            flex-grow: 1;
        }
        </style>
        """, unsafe_allow_html=True)

    # שימוש ב-st.columns עם קונפיגורציה מדויקת כדי למנוע רווחים
    col1, col2, col3 = st.columns([1, 1,15])

    with col1:
        btn1 = st.button("A", key="btn1")

    with col2:
        btn2 = st.button("B", key="btn2")







if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "Intro":
    from Intro import Intro_page
    Intro_page()
elif st.session_state.page == "song_user_classification":
    from song_user_classification import song_user_classification_page
    song_user_classification_page()
elif st.session_state.page == "persona_choose":
    from persona_choose import persona_choose_page
    persona_choose_page()
elif st.session_state.page == "Intro_know_or_dont":
    from Intro_know_or_dont import Intro_know_or_dont_page
    Intro_know_or_dont_page()
elif st.session_state.page == "songs_persona_like":
    from songs_persona_like import songs_persona_like_page
    songs_persona_like_page()
elif st.session_state.page == "method_choose":
    from methood_choose import method_choose_page
    method_choose_page()
elif st.session_state.page == "top_k_choose":
    from top_k_choose import top_k_choose_page
    top_k_choose_page()
elif st.session_state.page == "compare_lists":
    from compare_lists import compare_lists_page
    compare_lists_page()
elif st.session_state.page == "thank_you":
    from thank_you import thank_you_page
    thank_you_page()