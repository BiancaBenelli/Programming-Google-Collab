import pandas as pd
import math_functions as mf
import streamlit as st
import matplotlib.pyplot as plt
           
# Get raw cs file from github
titanic_df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')
#titanic_df.info()
titanic_df.Age.hist()

#print(mf.is_prime(17))

# Create a dynamic page
st.header("Titanic project")
st.subheader("Predicting death")

#if st.checkbox("Show isplay Titanic Dataframe"):
#    st.write("Titanic dataframe:")
#    st.write(titanic_df)

# Sidebar are good to hide settings
st.sidebar.write("Settings")
if st.sidebar.checkbox("Show isplay Titanic Dataframe"):
    st.write("Titanic dataframe:")
    st.write(titanic_df)

if st.button("Different way to show the Titanic Dataframe"):
    st.write("Titanic dataframe:")
    st.write(titanic_df)

st.subheader("Plots in columns")
# Create columns
col_1, col_2 = st.columns(2)
with col_1:
    fig, ax = plt.subplots()
    titanic_df.Age.hist(ax = ax)
    st.write(fig)
    st.caption("Age histogram")

with col_2:
    fig, ax = plt.subplots()
    titanic_df.Sex.hist()
    st.write(fig)
    st.caption("Sex histogram")

with st.expander("Try"):
    fig, ax = plt.subplots()
    titanic_df.Sex.hist()
    st.write(fig)
    st.caption("Sex histogram")

#select_box = st.select_box()