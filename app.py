import joblib
import streamlit as st
from developer import developer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


add_selectbox = st.sidebar.selectbox("Details/Developer",("Student Details","Developer"))
if add_selectbox== "Developer":
    developer()
    
model = joblib.load('RealFakeModel')
st.markdown('<h1 style="text-align:center;color:white;font-weight:bolder;font-size:100px;">FAKE NEWS PREDICTION</h1>',unsafe_allow_html=True)

ip = st.text_input('Enter the news article : ')

op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
  
comment_words = ''
stopwords = set(STOPWORDS)

for val in df.CONTENT:

    val = str(val)
 
    tokens = val.split()
     
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "
 
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig)
