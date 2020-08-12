import pandas as pd
import numpy as np
from sklearn import  datasets
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
iris = datasets.load_iris()

X = iris.data
y = iris.target
X1 = iris.data[: , :2]
a=plt.scatter(X1[y==0, 0],X1[y==0, 1],color='b',marker='o')
b=plt.scatter(X1[y==1, 0],X1[y==1, 1],color='y',marker='o')
c=plt.scatter(X1[y==2, 0],X1[y==2, 1],color='r',marker='o')
plt.xlabel('sepal width')
plt.ylabel('sepal length')
plt.legend(handles=[a,b,c], labels=['Iris-setosa',"Iris-virginica" ,'Iris-versicolor'],  loc='best')
plt.show()

X2 = iris.data[: , 2:]
a=plt.scatter(X2[y==0, 0],X2[y==0, 1],color='b',marker='o')
b=plt.scatter(X2[y==1, 0],X2[y==1, 1],color='y',marker='o')
c=plt.scatter(X2[y==2, 0],X2[y==2, 1],color='r',marker='o')
plt.xlabel('petal width')
plt.ylabel('petal length')
plt.legend(handles=[a,b,c], labels=['Iris-setosa',"Iris-virginica" ,'Iris-versicolor'],  loc='best')
plt.show()