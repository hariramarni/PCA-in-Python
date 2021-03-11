# Test code for dataset provided by XlnControl.
# Irregularities obtained while comparing Factor loadings.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import preprocessing
dataset = pd.read_csv(r'/Users/hariramarni/Desktop/PCAtest.csv')
print(dataset)
scaled_data = preprocessing.scale(dataset)
pca = PCA()
pca.fit(scaled_data)
pca_data = pca.transform(scaled_data)
per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
cov_matrix = np.cov(scaled_data.T)
print('cov_matrix =',cov_matrix)  
plt.show()
values,vector = np.linalg.eig(cov_matrix)
print('values =', values)
print('vector =', vector)
labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]
plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()
pca_df = pd.DataFrame(pca_data, columns= labels)
plt.scatter(pca_df.PC1, pca_df.PC2)
plt.title('My PCA Graph')
plt.xlabel('PC1 - {0}%'.format(per_var[0]))
plt.ylabel('PC2 - {0}%'.format(per_var[1]))
for sample in pca_df.index:
    plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))
plt.show()
loading_scores = pd.Series(pca.components_[0],index= labels)
#sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)
#Malfunction = sorted_loading_scores[0:110].index.values
#print(loading_scores[Malfunction])
print(loading_scores)
