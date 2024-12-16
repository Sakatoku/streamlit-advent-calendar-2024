import streamlit as st

# セッションステートのリセットボタンをサイドバーに表示する
def display_reset_state_sidebar():
    with st.sidebar:
        if st.button("ステートをリセットする"):
            st.session_state.clear()

display_reset_state_sidebar()

login = st.Page("login.py", title="ユーザー選択", icon="🐱")
quiz_a = st.Page("quiz_a.py", title="クイズA", icon="❓️")
result= st.Page("result.py", title="回答状況", icon="📊")

page = st.navigation(
    {
        "Account": [login],
        "Quiz": [quiz_a],
        "Result": [result],
    }
)
page.run()