import io
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from ...data import preprocessor
from .abstract_models import Graph

class ScattterPlot(Graph):
    __position = ''
    
    def __init__(self, player_pos=None):
        if player_pos:
            self.__position = player_pos
    
    def draw(self, data):
        fig, ax = plt.subplots()
        ax.clear()
        sns.regplot(x = data.columns[1], y = data.columns[0], data = data)
        buffer = io.BytesIO()
        plt.savefig(buffer, format = 'png')
        buffer.seek(0)
        return buffer.getvalue()
        