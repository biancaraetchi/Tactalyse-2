import io
import re
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import seaborn as sns
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from .abstract_models import Graph

class BarPlotBase(Graph):
    """
    Class that acts as base class for all bar plots and provides default values for attributes.
    """
    __main_pos = ''
    __position_name = ''
    __compare_pos = ''
    __orientation = 'v'
    __player_name = ''
    __compare_name = None

    def are_comparable(self, cmp_name, pos, cmp_pos):
        """
        Functions that checks whether the players being compared are in a set of positions
        that share the same main statistics.
        :param cmp_name: the name of the player that's being compared.
        :param pos: the first player's position.
        :param cmp_pos: the position of the player that's being compared.
        :return: True if there is no comparison or if the players are comparable.
        """
        if cmp_name != None:
            comparable_1 = ['Attacking Midfielder', 'Winger', 'Striker']
            comparable_2 = ['Full Back', 'Center Back', 'Defensive Midfielder']
            if ((pos in comparable_1 and cmp_pos in comparable_2) or 
                (pos in comparable_2 and cmp_pos in comparable_1)):
                return False
        return True
    
    def get_stats_superset(self):
        """
        :return: the union of sets of main statistics for attacking and defensive positions.
        """
        return ['Goals per 90', 'Offensive duels per 90',
                    'Defensive duels per 90', 'Fouls per 90',
                    'Interceptions per 90', 'Crosses per 90', 
                    'Dribbles per 90', 'Progressive runs per 90',
                    'Assists per 90']