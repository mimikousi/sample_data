import pandas as pd

#変数名のリストを作成します
columns = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'y']

#txtファイルをcsvファイルに変換します。
df = pd.read_table('debutanizer_data.txt', skiprows=2, sep='  ',header=None, engine='python')
df.columns = columns
df.to_csv('debutanizer_data.csv', index=False)