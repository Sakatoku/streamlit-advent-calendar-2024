import streamlit as st
import pandas as pd

# Advanced: Matplotlib, Plotly, PyDeck
import matplotlib.pyplot as plt
import japanize_matplotlib
import plotly.graph_objects as go
import pydeck as pdk

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

# タブを3つ作成する
tab1, tab2, tab3 = st.tabs(["Matplotlib", "Plotly", "PyDeck"])

# タブ1: Pylotlibを使ったグラフ
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
    # ラインチャートを描画
    fig, ax = plt.subplots()
    for country in selected_countries:
        ax.plot(chart_data["time_utc"].str.slice(5, 16), chart_data[country], label=country)

    ax.set_xlabel("時間")
    ax.set_ylabel("配達数")
    ax.set_title("配達数の推移")
    if len(selected_countries) > 0:
        ax.set_xticks(chart_data["time_utc"].str.slice(5, 16)[::2])
    ax.legend()
    fig.autofmt_xdate()
    st.pyplot(fig)

# タブ2: Plotlyを使ったグラフ
with tab2:
    # 変形する
    pivot_data = data.pivot(index="time_utc", columns="area_jp", values="delivered_count")
    # 選択した国だけ抽出した後に、データがない部分を0で埋める
    chart_data = pivot_data.filter(items=selected_countries).fillna(0).reset_index()
    # 変形した後のデータフレームを表示
    st.caption("グラフ用データ")
    st.dataframe(chart_data)
    # ラインチャートを描画
    st.caption("グラフ")
    fig = go.Figure()
    for country in selected_countries:
        fig.add_trace(go.Bar(
            x=chart_data["time_utc"],
            y=chart_data[country],
            name=country
        ))

    # レイアウト設定
    fig.update_layout(
        title="国別のデータ分布",
        xaxis_title="時刻 (UTC)",
        yaxis_title="値",
        barmode="stack",
        template="plotly_white",
        legend_title="国",
    )

    # Streamlitで表示
    st.plotly_chart(fig, use_container_width=True)

# タブ3: PyDeckを使った地図
with tab3:
    # フィルタする
    filtered_data = data[data["area_jp"].isin(selected_countries)]
    # 国別に集計する
    map_data = filtered_data.groupby("area_jp").agg({"delivered_count": "sum", "latitude": "mean", "longitude": "mean"}).reset_index()
    map_data["size"] = map_data["delivered_count"] / 10
    point_layer = pdk.Layer(
        "ScatterplotLayer",
        data=map_data,
        id="Pydeck_selected_countries",
        get_position=["longitude", "latitude"],
        get_radius="size",
        get_fill_color=[255, 75, 75],
        pickable=True,
        auto_highlight=True,
    )
    view_state = pdk.ViewState(
        latitude=40,
        longitude=-117,
        controller=True, zoom=2.4, pitch=30
    )
    chart = pdk.Deck(
        point_layer,
        initial_view_state=view_state,
        tooltip={"text": "{area_jp}\n配達数: {delivered_count}"},
    )
    event = st.pydeck_chart(chart, on_select="rerun",selection_mode="multi-object")

    event.selection