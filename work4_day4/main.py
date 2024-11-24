import streamlit as st

st.write(f"your sample API key: {st.secrets['API_Key']}")

session = st.connection("snowflake").session()
st.write(session.sql("select current_version()").collect()[0][0])