import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("CSV Files/car_price_dataset (1).csv", sep=";")

st.write(df.columns)

df.columns = df.columns.str.strip()

st.title ("bilar")

st.dataframe(df)

fig, ax =plt.subplots()

ax.scatter(df["Mileage"], df["Price"])

st.write(df.columns.tolist())






ax.set_xlabel("Miltal")
ax.set_ylabel("Pris")
ax.set_title("Pris vs Miltal")
st.pyplot(fig)

cars = df["Brand"] + "" + df["Model"]
option = st.selectbox("Choose a car", "Bilar")

selected_car = df[cars == option]
st.write(selected_car)