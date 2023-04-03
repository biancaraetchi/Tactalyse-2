from .abstract_models import Graph
import matplotlib.pyplot as plt
import numpy as np
import io

class LinePlot(Graph):
    __position = ''
    def __init__(self, player_pos=None):
        if player_pos:
            self.__position = player_pos

    def draw(self, data, column_names):
        date = data["Date"]
        data = data[column_names]
        #I'll generate a single line graph for now, I'm not sure how to group them efficiently for now..
        fig = plt.figure()
        ax = plt.axes()
        ax.plot(date,data["Interceptions"], marker='o')
        plt.title("Interceptions per 90 minutes")
        plt.legend()
        ax.set_xticks(["1","2","3"])
        mean=np.mean(data["Interceptions"])
        plt.axhline(y=mean, linestyle="dashed")
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        return buffer.getvalue()