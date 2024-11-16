import streamlit as st

from sidebar import display_sidebar

display_sidebar()

# クイズアプリを表示する
st.write(
    "クイズA：以下のコードを実行すると何が表示されますか？"
)  # ここはCSSとかでちょっといい感じに表示できると良いかも？(Day3で対応したい)

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
    st.balloons()
else:
    st.error("惜しいです！")
