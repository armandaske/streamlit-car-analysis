import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_fuel_type_count(df: pd.DataFrame):
    """
    Genera un gráfico de barras que muestra la cantidad de vehículos por tipo de combustible.

    :param df: DataFrame con los datos de vehículos.
    :return: Figura de Matplotlib con el gráfico generado.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x=df["Fuel_Type"], palette="viridis", ax=ax)
    ax.set_xlabel("Tipo de Combustible")
    ax.set_ylabel("Cantidad de Vehículos")
    ax.set_title("Cantidad de Vehículos por Tipo de Combustible")
    ax.grid()
    return fig

def plot_price_distribution(df: pd.DataFrame):
    """
    Genera un gráfico de barras que muestra la cantidad de vehículos por tipo de combustible.

    :param df: DataFrame con los datos de vehículos.
    :return: Figura de Matplotlib con el gráfico generado.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    df["Price"].hist(bins=20)
    ax.set_xlabel("precio (USD)")
    ax.set_ylabel("Cantidad de Vehículos")
    ax.set_title("Cantidad de Vehículos por precio")
    ax.grid()
    return fig