import streamlit as st
import random
import time

def button_click():
    st.session_state.page = "Intro_know_or_dont"

def persona_choose_page():
    time.sleep(0.5)
    from Intro import set_background
    set_background("other images/Backround.webp")
    people = [
        {
            "name": "John",
            "image": "persona_A.jpg",
        },
        {
            "name": "Bob",
            "image": "persona_B.jpg",
        },
        {
            "name": "Alice",
            "image": "persona_C.jpg",
        },
    ]

    chosen_person = random.choice(people)
    if "persona" not in st.session_state:
        st.session_state.persona = chosen_person["name"]

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
            max-width: 100%;
            width: 630px;
            height: 350px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease-in-out;
            }

        img:hover {
            transform: scale(1.05);
        }

        .stButton button {
            width: 100%;
            font-size: 18px;
            padding: 15px;
            border-radius: 15px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 10px;
        }

        .stButton button:hover {
            background-color: #45a049;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
            <div class="container">
                <div class="title">Meet {chosen_person['name']}!</div>
                <div class="sub_title"> based on your musical taste you can be friends! </div>
            </div>
            """,
        unsafe_allow_html=True,
    )

    try:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(f"personas_images/{chosen_person['image']}", use_container_width=True)
    except FileNotFoundError:
        st.error(f"Could not load the image for {chosen_person['name']}. Please check the file path.")


    col_next = st.columns([1, 1, 1])
    with col_next[1]:
        st.button("Next", key="songs_persona_like", on_click=button_click, use_container_width=True)
