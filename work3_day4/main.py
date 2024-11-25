import streamlit as st

from sidebar import display_sidebar

display_sidebar()

# ログインユーザーの取得処理
login_ids = ["🐈️", "🐋", "🐍"]
login_id = st.selectbox(
    "ログインするユーザーを選択しましょう！", options=login_ids, index=None
)
st.session_state.login_id = login_id

# ログイン処理
if login_id:
    if st.button("クイズに挑戦する"):
        st.switch_page("pages/quiz_a.py")
