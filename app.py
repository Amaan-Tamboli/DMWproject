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
    
model = joblib.load('Real-Fake')
st.markdown('<h1 style="text-align:center;color:black;font-weight:bolder;font-size:100px;">FAKE NEWS PREDICTION</h1>',unsafe_allow_html=True)

ip = st.text_input('Enter the news article : ')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
  
 
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                stopwords = stopwords,
                min_font_size = 10).generate(ip)
                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig)
