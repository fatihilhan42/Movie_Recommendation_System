import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Veri setini yükle
@st.cache_data  # Yeni önbellekleme komutu
def load_data():
    Movie_df = pd.read_csv('/content/sample_data/Movie_df.csv')  # varsayılan olarak csv dosyasını kullanıyorum, dosya adınızı değiştirebilirsiniz
    return Movie_df

# TF-IDF vektörlerini oluştur
@st.cache_data  # Yeni önbellekleme komutu
def create_tfidf_matrix(data):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['tags'].values.astype('U'))
    return tfidf_matrix

# Kosinüs benzerliğini hesapla
@st.cache_data  # Yeni önbellekleme komutu
def calculate_cosine_similarity(_tfidf_matrix):
    cosine_sim = cosine_similarity(_tfidf_matrix, _tfidf_matrix)
    return cosine_sim

# Film önerilerini al
@st.cache_data  # Yeni önbellekleme komutu
def get_recommendations(title, data, cosine_sim):
    idx = data[data['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    recommended_movies = [data['title'].iloc[i[0]] for i in sim_scores]
    return recommended_movies

# Afişleri al
def fetch_poster(movie_title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': 'fd5d08451c6cbb8b3ec7b1815a737821',  # The Movie Database (TMDb) API key
        'query': movie_title
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['results']:
        movie_id = data['results'][0]['id']
        poster_path = data['results'][0]['poster_path']
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None

def main():
    st.title('Film Öneri Sistemi')

    # Veri setini yükle
    Movie_df = load_data()

    # TF-IDF vektörlerini oluştur
    tfidf_matrix = create_tfidf_matrix(Movie_df)

    # Kosinüs benzerliğini hesapla
    cosine_sim = calculate_cosine_similarity(tfidf_matrix)

    # Film seçme arayüzü
    film_basligi = st.selectbox('Lütfen bir film seçin:', Movie_df['title'].values)

    if st.button('Öneri Al'):
        # Önerileri al
        recommendations = get_recommendations(film_basligi, Movie_df, cosine_sim)
        
        # Önerilen filmleri göster
        st.subheader('Önerilen Filmler:')
        cols = st.columns(len(recommendations))  # Kolonları oluştur
        for i, recommendation in enumerate(recommendations):
            with cols[i]:  # Her bir kolona bir film ve afiş ekleyin
                st.write(recommendation)
                poster_url = fetch_poster(recommendation)
                if poster_url:
                    st.image(poster_url, caption=recommendation, width=200, use_column_width=True)  # Afişleri küçültmek için width parametresini ayarlayın
                else:
                    st.write("Afiş bulunamadı.")

if __name__ == "__main__":
    main()
