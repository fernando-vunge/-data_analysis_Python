import pandas as pand
import matplotlib.pyplot as plit
import os

NAME = "App Air Quality NO2"
AIR_QUALITY_CSV_PATH = os.path.join(os.path.dirname(__file__), '..' ,'datasets', 'air_quality_no2.csv')

def get_name():
    return NAME

def main():
    air_quality = pand.read_csv(AIR_QUALITY_CSV_PATH, index_col=0, parse_dates=True)
    
    print(air_quality.head())
    air_quality.plot()
    plit.show()