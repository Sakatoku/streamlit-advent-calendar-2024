import streamlit as st

from sidebar import display_sidebar

display_sidebar()

# クイズアプリを表示する
st.write(
    "クイズA：以下のコードを実行すると何が表示されますか？"
)  # ここはCSSとかでちょっといい感じに表示できると良いかも？(Day3で対応したい)

# st.html('''
#         <!-- CSSでスタイルを設定 -->
#         <style>
#         .quiz-text{
#             padding: 0.5em 1em;
#             margin: 2em 0;
#             color: #474747;
#             background: whitesmoke;/*背景色*/
#             border-left: double 7px #4ec4d3;/*左線*/
#             border-right: double 7px #4ec4d3;/*右線*/
#         }
#         .quiz-text p {
#             margin: 0; 
#             padding: 0;
#             font-size: 1.3rem;
#             font-weight: bold;
#         }
#         </style>

#         <!-- クイズ文言の表示 -->
#         <div class="quiz-text">
#             <p>クイズA：以下のコードを実行すると何が表示されますか？</p>
#         </div>
#         ''')

st.code(
"""
import streamlit as st

st.write("Streamlitはとても簡単です！")
"""
,language="python", line_numbers=True
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
