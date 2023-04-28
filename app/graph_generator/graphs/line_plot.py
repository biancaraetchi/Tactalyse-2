import io

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from .abstract_models import Graph


class LinePlot(Graph):
    __position = ''

    def __init__(self, player_pos=None):
        if player_pos:
            self.__position = player_pos

    def get_xlabels(self, date):
        date = date.str.slice(start=2, stop=4)
        unique_dates = date.unique()
        unique_date_int = [int(i) for i in unique_dates]
        unique_date_int_plus_one = [x + 1 for x in unique_date_int]
        labels = []
        for i in range(len(unique_dates)):
            labels.append(str(unique_date_int[i]) + "/" + str(unique_date_int_plus_one[i]))
        start_years = []
        for i in range(len(unique_dates)):
            numbers = date[date == unique_dates[i]]
            start_years.append(len(date) - numbers.index[len(numbers) - 1] - 1)
        start_years.reverse()
        locations = []
        for i in range(len(start_years)):
            if i != len(start_years) - 1:
                locations.append((start_years[i] + start_years[i + 1]) / 2)
            else:
                locations.append((start_years[i] + len(date)) / 2)
        locations.reverse()
        start_years.reverse()

        return labels, locations, start_years

    def draw(self, data, column_names):
        date = data["Date"]
        labels, locations, start_years = self.get_xlabels(date)
        data = data[column_names]
        fig = plt.figure()
        ax = plt.axes()
        ax.plot(date, data["Interceptions"], marker='o')
        plt.title("Interceptions per 90 minutes")
        ax.set_xticks(locations, labels)
        mean = np.mean(data["Interceptions"])
        plt.axhline(y=mean, linestyle="dashed", label="Mean")
        for i in start_years:
            plt.axvline(x=i, linestyle="dashed", color='g')
        plt.legend()
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        return buffer.getvalue()

    # def draw(self, data, column_names):
    #     temp_start_date =  16/17
    #     temp_end_date = 20/21
    #     date = date["Date"]
    #     labels, locations, start_years = self.get_xlabels(date)
    #     data = data[column_names]
    #     fig, ax = plt.subplots()
    #     sns.lineplot(x=date, y=data["Interceptions"], marker = 'o', ax = ax)
    #     ax.set(title="Interceptions per 90 minutes", xticks = locations, xticklabes = labels)
    #     mean = np.mean(data["Interceptions"])
    #     # ax.axhline(y = mean, linestyle="dashed", label = "Mean", color = "black")
    #     sns.lineplot(x=date,  y=mean, ax=ax, linestyle="dashed", label="Mean", color = "black")
    #     for i in start_years:
    #         ax.axvline(x=i, linestyle="dashed", color='g')
    #     ax.axvline(x = temp_start_date, linestyle = "dashed", color = 'r')
    #     ax.axvline(x = temp_end_date, linestyle = "dashed", color = 'r')
    #     ax.legend()
    #     buffer = io.BytesIO()
    #     plt.savefig(buffer, format = 'png')
    #     buffer.seek(0)
    #     return buffer.getvalue()

