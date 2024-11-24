import streamlit as st
from snowflake.cortex import Complete


@st.cache_resource
def get_session():
    return st.connection("snowflake", max_entries=1).session()


# Get the credentials
session = get_session()

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
    response = Complete(llm_model, st.session_state.messages, stream=True)
    
    # アシスタントのレスポンスを追加
    with st.chat_message("assistant"):
        full_response = st.write_stream(response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
