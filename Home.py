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
            padding: 7px;
            box-shadow: 0px 0px 20px rgba(0, 0, 100, 0.8);
            text-align: center;
            margin: auto;
            width: 90%;
            max-width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow-x: hidden;
        }}
        .block-container {{
            padding-top: 25px !important;
            margin-top: 25px !important;
        }}
        .title-text {{
            font-size: 19px !important;
            font-weight: bold;
            text-shadow: 4px 4px 15px rgba(0,150,255,0.9);
            color: #B3E5FC;
        }}
        .subtitle-text {{
            font-size: 16px !important;
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
            <p class="subtitle-text">In this demo, you’ll recommend songs for someone, and we’ll compare your picks to Algorithm Y’s suggestions to demonstrate its performance. Let’s see how your intuition compares to data-driven recommendations!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    start = get_base64_image("other images/start.png")

    st.snow()

    st.markdown("""
        <style>
        .st-key-start_button button{
            width: 110px;
            height: 110px;
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
            .column-box {
                border: 2px dashed lightblue;
                padding: 10px;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # יצירת עמודות עם גבולות ויזואליים
    col1, col2, col3 = st.columns([0.1, 0.1, 0.8])  # מחלקים את המסך לשני חלקים שווים

    with col1:
        st.markdown('<div class="column-box">📦 עמודה 1</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="column-box">📦 עמודה 2</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="column-box">📦 עמודה 3</div>', unsafe_allow_html=True)

    with col1:
        if st.button("👍 Like"):
            st.write("You liked the song!")

    with col2:
        if st.button("👎 Dislike"):
            st.write("You disliked the song!")








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