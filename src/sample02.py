import streamlit as st
import numpy as np
import pandas as pd
import os

### 1. ラインチャート
st.write('## 1. ラインチャート')

# 1.1 データ生成部
st.write('#### 1.1. CSVデータを生成する')
if st.button('sample.csvを生成'):
    # データ生成
    sample_df = pd.DataFrame({
        # date_range(開始日, データ個数, 頻度:Daily = 1日刻み)
        'data': pd.date_range(start='2021-01-01', periods=100, freq='D'),
        # 乱数を100個生成
        'value': np.random.rand(100)
    })
    # CSVに保存, to_csv(ファイル名, 行番号設定)
    sample_df.to_csv('sample_data.csv', index=False)
    # メッセージ表示
    st.write('sample.csvを生成しました')

# 1.2 ラインチャート描画部
st.write('#### 1.2. CSVデータを可視化する')
# 「ボタン」ではなく「ファイルが存在するか」で判定する
if os.path.exists('sample_data.csv'):
    # 可視化ボタン
    if st.button('sample.csvを可視化'):
        # CSV読み込み
        sample_df = pd.read_csv('sample_data.csv')
        # チャート描画, df.set_index('data')でdataの値を横軸に設定
        st.line_chart(sample_df.set_index('data'))
else:
    st.info('先にCSVを生成してください')

### 2. マルチシリーズラインチャート
st.write('## 2. マルチシリーズラインチャート')

# 2.1 データ生成部
st.write('#### 2.1. CSVデータを生成する')
if st.button('multi_series_data.csvを生成'):
    # データ生成
    multi_df = pd.DataFrame({
        'date': pd.date_range(start='2026-01-01', periods=100, freq='D'),
        'value1': np.random.rand(100),
        'value2': np.random.rand(100),
        'value3': np.random.rand(100),
    })
    # CSVに保存
    multi_df.to_csv('multi_series_data.csv', index=False)
    # メッセージ表示
    st.write('multi_series_data.csvを生成しました')

# 2.2 マルチシリーズラインチャート描画部
st.write('#### 2.2. CSVデータを可視化する')
# ユーザに選択されたカラムのラインチャートを描画する
# 「ボタン」ではなく「ファイルが存在するか」で判定する
if os.path.exists('multi_series_data.csv'):
    # CSV読み込み
    multi_df = pd.read_csv('multi_series_data.csv')
    # 描画可能なカラムを取得（dateを除外する）
    available_columns = multi_df.columns[1:]
    # 描画対象カラムを選択
    selected_columns = st.multiselect("描画するカラムを選択する", available_columns)
    # チャート描画 
    if selected_columns:
        st.line_chart(multi_df.set_index('date')[selected_columns])
    else:
        st.write('表示する項目を選択してください')
else:
    st.info('先にCSVを生成してください')