import streamlit as st
from snowflake.snowpark.context import get_active_session


# Get the current credentials
session = get_active_session()

# Day1

"""書きたいことのメモ
今回使うライブラリは、Snowflake-ml-pythonライブラリの1.6.4。
https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/1.6.4/api/model/snowflake.cortex.Complete


・パッケージの読み込み方法を解説。
・Cortex LLMを使ってみる
"""

from snowflake.cortex import Complete

request = st.text_input("プロンプトを入力してください", key="complete")
response = Complete("mistral-large2", request)
st.write(response)


from snowflake.cortex import Translate

request = st.text_input("プロンプトを入力してください", key="translate")
response = Translate(request, "ja", "en")
st.write(response)



"""書きたいことのメモ
他にも様々な関数があるので、遊んでみてね。
https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#task-specific-functions
https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/1.6.4/index

"""
