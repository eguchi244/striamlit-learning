import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px
import plotly.graph_objects as go

### サンプルコード１
### 1. CSVテーブルを生成
st.write('### 1. CSVテーブルを生成')
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

    ### サンプルコード２
    ### 2. CSV編集テーブル
    st.write("### 2. CSV編集テーブル")

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

    ### サンプルコード３
    ### ### 3. インタラクティブな折れ線グラフ
    st.write("### 3. インタラクティブなグラフで可視化する")

    # 3.1 テーブル描画部
    # 折れ線グラフのインスタンスを生成する
    fig = go.Figure()
    # データ系列（トレース）を追加する
    fig.add_trace(go.Scatter(x=edited_data['日付'], # x軸指定
                             y=edited_data['温度'], # ｙ1軸指定(左)
                             mode='lines+markers', # モード指定
                             name='温度', # 凡例名指定
                             line=dict(color='red') # 線の色指定
    ))
    fig.add_trace(go.Scatter(x=edited_data['日付'], 
                             y=edited_data['湿度'], 
                             mode='lines+markers', 
                             name='湿度', 
                             line=dict(color='blue'), 
                             yaxis='y2' # ｙ2軸指定(左)
    ))

    # 3.2 折れ線グラフのレイアウト一括指定
    fig.update_layout(
        # グラフのタイトル指定
        title='温度と湿度の時系列データ',
        # X軸指定
        xaxis=dict(title='日付',  # x軸のタイトル
                   showgrid=False, # x軸のグリッドを非表示
                   showline=True, # x軸のラインを表示
                   ticks='inside', # x軸の目盛りを内側に表示
                   tickcolor='black' # x軸の目盛りの色
        ),
        # Y1軸指定(左)
        yaxis=dict(title='温度 [℃]', 
                   showgrid=False, 
                   showline=True, 
                   ticks='inside', 
                   tickcolor='black'
        ),
        # Y2軸指定(右)
        yaxis2=dict(title='湿度 [%]', 
                    overlaying='y', # y1軸と線を重ねる
                    side='right', # メモリを右側に表示
                    showgrid=False, 
                    showline=True, 
                    ticks='inside', 
                    tickcolor='black'
        )
    )
    # テーブル描画
    st.plotly_chart(fig)
else:
    st.info('先にCSVを生成してください')