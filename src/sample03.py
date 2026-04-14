import streamlit as st
import pandas as pd
import numpy as np
import os

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

# 1.2 テーブル描画部
if os.path.exists(filename):
    data = pd.read_csv(filename)
    st.write(data)
else:
    st.info('先にCSVを生成してください')