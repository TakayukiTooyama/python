import streamlit as st
import cv2
import pandas as pd
import time

""" テキスト表示 """

st.title('タイトル表示')
st.header('ヘッダー表示')
st.subheader('サブヘッダー表示')
st.text('テキスト表示')


""" 画像の表示 """
image = cv2.imread("cat.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# use_column_width=TrueはWebの幅はを合わせる設定
st.image(image, caption="cat", use_column_width=True)


""" 動画の再生 """
st.video("face.mp4")


""" インタラクティブ機能 """
# ボタン
option_button = st.button("ボタン")
if option_button:
    st.write("ボタンが押されました")
else:
    st.write("ボタンが押してください")


# ファイルアップローダー
up_file = st.file_uploader("Upload file")

if up_file is not None:
    st.image(up_file, caption="cat", use_column_width=True)


# ラジオボタン
option_radio = st.radio(
    "好きな果物を選んでください。",
    ('りんご', 'みかん', 'ぶどう', 'ばなな'))
st.write("あなたが選んだ果物は：", option_radio)


# チェックボックス
option_checkbox = st.checkbox('DataFrameの表示')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40] })
if option_checkbox:
    st.write(df)


# セレクトボックス
st.selectbox(
    "好きな果物を選んでください。",
    ('りんご', 'みかん', 'ぶどう', 'ばなな'))


# マルチセレクトボックス
st.multiselect("好きな果物を選んでください。",
            ['りんご', 'みかん', 'ぶどう', 'ばなな'],
            ['りんご', 'みかん'])

# スライダー
age = st.slider("あなたの年齢を教えてください。", min_value=0, max_value=130, step=1, value=20)
st.write(f"私の年齢は{age}歳です。")

values = st.slider("範囲を選択してください。", 0, 100, (25, 75))
st.write(f"範囲は{values}です。")


# サイドバー
st.sidebar.title("サイドバー")


# プログレスバー
progress_button = st.button("プログレスバー")
if progress_button:
    st.write("処理を開始します")
    my_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        my_bar.progress(i + 1)
    st.text("処理が完了しました")
else:
    st.write("ボタンを押してください")
