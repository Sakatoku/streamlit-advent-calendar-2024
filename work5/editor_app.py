import streamlit as st
import pandas as pd

st.title("データ編集アプリ")

# 編集する元のデータを読み出す
@st.cache_data
def read_data(country):
    # キャッシュがないときはこのコードが実行される
    print("read_data called")
    # 2つ目のアプリで使用したCSVファイルをこのPythonファイルと同じディレクトリに置いておく
    df = pd.read_csv("work2_delivery_plan.csv")
    return df[df["area_jp"] == country]

# 国を選ぶ
country = st.selectbox("国を選んでください", ["日本", "アメリカ", "イギリス"])

# データを編集する
df = read_data(country)
edited_df = st.data_editor(df)

# 編集したデータを保存する
st.download_button(
    label="CSVでダウンロード",
    data=edited_df.to_csv(index=False).encode("utf-8"),
    file_name="result.csv",
    mime="text/csv",
)
