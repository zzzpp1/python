import os
import numpy as np
import pandas as pd

f=open(r'C:\Users\zhang\Desktop\ml-latest-small\ratings.csv')
df=pd.read_csv(f)
df['mean']=df.groupby("movieId")["rating"].mean()
df.to_csv(r'C:\Users\zhang\Desktop\1\rate.csv', index=False)

path = r'C:\Users\zhang\Desktop\1'   #设置csv所在文件夹
files = os.listdir(path)  #获取文件夹下所有文件名
pd.options.display.max_columns = None
pd.options.display.max_rows = None

np.set_printoptions(threshold=np.inf)
df1 = pd.read_csv(path + '/' + files[0],encoding='gbk')  #读取首个csv文件，保存到df1中

for file in files[1:]:
  df2 = pd.read_csv(path +'/' +  file,encoding='gbk')  #打开csv文件，注意编码问题，保存到df2中
  df1 = pd.concat([df1,df2],axis=0,ignore_index=True)  #将df2数据与df1合并

df1 = df1.drop_duplicates()   #去重
df1 = df1.reset_index(drop=True) #重新生成index
print(df1.head())
