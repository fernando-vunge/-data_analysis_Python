import pandas as pand
import matplotlib.pyplot as plit

NAME = "App Titanic"
def get_name():
    return NAME

def main():
    #self.air_quality = pand.read_csv('../datasets/air_quality_no2.csv', index_col=0, parse_dates=True)
    print("ola titanic")
    #print(self.air_quality.head())
'''


tdata = pand.read_csv('datasets/titanic_dataset.csv', index_col=0, parse_dates=True)
tdata.loc[tdata['Age'].isna(), 'Name'] = 'anonymous'

print(tdata.loc[tdata['Age'].isna(), ['Name','Age']])

num_females = tdata[tdata['Sex'].isin(["female"])].shape[0]
num_males = tdata[tdata['Sex'].isin(["male"])].shape[0]
num_ageed = tdata[tdata['Age'].notna()].shape[0]

column([
    f"Numero de mulheres : {num_females}",
    f"Numero de homens : {num_males}",
    f"Numero de passageiros com idade registada : {num_ageed}",
])
'''