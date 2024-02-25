import pandas as pand
import matplotlib.pyplot as plit
import os

NAME = "App Titanic"
TITANIC_CSV_PATH = os.path.join(os.path.dirname(__file__), '..' ,'datasets', 'titanic.csv')

def get_name():
    return NAME

def main():
    titanic = pand.read_csv(TITANIC_CSV_PATH, index_col=0, parse_dates=True)
    
    titanic.plot.area(figsize=(12, 4), subplots=True)
    plit.show()
