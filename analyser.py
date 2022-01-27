import pandas as pd
import plotly.express as px


class Analyser:
    def __init__(self,
                 csv_path="stashFinder.csv",
                 min_minecratrs=0,
                 min_chests=0,
                 min_shulkers=0):
        self.csv_path = csv_path

        self.data = pd.read_csv(csv_path)
        self.data.columns = self.data.columns.str.replace(' ', '')

        self.min_minecratrs = min_minecratrs
        self.min_chests = min_chests
        self.min_shulkers = min_shulkers

    def __clean_data(self,
                     data,
                     min_minecratrs,
                     min_chests,
                     min_shulkers):
        data_cleaned = data.loc[
            data['chests'] >= min_chests
            ].loc[
            data['minecarts'] >= min_minecratrs
            ].loc[
            data['shulkers'] >= min_shulkers
            ]
        return data_cleaned

    def show_plot(self):
        print("Cleaning data")
        data_cleaned = self.__clean_data(self.data, self.min_minecratrs, self.min_chests, self.min_shulkers)
        print("Opening the graph")
        fig = px.scatter(data_cleaned, x='x', y='z', color='server', title='coordinates')
        fig.show()
