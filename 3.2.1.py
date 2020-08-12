import pandas as pd
import numpy as np
d = {
    'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
for key,value in df.iteritems():
    for key1,value1 in value.iteritems():
        if value1>3:
            df[key][key1]=value1**value1
r1=df
print(r1)
r2=df[(df.one==1) | (df.one==4) | (df.two==4) | (df.two==1) ]
print(r2)
r3=df.sample(axis=1)
print(r3)
df['add']=df['one']+df['two']
r4=df["add"]
print(r4)
r5=df[df.one>2]
print(r5)
