import streamlit as st
import pandas as pd

st.title("プレゼント配送計画 🦌")

# ファイルをアップロードする
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
if uploaded_file is None:
    st.write("ファイルがアップロードされていません")
    st.stop()

# アップロードされたファイルを読み込む
data = pd.read_csv(uploaded_file)

# データの中身を表示する
st.dataframe(data)
