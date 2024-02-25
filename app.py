import pandas as pand
from utils_module.utils import *


tdata = pand.read_csv('datasets/titanic_dataset.csv')

ln()
print(tdata.iloc[0:9, 3:5])
ln()
print(tdata.loc[(tdata['Age'] < 18) & tdata['Sex'].isin(['male']), ['Name','Sex','Age']])
ln()


num_females = tdata[tdata['Sex'].isin(["female"])].shape[0]
num_males = tdata[tdata['Sex'].isin(["male"])].shape[0]
num_ageed = tdata[tdata['Age'].notna()].shape[0]

column([
    f"Numero de mulheres : {num_females}",
    f"Numero de homens : {num_males}",
    f"Numero de passageiros com idade registada : {num_ageed}",
])
