import streamlit as st
import pandas as pd
from utils.data_processing import clean_data
from utils.visualization import plot_fuel_type_count, plot_price_distribution

df = pd.read_csv('https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv')


# Título de la aplicación
st.title("Mi primera aplicación con Streamlit 🚀")
# Agregar un texto
st.write("¡Bienvenido a tu primera aplicación interactiva en Python!")
if st.button("Mostrar gráfico y tabla"):
    st.pyplot(plot_fuel_type_count(df))
    st.dataframe(df.head())