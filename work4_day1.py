import streamlit as st
from snowflake.snowpark.context import get_active_session

# Get the current credentials
session = get_active_session()


# Snowflake LLMとの対話
from snowflake.cortex import Complete

request = st.text_input("プロンプトを入力してください", key="complete")
response = Complete("mistral-large2", request)
st.write(response)


# Snowflake LLMによる翻訳
from snowflake.cortex import Translate

request = st.text_input("プロンプトを入力してください", key="translate")
response = Translate(request, "ja", "en")
st.write(response)


# Snowflake LLMによる感情分析
from snowflake.cortex import Translate, Sentiment

request = st.text_input("プロンプトを入力してください")
response = Sentiment(Translate(request, "ja", "en"))
st.write(response)