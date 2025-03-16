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

def Intro_know_or_dont_page():
    set_background("other images/Backround.webp")

    st.markdown(
        """
        <style>
        .container {
            background: linear-gradient(135deg, #2a5ba8, #4c82c7, #3b6fb3);
            color: white;
            border-radius: 25px;
            padding: 25px;
            padding-bottom: 10px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            max-width: 450px;
            margin: auto;
            font-family: 'Poppins', sans-serif;
        }
        .header {
            font-size: 26px;
            font-weight: 600;
            margin-bottom: 20px;
            color: #ffffff;
        }
        .header-small {
            font-size: 14.5px;
            font-weight: 700;
            color: #FFFFFF; /* טקסט לבן */
            background-color: rgba(94, 35, 157, 0.8); /* רקע סגול חצי שקוף */
            padding: 2px 6px; /* ריפוד פנימי כדי לתת לתיבה גודל */
            border-radius: 5px; /* עיגול פינות לרקע */
        }
        .block-container {
            padding-top: 25px !important;
            margin-top: 25px !important;
        }
        .header-main {
            font-size: 18px;
            font-weight: 600;
            color: #ffffff;
            font-family: 'Arial', sans-serif; /* גופן מובדל */
            margin-bottom: 12px;
        }
        .sub-header {
            font-size: 16px;
            font-weight: 500;
            color: #ffffff;
            font-family: 'Verdana', sans-serif; /* גופן שונה להדגשה */
            margin-bottom: 15px;
        }
        .description {
            font-size: 20px;
            font-weight: 400;
            margin-top: 20px;
            color: #ffffff;
        }
        .green-text {
            color: #50c878;
            font-weight: 600;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.9);
        }
        .red-text {
            color: #FF4747; 
            font-weight: 600;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.9);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    persona_name = st.session_state.persona

    st.markdown(f"""
        <div class="container">
            <div class="header-small">Soon, you'll be recommending songs for your new friend!</div>
            <div class="header-main">But first, let’s get familiar with {persona_name}</div>
            <div class="header"> Know or Don't Know? </div>
            <div class="sub-header">We’ll now show you  <strong> songs that {persona_name} likes </strong>. Listen to them to get to know {persona_name} better and select if you know or don’t know each one.</div>
            <div class="description">
                <span class="green-text">Know this song?</span> Tap ✅<br>
                <span class="red-text">Never heard of it?</span> Tap ❌
            </div>
        </div>
    """, unsafe_allow_html=True)


    def handle_start_click():
        st.session_state.page = "songs_persona_like"

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("Let's go!", key="continue-btn", on_click=handle_start_click, use_container_width=True)

