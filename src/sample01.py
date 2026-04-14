import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 入門')

st.write('これはStreamlitアプリのデモです。')

if st.button('押してください'):
    st.write('ボタンが押されました！')
    # お祝いの風船を飛ばす演出
    st.balloons()  

name = st.text_input('あなたの名前を入力してください。')
if name:
    st.write(f'あなたの名前は{name}ですね！')

# slider('text', 最小値, 最大値, 初期値)
age = st.slider('あなたの年齢', 0, 100, 25)
st.write(f'あなたの年齢は{age}ですね！')

# 生成した配列を「表形式」に変換する
data = pd.DataFrame(
    # 乱数を二次元配列[100][2]で生成する, randn(平均0,標準偏差1)の乱数を格納
    np.random.randn(100, 2),
    # aとbで列名(ヘッダー)を定義
    columns=['a', 'b']
)

# 折れ線グラフ(xの横軸:0~99の行, yの縦軸:aとbの列)を描画する
st.line_chart(data)