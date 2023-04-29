import io
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from .abstract_models import Graph


class BarPlot(Graph):
    
    __position = ''
    __orientation = 'v'
    __player_name = ''


    def __init__(self, player_name, player_pos=None, orientation='v'):
        if player_pos:
            self.__position = player_pos
            self.__orientation = orientation
            self.__player_name = player_name
        
        
    def draw(self, data, stat):
    


        player_vs_avg_data = {' ': [self.__player_name, 'League average'], stat: [9, 6]}       
        df = pd.DataFrame(player_vs_avg_data)
        plt.subplot().clear()
        sns.barplot(x=" ", y=stat, data=df, orient=self.__orientation)
        buffer = io.BytesIO()
      
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        return buffer.getvalue()
