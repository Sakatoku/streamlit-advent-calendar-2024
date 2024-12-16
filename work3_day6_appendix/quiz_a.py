import streamlit as st

# アプリの初期化処理を行う
if "login_id" not in st.session_state or st.session_state.login_id == None:
    st.warning("ユーザーIDを選択してください。")
    if st.button("ユーザー選択ページに戻る"):
        st.switch_page("main.py")
    st.stop()

login_id = st.session_state.login_id
quiz_id = "quiz_a"

if "answer_status" not in st.session_state:
    st.session_state.answer_status = {}

if login_id not in st.session_state.answer_status:
    st.session_state.answer_status[login_id] = {}

# クイズアプリを表示する
st.write(
    "クイズA：以下のコードを実行すると何が表示されますか？"
)

st.code(
    """
import streamlit as st

st.write("Streamlitはとても簡単です！")
"""
)

options = ["エラーが出る", "Streamlitはとても簡単です！", "何も表示されない"]
selected_answer = st.selectbox(
    "出力結果を選んでください：",
    options=options,
    index=None,
)

# クイズの結果を処理する
if selected_answer == None:
    pass
elif selected_answer == "Streamlitはとても簡単です！":
    st.success("その通りです！")
    st.session_state.answer_status[login_id][quiz_id] = 1
    st.balloons()
else:
    st.error("惜しいです！")
