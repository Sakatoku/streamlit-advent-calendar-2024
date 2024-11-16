import streamlit as st

from sidebar import display_sidebar

display_sidebar()

if "answer_status" not in st.session_state:
    st.warning("まだ誰も回答していないようです。")
    if st.button("クイズ画面に戻る"):
        st.switch_page("pages/quiz_a.py")

else:
    st.bar_chart(st.session_state.answer_status, stack=False, horizontal=True)
