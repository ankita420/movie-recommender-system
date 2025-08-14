import streamlit as st
import pickle
import pandas as pd



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

movies_dict=pickle.load(open("movie_dict.pkl","rb"))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

option=st.selectbox('Give a movie name',movies['title'].values)
if st.button('Recommend'):
    names=recommend(option)


    print( st.text(names[0]))


    print(st.text(names[1]))


    print(st.text(names[2]))


    print(st.text(names[3]))


    print(st.text(names[4]))
