import pandas as pd
import warnings
import streamlit as st
warnings.filterwarnings('ignore')

@st.cache_data(show_spinner=False)
def data_preprocessing(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name = sheet_name, skiprows = 5, header = None)

    df = df.drop(df.columns[0], axis = 1)

    df = df.iloc[:, [2,8,9,11,12,13,36]]

    df = df.dropna()

    column_names = ['Line', 'LKDB', 'LKKTTR', 'HT', 'NN', 'NNG', 'Group']

    df.columns = column_names

    return df