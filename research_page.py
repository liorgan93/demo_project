import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read()).decode()

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

def research_page():
    persona_name = st.session_state.persona
    set_background("other images/Background.webp")

    st.markdown(
        """
        <style>
        .container {
            background: linear-gradient(135deg, rgba(42, 91, 168, 0.97), rgba(76, 130, 199, 0.97), rgba(59, 111, 179, 0.97));
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

    st.markdown(f"""<div class="container">
                <div class="header">You’ve just explored {persona_name}’s favorite music.<br>Did you feel a connection to their musical taste?</div>
            </div>""", unsafe_allow_html=True)

    st.divider()

    def handle_start_click():
        st.session_state.page = "song_user_classification"

    lets_go = get_base64_image("other images/lets go.png")
    st.markdown("""
            <style>
            .st-key-lets_go button{
                width: 130px;
                height: 130px;
                background-color: transparent;
                border: none;
                cursor: pointer;
                border-radius: 50%;
                transition: transform 0.6s ease-in-out, box-shadow 0.3s;
                box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.5);
                background-image: url('data:image/webp;base64,""" + lets_go + """');
                background-size: cover;
                margin: auto;
                display: flex;
                flex-direction: column;

            }
            .st-key-lets_go button:hover {
                transform: rotate(360deg) scale(1.1);
                box-shadow: 0px 0px 30px rgba(255, 255, 255, 0.8);
            }
            </style>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col3:
        st.button("No – it wasn’t quite my vibe 🙅‍♂️ ", key="dont_know")

    with col1:
        st.button("Yes – I really liked it 🎧 ", key="know")


