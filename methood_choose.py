import streamlit as st
import base64
import time
def click_a():
    st.session_state.page = "top_k_choose"

def click_b():
    st.session_state.page = "top_k_choose"

def click_c():
    st.session_state.page = "top_k_choose"

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def method_choose_page():
    from Intro import set_background
    set_background("other images/Backround.webp")

    record_topk = get_base64_image("a.jpg")
    record_personalization = get_base64_image("b.webp")
    record_advanced = get_base64_image("c.webp")

    # Main Title with a solid background for readability
    st.markdown("""
        <div style='background-color: rgba(0, 0, 50, 0.99); padding: 20px; border-radius: 10px;'>
            <h1 style='text-align: center; color: #8A2BE2; font-family: "Comic Sans MS", cursive;'>🎵 Demo - The World of Music Recommendations 🎧</h1>
            <h3 style='text-align: center; color: #ADD8E6;'>Choose your record and start playing! 🎶</h3>
        </div>
    """, unsafe_allow_html=True)

    # Styling with CSS
    st.markdown("""
        <style>
        .st-key-aa button, .st-key-bb button, .st-key-cc button {
            width: 150px;
            height: 150px;
            background-color: transparent;
            border: none;
            cursor: pointer;
            border-radius: 50%;
            transition: transform 0.6s ease-in-out, box-shadow 0.3s;
            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.5);
            margin: auto;
            display: flex;
            flex-direction: column;


        }
        .st-key-aa button:hover, .st-key-bb button:hover, .st-key-cc button:hover {
            transform: rotate(360deg) scale(1.1);
            box-shadow: 0px 0px 30px rgba(255, 255, 255, 0.8);
        }
        .st-key-aa button {
            background-image: url('data:image/webp;base64,""" + record_topk + """');
            background-size: cover;
            background-position: center;
        }
        .st-key-bb button {
            background-image: url('data:image/webp;base64,""" + record_personalization + """');
            background-size: cover;
            background-position: center;
        }
        .st-key-cc button {
            background-image: url('data:image/webp;base64,""" + record_advanced + """');
            background-size: cover;
            background-position: center;
        }
        .selected-page {
            background-color: rgba(50, 0, 100, 0.8);
            padding: 10px;
            border-radius: 10px;
            color: #E6E6FA;
            text-align: center;
            font-size: 18px;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])

    with col2:
        st.button("", key="aa", on_click=click_a, use_container_width=True)
        st.button("", key="bb", on_click=click_b, use_container_width=True)
        st.button("", key="cc", on_click=click_c, use_container_width=True)