import streamlit as st

# API Key
st.write(f"your sample API key: {st.secrets['API_Key']}")

# Group User & Pass
st.write(f"your username: {st.secrets['group1']['username']}")
st.write(f"your password: {st.secrets['group1']['password']}")

# st.connectionによるSnowflakeセッションの作成
session = st.connection("snowflake").session()
st.write(session.sql("select current_user()").collect()[0][0])

# st.text_inputによるパスワードの取得
password = st.text_input("パスワードを入力してください", type="password")