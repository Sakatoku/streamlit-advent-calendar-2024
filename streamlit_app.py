import streamlit as st

# セッションステートの設計
# - day: st.selectboxで選択された日付番号(1-25)
# - article_id: 実際に表示する記事の日付番号(1-25)

# 日付番号をURLパラメータから取得する
def get_day_from_query_params():
    if "day" in st.query_params:
        return int(st.query_params["day"])
    return None

# 日付番号をセッションステートから取得する
def get_day_from_session_state():
    if "article_id" in st.session_state:
        return st.session_state.article_id
    return 0

# 日付番号を更新する
def update_day():
    # article_idとdayを同期させる
    st.session_state.article_id = st.session_state.day
    # URLパラメータを更新
    st.query_params["day"] = st.session_state.article_id

# ファイルを読み込んで表示する
def show_article(article_id):
    filename = f"articles/{article_id}.md"
    if article_id == 0:
        filename = "articles/introduction.md"
    # articles/{artile_id}.md から記事を読み込んで、st.markdown() で表示する
    with open(filename, "r", encoding="utf-8") as f:
        st.markdown(f.read())

# ページ設定を変更
st.set_page_config(
    page_title="Streamlit Advent Calendar 2024",
    page_icon=":snowman:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# selectboxの表示フォーマット
def format_day(day):
    if day == 0:
        return "はじめに"
    return f"{day}日目"

# サイドバーを設定
st.sidebar.header(":snowman: About")
st.sidebar.markdown("""
:streamlit: [Streamlit](https://streamlit.io)はインタラクティブなデータアプリを簡単に作れるPythonライブラリです。  
[Streamlit Advent Calendar 2024](https://qiita.com/advent-calendar/2024/streamlit)は、[30 Days of Streamlit](https://30days.streamlit.app/)の日本語アップデート版として、25日間でStreamlitによるデータアプリの開発を習得できるチュートリアルを作ろう！というコミュニティ企画です。  
""")

st.sidebar.header(":material/collections_bookmark: リソース")
st.sidebar.markdown("""
- [Playground](https://www.streamlit.io/playground)
- [Documentation](https://docs.streamlit.io/)
- [書籍](https://techbookfest.org/product/fhiwFCAW3weeFibUeFc4p1?productVariantID=1m3McjcE7dvXzMZcwQDz8c) (Streamlit入門)
"""
)

st.sidebar.header(":material/share: アプリをシェアしよう")
st.sidebar.markdown("""
:streamlit: [Streamlit Community Cloud](https://streamlit.io/cloud)を使うと作ったデータアプリをたった数回のクリックで公開できます！
""")

# タイトルを設定
st.title(":christmas_tree: Streamlit Advent Calendar 2024 :calendar:")

# 表示する記事の日付番号を決定する
article_id = get_day_from_query_params()
if article_id is None:
    article_id = get_day_from_session_state()
article_id = st.selectbox("読みたい記事を選択してください", list(range(0, 26)), article_id, key="day", format_func=format_day, on_change=update_day)

# 日付番号に応じた記事を表示する
show_article(article_id)
