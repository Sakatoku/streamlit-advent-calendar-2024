import streamlit as st
from snowflake.cortex import Complete


# Get the credentials
session = st.connection("snowflake").session()

# チャット欄をコンテナで括る
with st.container(border=True):
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

    # メッセージ表示用のコンテナを作成しておく
    messages = st.container(height=500)

    # 過去の会話を表示
    for message in st.session_state.messages:
        with messages.chat_message(message["role"]):
            st.markdown(message["content"])

    # 新しいプロンプトを送信
    if prompt := st.chat_input("Cortex LLMとのチャットを始めましょう"):
        # ユーザーのメッセージを追加
        st.session_state.messages.append({"role": "user", "content": prompt})
        with messages.chat_message("user"):
            st.markdown(prompt)

        # LLMに履歴を含むリクエストを送信
        response = Complete(llm_model, st.session_state.messages, stream=True, session=session)
        
        # アシスタントのレスポンスを追加
        with messages.chat_message("assistant"):
            full_response = st.write_stream(response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})



# --- 全体に対するクイズを追加 ---
with st.expander("📝 Quiz: このアプリの仕組みを理解できているか確認してみましょう！（全3問）"):
    st.markdown("次の3問について、下の回答番号をそれぞれ選んでください。最後に一括で回答をチェックします。")

    # Q1
    st.markdown("**Q1. 最も大きなパラメータ数を持ち、多言語にも対応しているLLMモデルはどれでしょうか？**")
    st.write("""
    1. mistral-large2  
    2. llama3.1-8b  
    3. llama3.1-70b
    """)
    q1_idx = st.radio("回答番号を選択 (Q1)", ["1", "2", "3"], key="q1", index=None)

    # Q2
    st.markdown("**Q2. メッセージ用コンテナ`messages = st.container(height=500)`を用意することで、どのようなメリットが得られるでしょうか？**")
    st.write("""
    1. LLMの処理速度が速くなる  
    2. 環境依存を減らし開発やデプロイを効率的に行えるようになる
    3. 予め表示する要素を定義しておくことで、複数の要素を意図した順序で表示できるようになる
    """)
    q2_idx = st.radio("回答番号を選択 (Q2)", ["1", "2", "3"], key="q2", index=None)

    # Q3
    st.markdown("**Q3. LLMからのストリーム対応を行うには、どのコードが正しいでしょうか？**")
    st.write("""
    1. `response = Complete(llm_model, st.session_state.messages, session=session)`  
    2. `response = Complete(llm_model, st.session_state.messages, stream=True, session=session)`  
    3. `response = Complete(llm_model, st.session_state.messages, stream=False, session=session)`
    """)
    q3_idx = st.radio("回答番号を選択 (Q3)", ["1", "2", "3"], key="q3", index=None)

    # 一括回答チェック
    if st.button("クイズの回答をチェック"):
        # Q1
        if q1_idx == "1":
            st.success("Q1: 正解です！`mistral-large2` は最も大きなパラメータ数（120B）を持ち、多言語対応も優れています。")
        else:
            st.error("Q1: 残念！もう一度挑戦してみましょう。")

        # Q2
        if q2_idx == "3":
            st.success("Q2: 正解です！メッセージ用コンテナを用意することで、複数の要素を意図した順序で表示できます。")
        else:
            st.error("Q2: 残念！もう一度挑戦してみましょう。")

        # Q3
        if q3_idx == "2":
            st.success("Q3: 正解です！ストリーム対応を行うには `stream=True` を指定します。")
        else:
            st.error("Q3: 残念！もう一度挑戦してみましょう。")