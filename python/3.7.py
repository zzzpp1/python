#encoding=utf-8
import pandas as pd
import numpy as np
import time
import os
import csv
import matplotlib.pyplot as plt
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
#评分5分以上的电影及其标签
f1=open(r'G:\数据\ml-latest-small\ratings.csv')
f2=open(r'G:\数据\ml-latest-small\tags.csv')
df1=pd.read_csv(f1)
df2=pd.read_csv(f2)
out_csv=pd.concat([df1,df2],axis=0)
#print(out_csv)
def convert(timestamp):
    timeArray = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y", timeArray)
    #print(otherStyleTime)
    return otherStyleTime
out_csv["timestamp"]=out_csv["timestamp"].apply(convert)
#print(out_csv)
a=out_csv[(out_csv["rating"]>=5)&(out_csv["timestamp"]=='2018')]
b=a.drop_duplicates(subset=['movieId'])
print("评分5分以上的电影及其标签")
print(b)
#复仇者联盟的评分
f=open(r'G:\数据\ml-latest-small\ratings.csv')
df=pd.read_csv(f)
def converts(timestamp):
    timeArray = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y%m", timeArray)
    #print(otherStyleTime)
    return int(otherStyleTime)
df["timestamp"]=df["timestamp"].apply(converts)
score_260=df[(df["movieId"]==260)]
score_260.sort_values(by=['timestamp'], ascending=True, inplace=True)
print(score_260)
plt.plot(score_260['timestamp'],score_260['rating'])
font2 = {'family': 'Times New Roman',
                  'size': 20,}
plt.ylabel("The rating of movie",font2)
plt.xlabel("MovieId 260",font2)
plt.show()