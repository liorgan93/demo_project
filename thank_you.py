import streamlit as st
from Intro import set_background
import time

# Mobile-friendly "Thank You" page with enhanced styling
def thank_you_page():
    time.sleep(0.5)
    set_background("other images/Backround.webp")
    st.markdown(
        """
        <style>
            .flipped-emoji {
                display: inline-block;
                transform: scaleX(-1);
            }

            .thank-you-container {
                font-family: 'Helvetica Neue', Arial, sans-serif;
                text-align: center;
                padding-top: 60px;
                padding-bottom: 60px;
                background: linear-gradient(135deg, rgba(225, 200, 255, 0.95), rgba(200, 220, 255, 0.95));
                border-radius: 30px;
                max-width: 90%;
                margin: auto;
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
            }
            .thank-you-title {
                font-size: 35px;
                font-weight: bold;
                color: #222;
                margin-bottom: 15px;
            }
            .thank-you-message {
                font-size: 20px;
                color: #444;
                margin-bottom: 25px;
                padding: 0 15px;
            }
            .download-button a {
                display: inline-block;
                text-decoration: none;
                background-color: #1E90FF;
                color: white;
                padding: 12px 25px;
                border-radius: 25px;
                font-size: 16px;
                transition: background-color 0.3s;
            }
            .download-button a:hover {
                background-color: #1C86EE;
            }
        </style>
        <div class="thank-you-container">
        <div class="thank-you-title">
            🎉 Thank You for Participating! <span class="flipped-emoji">🎉</span>
        </div>
            <div class="thank-you-message">
                We appreciate your time and hope you enjoyed the demo. If you'd like to To learn more about the methods demonstrated in this demo, You're welcome to download the paper below!
            </div>
            <div class="download-button">
                <a href="top_k_songs.csv" download>⬇️ Download Paper (PDF)</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )