#Supervisors take on PCA Code
# -*- coding: utf-8 -*-
"""
# PCA from csv dataset

"""
# impor required libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

# importing or loading the dataset  - change the file path as needed
dataset = pd.read_csv(r'/Users/user/Desktop/Data.csv') 

# (optional) print data to check that it has been correctly imported
print(dataset)

# PCA
from sklearn.decomposition import PCA
from sklearn import preprocessing

# Pre-process the data
sdata = preprocessing.scale(dataset)
pca = PCA(n_components=2)
pca.fit(sdata)

# show principal components
print(pca.components_)

# show the explained variance
print(pca.explained_variance_)

# scatter plot
# plot data
plt.scatter(sdata[:, 0], sdata[:, 1], alpha=0.2)
