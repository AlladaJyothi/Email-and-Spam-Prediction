import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB as nb

st.image(r"C:\Users\DELL\Pictures\inno_image.webp")
name=st.title('Email Spam and Ham Prediction')

model=pickle.load(open(r"C:\Users\DELL\Machine Learning\model.pkl",'rb'))
bow=pickle.load(open(r"C:\Users\DELL\Machine Learning\bow.pkl",'rb'))

email = st.text_input('Enter the Email:')
st.button("Submit")
data = bow.transform([email]).toarray() 
spam_ham = model.predict(data)[0]
spam_ham

if spam_ham=='spam':
    st.image(r"C:\Users\DELL\Pictures\spam image.PNG")
