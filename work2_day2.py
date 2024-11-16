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

# 国の一覧を取得する
countries = data["area_jp"].unique()
st.write("国の一覧：", countries)

# 表示する国を選択する
selected_countries = st.multiselect("データを表示する国を選択してください", countries, default=countries[:3])
st.write("選択された国：", selected_countries)

# 合計を計算して表示する
filtered_data = data[data["area_jp"].isin(selected_countries)]
total_delivered_count = filtered_data["delivered_count"].sum()
st.metric("🎁 予定配達数", total_delivered_count)
