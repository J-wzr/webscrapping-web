import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("data.txt")
print(df.columns)

fig = px.line(x=df["datetime"], y=df["temperature"],
              labels={"x":"Date", "y":"Temperature (C)"})


st.set_page_config("Plottings", page_icon="logo.png")
st.header("Graphs with Ploty")
st.text("Plotting automatic graph data from text files using ploty library for python")
st.plotly_chart(fig)