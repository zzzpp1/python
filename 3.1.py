import numpy as np
import pandas as pd
#第一问
f=open(r'C:\Users\zhang\Desktop\ml-latest-small\ratings.csv')
df=pd.read_csv(f)
bins=[0,1,2,3,4,5]
a=pd.cut(df["rating"],bins).value_counts()
#c=list(a)
#print(a)
#print(c)

#第二问
df["comment"]=np.where(df.rating>=4,"推荐","不推荐")
#print(df.head())
df.to_csv(r'C:\Users\zhang\Desktop\python\作业\comment.csv', index=False)

