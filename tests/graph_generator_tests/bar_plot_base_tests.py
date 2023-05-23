from app.graph_generator.graphs.bar_plot_base import *

def test_get_stats_superset(self):
    obj = BarPlotBase()
    list = ['Goals per 90', 'Offensive duels per 90',
                    'Defensive duels per 90', 'Fouls per 90',
                    'Interceptions per 90', 'Crosses per 90', 
                    'Dribbles per 90', 'Progressive runs per 90',
                    'Assists per 90']
    assert list == obj.get_stats_superset(), 'incorrect list'
