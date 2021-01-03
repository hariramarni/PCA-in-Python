import pandas as pd
import numpy as np
import random as rd

from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
test = ['test']
Tag1= ['62PDI1202.PV']
Tag2= ['62TI3246.PV']
Tag3= ['62PDI3226.PV']
Tag4= ['62HIC3225.MV']
Tag5= ['62TI3230.PV']
Tag6= ['62TI3231.PV']
Tag7= ['62TI3208.PV']
Tag8= ['62TI3215.PV']
Tag9= ['62PI3226.PV']
Tag10= ['62UI3226.PV']
Tag11= ['62FI1211A.PV']
Tag12= ['62FQI1404.PV']
Tag13= ['62ZSL3201B.PV']
Tag14= ['62ZSL3201A.PV']
Tag15= ['62TI1515.PV']
Tag16= ['62PI1510.PV']
Tag17= ['62HIC3204.MV']
Tag18= ['62TI3205.PV']
Tag19= ['62TI1511.PV']
Tag20= ['E62TI1512.PV']
Tag21= ['62FQI1516.PV']
data = pd.DataFrame(columns=[*Tag1,*Tag2,*Tag3
,*Tag4,*Tag5,*Tag6,*Tag7,*Tag8,*Tag9,*Tag10,*Tag11,*Tag12,*Tag13,*Tag14,*Tag15,*Tag16,*Tag17,*Tag18,*Tag19,*Tag20,*Tag21 ], index=test)
for test in data.index:
    data.loc[test, '62PDI1202.PV']=np.random.poisson(lam=rd.randrange(0.469615), size=1)
    data.loc[test, '62TI3246.PV']=np.random.poisson(lam=rd.randrange(12.3538), size=1)
    data.loc[test, '62PDI3226.PV']=np.random.poisson(lam=rd.randrange(2.56503), size=1)
    data.loc[test, '62HIC3225.MV']=np.random.poisson(lam=rd.randrange(100), size=1)
    data.loc[test, '62TI3230.PV']=np.random.poisson(lam=rd.randrange(134.28), size=1)
    data.loc[test, '62TI3231.PV']=np.random.poisson(lam=rd.randrange(23.787), size=1)
    data.loc[test, '62TI3208.PV']=np.random.poisson(lam=rd.randrange(82.4523), size=1)
    data.loc[test, '62TI3215.PV']=np.random.poisson(lam=rd.randrange(29.5771), size=1)
    data.loc[test, '62PI3226.PV']=np.random.poisson(lam=rd.randrange(750.87), size=1)
    data.loc[test, '62UI3226.PV']=np.random.poisson(lam=rd.randrange(18.7095), size=1)
    data.loc[test, '62FI1211A.PV']=np.random.poisson(lam=rd.randrange(87181.9), size=1)
    data.loc[test, '62FQI1404.PV']=np.random.poisson(lam=rd.randrange(13534.3), size=1)
    data.loc[test, '62ZSL3201B.PV']=np.random.poisson(lam=rd.randrange(1), size=1)
    data.loc[test, '62ZSL3201A.PV']=np.random.poisson(lam=rd.randrange(0), size=1)
    data.loc[test, '62TI1515.PV']=np.random.poisson(lam=rd.randrange(300.079), size=1)
    data.loc[test, '62PI1510.PV']=np.random.poisson(lam=rd.randrange(556.08), size=1)
    data.loc[test, '62HIC3204.MV']=np.random.poisson(lam=rd.randrange(100), size=1)
    data.loc[test, '62TI3205.PV']=np.random.poisson(lam=rd.randrange(212.269), size=1)
    data.loc[test, '62TI1511.PV']=np.random.poisson(lam=rd.randrange(100.733), size=1)
    data.loc[test, 'E62TI1512.PV']=np.random.poisson(lam=rd.randrange(101.9), size=1)
    data.loc[test, '62FQI1516.PV']=np.random.poisson(lam=rd.randrange(99.5177), size=1)
print(data.head())
print(data.shape)
