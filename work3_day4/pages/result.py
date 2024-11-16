import streamlit as st

from sidebar import display_sidebar

display_sidebar()

st.bar_chart(st.session_state.answer_status, stack=False, horizontal=True)
