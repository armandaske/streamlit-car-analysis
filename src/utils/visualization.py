import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_count(df: pd.DataFrame, feature: str):
    """
    Genera un gráfico de barras que muestra la cantidad de vehículos por tipo de combustible.

    :param df: DataFrame con los datos de vehículos.
    :return: Figura de Matplotlib con el gráfico generado.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x=df[feature], palette="viridis", ax=ax)
    ax.set_xlabel(feature)
    ax.set_ylabel("Cantidad de Vehículos")
    ax.set_title(f"Cantidad de Vehículos por {feature}")
    ax.grid()
    return fig

def plot_metric_distribution(df: pd.DataFrame, metric: str):
    """
    Genera un gráfico de barras que muestra la cantidad de vehículos por tipo de combustible.

    :param df: DataFrame con los datos de vehículos.
    :return: Figura de Matplotlib con el gráfico generado.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    df[metric].hist(bins=20)
    ax.set_xlabel("precio (USD)")
    ax.set_ylabel("Cantidad de Vehículos")
    ax.set_title(f"Cantidad de Vehículos por {metric}")
    ax.grid()
    return fig