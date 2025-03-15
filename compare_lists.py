import streamlit as st
import pandas as pd

def compare_lists_page():
    selected_songs = st.session_state.user_choice
    algorithm_df = pd.read_excel("alg_results.xlsx")

    if 'top_k' not in algorithm_df.columns:
        st.error("Error: The file must contain a 'top_k' column.")
        return

    algorithm_songs = sorted(set(algorithm_df['top_k'].dropna().tolist()))
    user_songs = sorted(set(selected_songs))

    matching_songs = sorted(set(user_songs).intersection(set(algorithm_songs)))
    non_matching_user_songs = sorted(set(user_songs) - set(algorithm_songs))
    non_matching_algorithm_songs = sorted(set(algorithm_songs) - set(user_songs))

    total_matches = len(matching_songs)
    total_possible = max(len(user_songs), len(algorithm_songs))
    match_percentage = (total_matches / total_possible) * 100 if total_possible > 0 else 0

    # Ensuring all lists are of the same length without extra empty row
    max_length = max(len(matching_songs) + len(non_matching_user_songs), len(matching_songs) + len(non_matching_algorithm_songs))
    user_column = matching_songs + non_matching_user_songs + [""] * (max_length - len(matching_songs) - len(non_matching_user_songs))
    algorithm_column = matching_songs + non_matching_algorithm_songs + [""] * (max_length - len(matching_songs) - len(non_matching_algorithm_songs))

    # Create the DataFrame
    comparison_df = pd.DataFrame({
        "User's Choice": user_column,
        "Algorithm's Choice": algorithm_column
    })

    # CSS for styling
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            width: 100vw;
            overflow-x: hidden;
            padding: 0;
        }
        .center-text {
            text-align: center;
        }
        .stDataFrame {
            max-width: 100%;
        }
        .success-text {
            color: #4CAF50;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
        .failure-text {
            color: #E53935;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="center-text">🎵 Your Selections vs. Algorithm\'s Picks</h1>', unsafe_allow_html=True)
    st.markdown(
        '<h3 class="center-text">Here\'s a direct comparison of your song choices and what the algorithm picked for you:</h3>',
        unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
    with col2:
        st.subheader(f"✅ Matches: {total_matches}/{total_possible}")
        st.dataframe(comparison_df, hide_index=True, use_container_width=True)

    if match_percentage >= 50:
        st.markdown('<p class="success-text">Great match! You and the algorithm think alike! 🎉</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="failure-text">Not a great match... Maybe next time! ❌</p>', unsafe_allow_html=True)