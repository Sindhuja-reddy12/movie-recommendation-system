import streamlit as st
import pickle
import pandas as pd

movies_dic = pickle.load(open('movie_dict.pkl','rb'))
#mmovies_list = movies_list['title'].values
movies = pd.DataFrame(movies_dic)
similar = pickle.load(open('similar.pkl','rb'))

#here dataframe naem is movies
recommended_movies=[]

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similar[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('Movie-recommender-system')
option = st.selectbox(
"How would you like to be contacted?",
movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(option)
    for i in recommendations:

        st.write(i)


