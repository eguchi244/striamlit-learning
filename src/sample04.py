import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px

### 1. CSVを生成
st.write('### 1. CSVを生成')
filename = 'sample.csv'

# 1.1 データ生成部
# 生成するデータ数を確認, st.number_input(text, 最小値, 初期値)
num_data = st.number_input('生成するデータ数を選択してください', min_value=1, value=3)

if st.button(f'{filename}を生成'):
    # データ生成
    df = pd.DataFrame({
        # date_range(開始日, データ個数, 頻度:Daily = 1日刻み)
        '日付': pd.date_range(start='2026-01-01', periods=num_data, freq='D'),
        # 0~30の乱数を生成
        '温度': np.random.rand(num_data) * 30,
        # 40%~90%の範囲の乱数をnum_data個で生成
        '湿度': np.random.randint(40, 100, size=num_data)
    })
    df.to_csv(filename, index=False)
    st.write(f'{filename}を生成しました')

### 2. CSV編集テーブル
if os.path.exists(filename):
    st.write("### 2. CSVテーブル")
    # 2.1 データ編集部, st.data_editor(対象データ, 表示件数)
    data = pd.read_csv(filename)
    edited_data = st.data_editor(data, num_rows=10)

    # CSVを上書き保存
    if st.button('CSVを保存する'):
        edited_data.to_csv(filename, index=False)
        st.success('保存しました！')

    # 2.2 テーブル描画部
    # 温度の折れ線グラフ
    # 折れ線グラフのインスタンスを生成する
    fig = px.line(edited_data,  # 対象データ
                  x='日付', # x軸指定
                  y='温度', # y軸指定
                  title='温度の時系列データ', # タイトル指定
                  markers=True # マーカー指定
    )
    # テーブル描画
    st.plotly_chart(fig)

    # 湿度の折れ線グラフ
    fig = px.line(edited_data,
                   x='日付', 
                   y='湿度', 
                   title='湿度の時系列データ', 
                   markers=True
    )
    st.plotly_chart(fig)
else:
    st.info('先にCSVを生成してください')