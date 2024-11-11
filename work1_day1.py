import streamlit as st

st.title("Streamlitクリスマスカード 🎅")

# ボタンを押すと雪が降る
button_pushed = st.button("雪を降らせる")
if button_pushed:
    st.snow()
