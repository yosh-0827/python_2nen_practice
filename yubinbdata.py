# -*- coding: utf-8 -*-
"""yubinbdata.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LB0i5MsSCQDZfj-lw3eOkGQGuWVEcPnx
"""

import pandas as pd

# データフレームを読み込む
df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis")
print(len(df))
print(df.columns.values)

import pandas as pd

df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis")

# 2の列が１６００００６の住所を抽出して表示
result = df[df[2] == 1600006]
print(result[[2,6,7,8]])

import pandas as pd

df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis")

# 8の列が四谷の住所を抽出して表示
result = df[df[8] == "四谷"]
print(result[[2,6,7,8]])

# 8の列に「四谷」の文字が含まれている住所を抽出して表示
result = df[df[8].str.contains("四谷")]
print(result[[2,6,7,8]])