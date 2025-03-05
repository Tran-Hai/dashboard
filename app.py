import streamlit as st
import pandas as pd
from DataPreprocessing import data_preprocessing
from chart import create_pie_chart, create_bar_chart
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title = "Data Visualization", layout = "wide", initial_sidebar_state = "expanded")

st.title(":bar_chart: Data Visualization")
st.markdown("Welcome to the Data Visualization app! Choose a dataset from the dropdown menu and visualize it using various chart types.")


file_path = "File số vụ BM tháng 2.25.xlsx"

# df1 = data_preprocessing(file_path, "CHUNG")
# df2 = data_preprocessing(file_path, "ASSY")
# df3 = data_preprocessing(file_path, "PROCESS")

col1, col2, col3 = st.columns(3)

st.sidebar.header("Choose a filter")
section = st.sidebar.selectbox("", ['CHUNG', 'ASSY', 'PROCESS'])

if not section:
    df1 = data_preprocessing(file_path, "CHUNG")
else:
    df1 = data_preprocessing(file_path, str(section))

group = st.sidebar.multiselect("Pick your group", df1['Group'].unique())

if not group:
    df2 = df1.copy()
else:
    df2 = df1[df1['Group'].isin(group)]


with col1:
    figure_ht = create_pie_chart(df2, 'HT', 'Hiện Tượng')
    st.plotly_chart(figure_ht, use_container_width=True)

with col2:
    figure_nn = create_pie_chart(df2, 'NN', 'Nguyên Nhân')
    st.plotly_chart(figure_nn, use_container_width=True)

with col3:
    figure_nng = create_pie_chart(df2, 'NNG', 'Nguyên Nhân Gốc')
    st.plotly_chart(figure_nng, use_container_width=True)






