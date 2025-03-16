import streamlit as st
import base64
import time

def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
        page_background = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpeg;base64,{encoded_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #FFFFFF;
        }}
        </style>
        """
        st.markdown(page_background, unsafe_allow_html=True)

def Intro_page():
    time.sleep(0.5)
    set_background("other images/Backround.webp")

    st.markdown(
        """
        <style>
        .container {
            background: linear-gradient(135deg, #2a5ba8, #4c82c7, #3b6fb3);
            color: white;
            border-radius: 25px;
            padding: 8px;
            padding-bottom: 10px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            max-width: 400px;
            margin: auto;
            font-family: 'Poppins', sans-serif;
        }
        .block-container {
            padding-top: 25px !important;
            margin-top: 25px !important;
        }
        .header {
            font-size: 26px;
            font-weight: 600;
            margin-bottom: 20px;
            color: #ffffff;
        }
        .description {
            font-size: 22px;
            font-weight: 300;
            margin-bottom: 20px;
            color: #ffffff;
        }
        .footer {
            font-size: 16px;
            margin-top: 20px;
            color: #ffffff;
        }
        .green-text {
            color: #008000; 
            font-weight: 600;
        }
        .red-text {
            color: red; 
            font-weight: 600;
        }
        </style>
        <div class="container">
            <div class="header"> Like or Dislike? <br> Let's explore your music taste! </div>
            <div class="description">
                <span class="green-text">Like the song?</span> ?&nbsp;&nbsp;Tap 👍 <br>
                <span class="red-text">Not your vibe?</span> ?&nbsp;&nbsp;Tap 👎
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    def handle_start_click():
        st.session_state.page = "song_user_classification"

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("Let's go!", key="start-btn", on_click=handle_start_click, use_container_width=True)