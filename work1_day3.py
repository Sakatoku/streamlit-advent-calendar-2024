import streamlit as st

# 名前と国からメッセージを作成する関数。これはコピペして使ってください。
def make_message(name: str, country: str):
    data = {
        "日本": f"メリークリスマス、{name}さん！このクリスマスが{name}さんにとって愛と喜びに満ちたものになりますように。",
        "アメリカ": f"Ho Ho Ho! Merry Christmas, {name}! May your heart be warm, your home be bright, and your days be merry and full of happiness.",
        "中国": f"亲爱的{name}、圣诞快乐！愿你的每一天都充满笑容和祝福！",
        "オーストラリア": f"Ho Ho Ho! Merry Christmas, {name}! May your heart be warm, your home be bright, and your days be merry and full of happiness.",
    }
    return data[country]

# 国から画像のURLを作成する関数。これはコピペして使ってください。
def make_image_url(country: str):
    data = {
        "日本": "https://i.gyazo.com/7f7fa9985d27a49f7b65f2b6faf7bde5.jpg",
        "アメリカ": "https://i.gyazo.com/0ed3c1555f8c474a81a5ec77ecb657ff.jpg",
        "中国": "https://i.gyazo.com/721cc5acf919c27c9a57005af8b78ea2.jpg",
        "オーストラリア": "https://i.gyazo.com/566a5129252ac459c3493b07e0bb0683.jpg"
    }
    return data[country]

st.title("Streamlitクリスマスカード 🎅")

# ボタンを押すと雪が降る
button_pushed = st.button("雪を降らせる")
if button_pushed:
    st.snow()

# テキストを入力させる
name = st.text_input(f"あなたのお名前")
# 選択肢から国を選ばせる
country = st.selectbox(f"あなたが住んでいる国", ["", "日本", "アメリカ", "中国", "オーストラリア"])

# 名前と国が両方とも入力されたらクリスマスカードを表示する
if name != "" and country != "":
    # 国ごとに表示する内容を変える
    message = make_message(name, country)
    st.write(message)
    image_url = make_image_url(country)
    st.image(image_url)
