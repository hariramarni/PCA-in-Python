# PCA code for analysing the health of turbomachines
import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
test = ['test'+ str(i) for i in range(1,101)]
ao = ['62PDI1202.PV']
bo = ['62TI3246.PV']
co = ['62PDI3226.PV']
do = ['62HIC3225.MV']
eo = ['62TI3230.PV']
fo = ['62TI3231.PV']
go = ['62TI3208.PV']
ho = ['62TI3215.PV']
io = ['62PI3226.PV']
jo = ['62UI3226.PV']
ko = ['62FI1211A.PV']
lo = ['62FQI1404.PV']
mo = ['62ZSL3201B.PV']
no = ['62ZSL3201A.PV']
po = ['62TI1515.PV']
qo = ['62PI1510.PV']
ro = ['62HIC3204.MV']
so = ['62TI3205.PV']
to = ['62TI1511.PV']
uo = ['E62TI1512.PV']
vo = ['62FQI1516.PV']

data = pd.DataFrame(columns=[*ao, *bo, *co, *do, *eo, *fo, *go, *ho, *io, *jo, *ko, *lo, *mo, *no, *po, *qo, *ro, *so, *to, *uo, *vo ], index=test)
for test in data.index:
	data.loc[test,'62PDI1202.PV'] = np.random.poisson(lam=rd.randrange(0,1), size=1)
	data.loc[test,'62TI3246.PV'] = np.random.poisson(lam=rd.randrange(12,15), size=1)
	data.loc[test,'62PDI3226.PV'] = np.random.poisson(lam=rd.randrange(2,3), size=1)
	data.loc[test,'62HIC3225.MV'] = np.random.poisson(lam=rd.randrange(99,100), size=1)
	data.loc[test,'62TI3230.PV'] = np.random.poisson(lam=rd.randrange(132,138), size=1)
	data.loc[test,'62TI3231.PV'] = np.random.poisson(lam=rd.randrange(20,25), size=1)
	data.loc[test,'62TI3208.PV'] = np.random.poisson(lam=rd.randrange(82,85), size=1)
	data.loc[test,'62TI3215.PV'] = np.random.poisson(lam=rd.randrange(28,32), size=1)
	data.loc[test,'62PI3226.PV'] = np.random.poisson(lam=rd.randrange(745,755), size=1)
	data.loc[test,'62UI3226.PV'] = np.random.poisson(lam=rd.randrange(18,19), size=1)
	data.loc[test,'62FI1211A.PV'] = np.random.poisson(lam=rd.randrange(87000,89000), size=1)
	data.loc[test,'62FQI1404.PV'] = np.random.poisson(lam=rd.randrange(12000,14000), size=1)
	data.loc[test,'62ZSL3201B.PV'] = np.random.poisson(lam=rd.randrange(0,1), size=1)
	data.loc[test,'62ZSL3201A.PV'] = np.random.poisson(lam=rd.randrange(0,1), size=1)
	data.loc[test,'62TI1515.PV'] = np.random.poisson(lam=rd.randrange(298,303), size=1)
	data.loc[test,'62PI1510.PV'] = np.random.poisson(lam=rd.randrange(550,557), size=1)
	data.loc[test,'62HIC3204.MV'] = np.random.poisson(lam=rd.randrange(99,100), size=1)
	data.loc[test,'62TI3205.PV'] = np.random.poisson(lam=rd.randrange(212,216), size=1)
	data.loc[test,'62TI1511.PV'] = np.random.poisson(lam=rd.randrange(99,101), size=1)
	data.loc[test,'E62TI1512.PV'] = np.random.poisson(lam=rd.randrange(100,105), size=1)
	data.loc[test,'62FQI1516.PV'] = np.random.poisson(lam=rd.randrange(95,105), size=1)

print(data.head())
print(data.shape)
scaled_data = preprocessing.scale(data.T)
pca = PCA()
pca.fit(scaled_data)
PCA()
pca_data = pca.transform(scaled_data)
per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]
plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()



 


