import streamlit as st
import pandas as pd
from DataPreprocessing import data_preprocessing
from chart import create_pie_chart, create_bar_chart
from utils.constants import ma_linh_kien, ma_hien_tuong, ma_nguyen_nhan, ma_nguyen_nhan_goc
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
    figure_ht = create_pie_chart(df2, 'HT', 'Hiện Tượng', ma_hien_tuong)
    st.plotly_chart(figure_ht, use_container_width=True)

with col2:
    figure_nn = create_pie_chart(df2, 'NN', 'Nguyên Nhân', ma_nguyen_nhan)
    st.plotly_chart(figure_nn, use_container_width=True)

with col3:
    figure_nng = create_pie_chart(df2, 'NNG', 'Nguyên Nhân Gốc', ma_nguyen_nhan_goc)
    st.plotly_chart(figure_nng, use_container_width=True)

with col1:
    max_ht = df2['HT'].mode()[0]
    filtered_df2 = df2[df2['HT']==max_ht]
    st.write(filtered_df2)
    figure_max_ht = create_bar_chart(filtered_df2, 'Line')
    st.plotly_chart(figure_max_ht, use_container_width=True)


col4, col5 = st.columns(2)

with col4:
    figure_lkdb = create_pie_chart(df2, 'LKDB', 'Linh Kiện Đồng Bộ', ma_linh_kien)
    st.plotly_chart(figure_lkdb, use_container_width=True)

with col5:
    figure_lkkttr = create_pie_chart(df2, 'LKKTTR', 'Linh Kiện Không Thể Tách Rời', ma_linh_kien)
    st.plotly_chart(figure_lkkttr, use_container_width=True)




