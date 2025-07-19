import json
import os
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load config with API key
with open(os.path.join(current_dir, "config.json"), "r", encoding="utf-8") as f:
    config = json.load(f)

api_key = config["OMDB_API_KEY"]  # This is the correct variable name

# Streamlit page settings
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommender")

# Load movie list
movie_list = sorted(df['title'].dropna().unique())
selected_movie = st.selectbox("🎬 Select a movie:", movie_list)

# Recommendation logic
if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend_movies(selected_movie)
        if recommendations is None or recommendations.empty:
            st.warning("Sorry, no recommendations found.")
        else:
            st.success("Top similar movies:")
            for _, row in recommendations.iterrows():
                movie_title = row['title']
                plot, poster = get_movie_details(movie_title, api_key) 

                with st.container():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if poster != "N/A":
                            st.image(poster, width=100)
                        else:
                            st.write("❌ No Poster Found")
                    with col2:
                        st.markdown(f"### {movie_title}")
                        st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")
