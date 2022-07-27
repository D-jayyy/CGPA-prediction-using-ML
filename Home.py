##creating a streamlit file

import pickle  #to load a saved model
import streamlit as st
import pandas as pd


@st.cache(suppress_st_warning=True)
def load_model():
    model = pickle.load(open('1st_model.pkl', 'rb'))
    return model



st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to CGPA PREDICTION PORTAL 👋")

st.sidebar.success("Select from above pages.")
st.sidebar.caption('This project is made by: CS-19076, CS-19100, CS-19121.')

st.markdown(
    """
    This is a simple web-app that predicts the CGPA of a student using "MACHINE LEARNING" techniques.
    
    p.s: Machine Learning is a field that uses data to learn patterns and predict future events.Hence it is not some sort of magic :)
    

"""
)








