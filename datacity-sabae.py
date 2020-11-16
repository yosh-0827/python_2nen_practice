#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# データフレームを読み込む
df = pd.read_csv("200.csv", encoding="shift-jis")

print(len(df))
print(df.columns.values)


# In[3]:


import pandas as pd

# データフレームを読み込む
df = pd.read_csv("200.csv", encoding="shift-jis")

# 消火栓のある地点（緯度、経度）をリスト化する
hydrant = df[["緯度","経度"]].values             # リスト化
print(len(hydrant))
print(hydrant)


# In[6]:


import folium

# 地図を使って書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)   # 地図を作成(緯度経度は鯖江の場所を示す)
m.save("sabae.html")  # 地図を保存


# 地図にマーカーを追加する

# In[18]:


import folium

# 地図を作って書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)   # 地図を作成(緯度経度は鯖江の場所を示す)
folium.Marker([35.942957, 136.198863], tooltip="textwonyuuryokudekiruyo").add_to(m)
m.save("megane.html")
m


# 消火栓のデータを用いてどこにあるかピンで表示

# In[15]:


import folium
import pandas as pd

# データフレームを読み込む
df = pd.read_csv("200.csv", encoding="shift-jis")

# 消火栓のある地点（緯度、経度）をリスト化する
hydrant = df[["緯度", "経度"]].values
#print(df[["緯度", "経度"]].values)

# 地図を作って書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)
for data in hydrant:
    folium.Marker([data[0], data[1]]).add_to(m)
     # from IPython.core.debugger import Pdb; Pdb().set_trace()
     # デバッグしたい行の直前に、上記を追加します。
m.save("hydrant.html")
m

