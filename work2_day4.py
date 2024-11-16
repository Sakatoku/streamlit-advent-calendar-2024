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
# st.write("国の一覧：", countries)

# 表示する国を選択する
selected_countries = st.multiselect("データを表示する国を選択してください", countries, default=countries[:3])
# st.write("選択された国：", selected_countries)

# 合計を計算して表示する
filtered_data = data[data["area_jp"].isin(selected_countries)]
total_delivered_count = filtered_data["delivered_count"].sum()
st.metric("🎁 予定配達数", total_delivered_count)

# タブを2つ作成する
tab1, tab2 = st.tabs(["ラインチャート :material/show_chart:", "バーチャート :material/bar_chart:"])

# タブ1: ラインチャート
with tab1:
    # 変形する
    pivot_data = data.pivot(index="time_utc", columns="area_jp", values="delivered_count")
    # 選択した国だけ抽出した後に、データがない部分を0で埋める
    chart_data = pivot_data.filter(items=selected_countries).fillna(0).reset_index()

    # 変形した後のデータフレームを表示
    st.caption("グラフ用データ")
    st.dataframe(chart_data)
    # ラインチャートを描画
    st.caption("グラフ")
    st.line_chart(chart_data, x="time_utc", y=selected_countries, height=500)

# タブ2: バーチャート
with tab2:
    # 変形する
    pivot_data = data.pivot(index="time_utc", columns="area_jp", values="delivered_count")
    # 選択した国だけ抽出した後に、データがない部分を0で埋める
    chart_data = pivot_data.filter(items=selected_countries).fillna(0).reset_index()

    # 変形した後のデータフレームを表示
    st.caption("グラフ用データ")
    st.dataframe(chart_data)
    # バーチャートを描画
    st.caption("グラフ")
    st.bar_chart(chart_data, x="time_utc", y=selected_countries, height=500)
