import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中
plt .rcParams['axes.unicode_minus']=False     # 正常显示负号


x_df=pd.DataFrame(datasets.load_boston()['data'],columns=datasets.load_boston()['feature_names']) #X
y_df=pd.DataFrame(datasets.load_boston()['target'],columns=['y']) #Y
df=x_df.join(y_df)
#print(df.head())
RM=np.array(x_df["RM"])
DIS=np.array(x_df["DIS"])
PTRATIO=np.array(x_df["PTRATIO"])
LSTAT=np.array(x_df["LSTAT"])
Y=np.array(y_df)
fig = plt.figure()
ax = fig.add_subplot(221)
plt.scatter(RM, Y, marker='o', color='b', label='RM',s=20)
plt.xlabel("RM")
plt.ylabel('Y')
plt.legend(loc='upper right')
ax = fig.add_subplot(222)
plt.scatter(DIS, Y, marker='o', color='r', label='DIS',s=20)
plt.xlabel("DIS")
plt.ylabel('Y')
plt.legend(loc='upper right')
ax = fig.add_subplot(223)
plt.scatter(PTRATIO, Y, marker='o', color='y', label='PTRATIO',s=20)
plt.xlabel("PTRATIO")
plt.ylabel('Y')
plt.legend(loc='upper right')
ax = fig.add_subplot(224)
p4=plt.scatter(LSTAT, Y, marker='o', color='k', label='LSTAT',s=20)
plt.xlabel("PTRATIO")
plt.ylabel('Y')
plt.legend(loc='upper right')
#plt.show()

"从图中可以看出RM和Y具有线性"
###############################################################################
data=df[['RM','DIS','PTRATIO','LSTAT']]
x_train, x_test, y_train, y_test = train_test_split(data, y_df, test_size=0.2, random_state=1)
model = LinearRegression()
model.fit(x_train, y_train)
b=model.intercept_ #截距
w=model.coef_  #线性模型的系数
"回归方程为："
y=w[0][0]*df['RM']+w[0][1]*df['DIS']+w[0][2]*df['PTRATIO']+w[0][3]*df['LSTAT']+b
##############################################################################
"从图中可以看出RM和Y具有线性"
####################################################################################
a=[[8,2,12,22]]
pre=model.predict(a)
print("该小区房价为",pre[0][0])