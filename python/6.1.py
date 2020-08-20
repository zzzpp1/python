from itertools import product
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pydotplus
from IPython.display import Image, display
from sklearn import datasets
from sklearn import tree

X,y=datasets.load_iris(return_X_y=True) #X与y
target_names=datasets.load_iris().target_names #y的值列表:0:setosa,1:versicolor,2:virginica
feature_names=datasets.load_iris().feature_names #特征X的名称列表

x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=14)
print("训练数据集样本总数:%d;测试数据集样本总数:%d" %(x_train.shape[0],x_test.shape[0]))
ss = MinMaxScaler()
x_train = ss.fit_transform(x_train,y_train)
x_test = ss.transform(x_test)

clf = DecisionTreeClassifier(criterion="entropy",max_depth=3)
clf.fit(X, y) # 拟合模型
pre=clf.predict([[6,1,3,1]])
print(pre)
data = tree.export_graphviz(clf,out_file = None, feature_names = target_names['feature_names'],
                                class_names = target_names['target_names'],filled=True,rounded=True )
graph = pydotplus.graph_from_dot_data(data)
display(Image(graph.create_png()))
"可以看出最可能的种类是setosa"

