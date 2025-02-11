import pandas as pd

def clean_data(df):
    clean_df=df.copy()
    clean_df.columns=df.columns.str.strip().str.lower()
    clean_df.columns=clean_df.columns.str.replace(' ','_')
    clean_df=clean_df.drop_duplicates()
    clean_df=clean_df.dropna()
    clean_df
    return clean_df
