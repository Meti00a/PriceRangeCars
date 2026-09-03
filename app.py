import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("csvv/car_price_dataset (1).csv", sep=";")

st.title ("bilar")

st.dataframe(df)

fig, ax =plt.subplots()
ax.scatter(df["Mileage"], df["Price"])
ax.set_xlabel("Miltal")
ax.set_ylabel("Pris")
ax.set_title("Pris vs Miltal")
st.pyplot(fig)