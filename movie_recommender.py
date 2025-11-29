import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib


# LOAD DATA

def load_data():
    print("📁 Loading data...")

    # FULL absolute path
    path = "/Users/kerenkoleoso/Documents/Portfolio-1/movie_recommender/movies_small.csv"

    movies = pd.read_csv(path, low_memory=False)

    movies['overview'] = movies['overview'].fillna("")
    return movies



# BUILD TF-IDF MATRIX

def build_tfidf(movies):
    print("🔧 Building TF-IDF matrix...")
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(movies["overview"])

    # Save for reuse
    joblib.dump(tfidf, "tfidf_vectorizer.joblib")
    joblib.dump(tfidf_matrix, "similarity_matrix.joblib")

    print("✅ TF-IDF + similarity saved!")
    return tfidf_matrix



# LOAD OR BUILD MODEL

def load_or_build(movies):
    try:
        print("📦 Loading prebuilt model...")
        tfidf = joblib.load("tfidf_vectorizer.joblib")
        similarity = joblib.load("similarity_matrix.joblib")
        print("✅ Loaded!")
        return tfidf, similarity
    except:
        print("⚠️ No saved model found — building new one.")
        tfidf_matrix = build_tfidf(movies)
        similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
        return None, similarity



# RECOMMEND MOVIES

def recommend(movie_title, movies, similarity):
    movie_title = movie_title.lower()

    # Look for movie by title
    matches = movies[movies['title'].str.lower() == movie_title]

    if matches.empty:
        print("❌ Movie not found.")
        return

    idx = matches.index[0]

    # Get similarity scores
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\n🎬 Top recommendations similar to '{movie_title.title()}':\n")
    rec_count = 0

    for i, score in scores[1:]:
        title = movies.iloc[i]["title"]
        if isinstance(title, str):
            print(f"- {title}")
            rec_count += 1

        if rec_count == 5:
            break



# MAIN

def main():
    movies = load_data()

    _, similarity = load_or_build(movies)

    print("\n✨ Movie Recommender Ready!")
    user_movie = input("Enter a movie title: ")
    recommend(user_movie, movies, similarity)


if __name__ == "__main__":
    main()
