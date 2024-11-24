import streamlit as st
from snowflake.cortex import Complete
from snowflake.snowpark.context import get_active_session


# Get the current credentials
session = get_active_session()

# LLMモデルの選択肢
LLM_OPTIONS = [
    "mistral-large2",
    "llama3.1-8b",
    "llama3.1-70b",
]

"""書きたいことのメモ
他にもいろいろなモデルが使えるよ。
https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex#arguments
https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#availability
"""

# LLMモデルの選択
llm_model = st.selectbox("対話するCortex LLMモデルを選択してください", LLM_OPTIONS)

# 新しいプロンプトを送信
if prompt := st.chat_input("Cortex LLMとのチャットを始めましょう"):
    # ユーザーのメッセージを追加
    with st.chat_message("user"):
        st.markdown(prompt)

    # LLMにリクエストを送信
    response = Complete(llm_model, prompt)

    # アシスタントのレスポンスを追加
    with st.chat_message("assistant"):
        st.markdown(response)