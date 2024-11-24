import json

import streamlit as st
from snowflake.cortex import Complete
from snowflake.snowpark.context import get_active_session


def extract_message_from_response(response: str) -> str:
    # JSON文字列を辞書に変換
    response_dict = json.loads(response)
    
    # choices 配列からメッセージを取得
    return response_dict["choices"][0]["messages"]


# Get the current credentials
session = get_active_session()

# LLMモデルの選択肢
LLM_OPTIONS = [
    "mistral-large2",
    "llama3.1-8b",
    "llama3.1-70b",
]

# LLMモデルの選択
llm_model = st.selectbox("対話するCortex LLMモデルを選択してください", LLM_OPTIONS)


# 会話履歴をセッション状態で保持
if "messages" not in st.session_state:
    st.session_state.messages = []

# 過去の会話を表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 新しいプロンプトを送信
if prompt := st.chat_input("Cortex LLMとのチャットを始めましょう"):
    # ユーザーのメッセージを追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # LLMに履歴を含むリクエストを送信
    response_dict = Complete(llm_model, st.session_state.messages)
    response = extract_message_from_response(response_dict)
    
    # アシスタントのレスポンスを追加
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
