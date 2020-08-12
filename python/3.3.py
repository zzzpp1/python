import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #导入图形库
plt.rcParams['font.sans-serif']=['Simhei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

f=open(r'C:\Users\zhang\Desktop\bank_data.csv')
df=pd.read_csv(f)
print(df.info())
a=df.isnull().any() #计算17个指标中有没有缺失值
print(a)

plt.boxplot(x=df.age,  # 指定绘图数据
            patch_artist=True,  # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True,  # 以点的形式显示均值
            boxprops={'color': 'black', 'facecolor': '#9999ff'},  # 设置箱体属性，填充色和边框色
            flierprops={'marker': 'o', 'markerfacecolor': 'red', 'color': 'black'},  # 设置异常值属性，点的形状、填充色和边框色
            meanprops={'marker': 'D', 'markerfacecolor': 'indianred'},  # 设置均值点的属性，点的形状、填充色
            medianprops={'linestyle': '--', 'color': 'orange'})  # 设置中位数线的属性，线的类型和颜色
# 设置y轴的范围
plt.ylim(10, 65)

# 去除箱线图的上边框与右边框的刻度标签
plt.tick_params(top='off', right='off')
#plt.show()

