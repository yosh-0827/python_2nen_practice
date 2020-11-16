#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

# データフレームを読み込み
# 読み込むファイルは実行するpyファイルと同じディレクトリに置くこと
df = pd.read_csv("FEH_00200524_201116152702.csv", index_col="全国・都道府県", encoding="shift_jis")

print(len(df))
print(df.columns.values)


# In[2]:


# pip install japanize-matplotlib
# japanize-matplotlibをインストールしていない場合、これを実行


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込み
df = pd.read_csv("FEH_00200524_201111160011.csv", index_col="全国・都道府県", encoding="shift_jis")

# 平成３０年の列データで棒グラフを作って表示する
df = df.drop("全国", axis=0)
df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",", ""))
print(df["平成30年"])
df["平成30年"].plot.bar(figsize=(150,100))
plt.show()
plt.savefig("bargraph.png")


# In[3]:


import matplotlib.pyplot as plt
import japanize_matplotlib

plt.plot([1, 2, 3, 4])
plt.xlabel('簡単なグラフ')
plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込み
df = pd.read_csv("FEH_00200524_201111160011.csv", index_col="全国・都道府県", encoding="shift_jis")

# 平成３０年の列データで棒グラフを作って表示する
df = df.drop("全国", axis=0)
df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",", ""))
df = df.sort_values("平成30年", ascending=False)    #人口の多い順に並べ替え
print(df["平成30年"])
df["平成30年"].plot.bar(figsize=(100,50))
plt.show()


# 平成30年と29年の人口増減を求める

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読む込む
df = pd.read_csv("FEH_00200524_201116152702.csv", index_col="全国・都道府県", encoding="shift_jis")

# 平成30年の列データで棒グラフを作って表示する
df = df.drop("全国", axis=0)

# カンマを取り除く
df["平成29年"] = pd.to_numeric(df["平成29年"].str.replace(",", ""))
df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",", ""))

# ２つの列データの差を新しい列として作る　df["新しい列"] = df["差分を取られる元"] - df["差しひく列"]
df["人口増減"] = df["平成30年"] - df["平成29年"]
df = df.sort_values("人口増減", ascending=False)
df["人口増減"].plot.bar(figsize=(10,6))
plt.show()

