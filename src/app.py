import streamlit as st
import pandas as pd
from utils.data_processing import clean_data
from utils.visualization import plot_feature_count, plot_metric_distribution

df = pd.read_csv('https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv')
df=clean_data(df)

# Título de la aplicación
st.title("Análisis y distribución de características en autos")
# Agregar un texto
st.write("¡Bienvenido! Aquí podrás graficar y visualizar distintas características de automóviles vendidos en los últimos años")

# Initialize session state variables if they don’t exist
if "show_feature" not in st.session_state:
    st.session_state.show_feature = False
if "show_metric" not in st.session_state:
    st.session_state.show_metric = False

# Feature Selection
feature = st.selectbox(
    'Selecciona una característica para gráficar',
    ('fuel_type', 'transmission', 'model', 'brand')
)

st.write('Seleccionaste:', feature)

if st.button(f"Mostrar gráfico y tabla de {feature}"):
    st.session_state.show_feature = True  # Store the state

if st.session_state.show_feature:
    st.pyplot(plot_feature_count(df, feature))
    st.dataframe(df.groupby(feature).size())

# Metric Selection
metric = st.selectbox(
    'Selecciona una métrica para gráficar',
    ('year', 'engine_size', 'mileage', 'doors', 'owner_count', 'price')
)

st.write('Seleccionaste:', metric)

if st.button(f"Mostrar gráfico y tabla de {metric}"):
    st.session_state.show_metric = True  # Store the state

if st.session_state.show_metric:
    st.pyplot(plot_metric_distribution(df, metric))
    st.dataframe(df.groupby(metric).size())