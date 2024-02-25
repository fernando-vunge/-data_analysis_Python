import pandas as pand
import matplotlib.pyplot as plit

class AppNO2:
    name = "App Air Quality NO2"
    air_quality = pand.read_csv('../datasets/air_quality_no2.csv', index_col=0, parse_dates=True)
    
    def main(self) -> None:
        print(self.air_quality.head())