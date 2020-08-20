import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn import datasets
df=pd.DataFrame(datasets.load_iris()['data'],columns=datasets.load_iris()['feature_names'])

k_means = KMeans(n_clusters=3, random_state=10)
k_means.fit(df)
pre= k_means.predict(df)
print(pre)
center=k_means.cluster_centers_
print(center)
plt.scatter(df[:,0],df[:,2],c=pre)
plt.show()
