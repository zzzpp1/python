
import numpy as np
import pandas as pd
import time, datetime

#一共有多少不同的用户
f1=open(r'C:\Users\zhang\Desktop\ml-latest-small\tags.csv')
f2=open(r'C:\Users\zhang\Desktop\ml-latest-small\ratings.csv')
df1=pd.read_csv(f1)
df2=pd.read_csv(f2)
df = df1.append([df2],ignore_index=True)
a=df['userId'].nunique()
#print(a)
#一共有多少不同的电影
f=open(r'C:\Users\zhang\Desktop\ml-latest-small\movies.csv')
df=pd.read_csv(f)
b=df['movieId'].nunique()
#print(b)
#一共有多少不同的电影种类
c=df['genres'].nunique()
#print(c)
#一共有多少电影没有外部链接
f=open(r'C:\Users\zhang\Desktop\ml-latest-small\links.csv')
df=pd.read_csv(f)
e=df['movieId'].nunique()
f=b-e
#print(f)
#2018年一共有多少人进行过电影评分
for i in range(len(df2["timestamp"])):
    time_local = time.localtime(df2["timestamp"][i])
    df2["timestamp"][i] = time.strftime("%Y", time_local)
    #print(df2["timestamp"][i])
#print(df2["timestamp"])
df_2018 = df2[df2['timestamp'] == 2018]
#print(df_2018)
u = df_2018['userId'].nunique()
print("2018年一共有%d人进行过电影评分"%u)

