import streamlit as st


# ページ選択（カスタマイズ版）をサイドバーに表示する
def display_page_links_sidebar():
    with st.sidebar:
        st.page_link("main.py", label="ユーザー選択", icon="🐱")
        st.page_link("pages/quiz_a.py", label="クイズA", icon="❓️")
        st.page_link("pages/result.py", label="回答状況", icon="📊")


def display_sidebar():
    display_page_links_sidebar()
