Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import random as rd

>>> from sklearn.decomposition import PCA
>>> from sklearn import preprocessing
>>> import matplotlib.pyplot as plt
>>> genes = ['gene' + str(i) for i in range(1,101)]
>>> wt = ['wt' + str(i) for i in range(1,6)]
>>> ko = ['ko' + str(i) for i in range(1,6)]
>>> data = pd.DataFrame(columns=[*wt, *ko], index=genes)
>>> for gene in data.index:
	data.loc[gene,'wt1':'wt5'] = np.random.poisson(lam=rd.randrange(10,1000), size=5)
	data.loc[gene,'ko1':'ko5'] = np.random.poisson(lam=rd.randrange(10,1000), size=5)

>>> print(data.head())
       wt1  wt2  wt3  wt4  wt5  ko1  ko2  ko3  ko4  ko5
gene1   41   55   54   55   39   14   17   12   14   24
gene2  928  981  907  942  869  837  879  864  832  877
gene3  699  634  639  661  718  736  766  756  745  787
gene4  200  187  197  179  192  809  824  850  829  815
gene5   90   86   83   80   72  392  423  422  389  389
>>> print(data.shape)
(100, 10)
>>> scaled_data = preprocessing.scale(data.T)
>>> pca = PCA()
>>> pca.fit(scaled_data)
PCA()
>>> pca_data = pca.transform(scaled_data)
>>> per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
>>> labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]
>>> plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
<BarContainer object of 10 artists>
>>> plt.ylabel('Percentage of Explained Variance')
Text(0, 0.5, 'Percentage of Explained Variance')
>>> plt.xlabel('Principal Component')
Text(0.5, 0, 'Principal Component')
>>> plt.title('Scree Plot')
Text(0.5, 1.0, 'Scree Plot')
>>> plt.show()
>>> plt.show()
>>> pca_df = pd.DataFrame(pca_data, index=[*wt, *ko], columns=labels)
>>> plt.scatter(pca_df.PC1, pca_df.PC2)
<matplotlib.collections.PathCollection object at 0x126036970>
>>> plt.title('My PCA Graph')
Text(0.5, 1.0, 'My PCA Graph')
>>> plt.xlabel('PC1 - {0}%'.format(per_var[0]))
Text(0.5, 0, 'PC1 - 90.4%')
>>> plt.ylabel('PC2 - {0}%'.format(per_var[1]))

Text(0, 0.5, 'PC2 - 2.7%')
>>> plt.ylabel('PC2 - {0}%'.format(per_var[1]))

Text(0, 0.5, 'PC2 - 2.7%')
>>> for sample in pca_df.index
SyntaxError: invalid syntax
>>> for sample in pca_df.index:
	 plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))

	 
Text(-8.945287186159572, 0.3629474275530417, 'wt1')
Text(-9.943709587962807, -1.0187399546328857, 'wt2')
Text(-9.84793212909629, -0.14122826540745687, 'wt3')
Text(-9.748513961492732, -1.9480339184013895, 'wt4')
Text(-9.022493309022536, 2.9738046549568358, 'wt5')
Text(9.437705079776388, 0.6863440170569319, 'ko1')
Text(9.167654657725098, -1.8731968849035492, 'ko2')
Text(9.650859020181473, -1.1207856554899003, 'ko3')
Text(9.298257767920854, -0.589475709809513, 'ko4')
Text(9.953459648130115, 2.6683642890778834, 'ko5')
>>> plt.show()
>>> plt.show()
