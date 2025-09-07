import streamlit as st 
import pickle 
import pandas as pd 
import requests

def fetch_poster(movie_id): 
    api_key = st.secrets['TMDB_API_KEY']
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    try: 
        response = requests.get(url)
        response.raise_for_status()
        data = response.json() 
        print(data)
        st.write(data)
        poster_path = data.get('poster_path')
        print(poster_path)
        st.write(poster_path)
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/kuf6dutpsT0vSVehic3EZIqkOBt.jpg  "
        else:
            "https://via.placeholder.com/500x750?text=No+Poster" 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"
    
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = [] 
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from api 
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters



movies_dict = pickle.load(open('pickle/movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('pickle/similarity.pkl','rb'))

st.header('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select the movie to get recommendations:',
    (movies['title'].values)
)

if st.button('Show Recommendations'):
    recommended_movies,recommended_movies_posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1: 
        st.text(recommended_movies[0])
        st.image(recommended_movies_posters[0])
    with col2: 
        st.text(recommended_movies[1])
        st.image(recommended_movies_posters[1])
    with col3: 
        st.text(recommended_movies[2])
        st.image(recommended_movies_posters[2])
    with col4: 
        st.text(recommended_movies[3])
        st.image(recommended_movies_posters[3])
    with col5: 
        st.text(recommended_movies[4])
        st.image(recommended_movies_posters[4])