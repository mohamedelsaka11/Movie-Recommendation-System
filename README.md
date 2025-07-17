# 🎬 Movie Recommender System

A content-based movie recommendation system built with Python, Streamlit, and scikit-learn. Given a movie title, the app suggests similar movies along with their posters and plots using the OMDb API.

## 📌 Features

- Recommend similar movies based on text similarity (TF-IDF & cosine similarity)
- Show movie poster and plot using OMDb API
- Easy-to-use Streamlit interface
- Preprocessed and cleaned dataset for better results

## 🧠 How It Works

1. **Data Preprocessing:** Clean and prepare the dataset using pandas and scikit-learn.
2. **Feature Extraction:** Use TF-IDF vectorization on movie descriptions.
3. **Similarity Computation:** Calculate cosine similarity between all movie vectors.
4. **Recommendation:** For a selected movie, recommend the top similar ones.
5. **Movie Info Fetching:** Use OMDb API to get poster and plot details dynamically.

## 🛠️ Tech Stack

- **Python** – Core programming language
- **Pandas, scikit-learn** – Data processing & similarity computation
- **Streamlit** – Web app UI
- **Joblib** – For saving/loading preprocessed data
- **OMDb API** – To fetch real-time movie info (poster, plot)
