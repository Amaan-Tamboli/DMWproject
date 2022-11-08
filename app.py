import joblib
import streamlit as st
from developer import developer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer(stop_words='english')


add_selectbox = st.sidebar.selectbox("Details/Developer",("Prediction","Developer"))
if add_selectbox== "Developer":
    developer()
elif(add_selectbox=="Prediction"):
    model = joblib.load('Real-Fake')
    st.markdown('<h1 style="text-align:center;color:black;font-weight:bolder;font-size:100px;">FAKE NEWS PREDICTION</h1>',unsafe_allow_html=True)

    ip = st.text_input('Enter the news article : ')
    op = model.predict([ip])
    if st.button('Predict'):
      st.title(op[0])
