# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:23:09 2019

@author: matsm
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
import matplotlib.patches as mpatches


def positionOptions(pos):
    if pos == 'Goalkeeper':
        posoptions = ['GK']
    elif pos == 'Center Back':
        posoptions = ['RCB', 'RCB3', 'CB', 'LCB', 'LCB3']
    elif pos == 'Full Back':
        posoptions = ['LB', 'LB5', 'LWB', 'RB', 'RB5', 'RWB']
    elif pos == 'Defensive Midfielder':
        posoptions = ['DMF', 'LCMF', 'RCMF', 'LDMF', 'RDMF', 'LCMF3', 'RCMF3']
    elif pos == 'Attacking Midfielder':
        posoptions = ['AMF', 'LAMF', 'RAMF']
    elif pos == 'Winger':
        posoptions = ['RW','RWF','LWF','LW']
    elif pos == 'Striker':
        posoptions = ['CF']
    else:
        posoptions = ['']

    return posoptions


def positional_stats(position):
    """Defines the stats that should be in the radar plot. Different for each
    playing position"""

    if position == 'Center Back':
        labels = ['                         Defensive duels per 90',
                  '                                Tackles + interceptions (pAdj)\n\n',
                  '          Aerial duels won, % \n ',
                  'Aerial wins \n ',
                  'Pass accuracy (%)                           \n   ',
                  'Forward pass accuracy (%)                                        ',
                  'Long passes (%)                    ',
                  'Progressive passes (%)',
                  '\n                        Progressive runs per 90'
                  ]

    elif position == 'Full Back':
        labels = ['                              Defensive duels per 90',
                  '                                   Tackles + interceptions (pAdj)\n\n',
                  '          Aerial wins \n ',
                  'Pass accuracy (%)     \n    \n ',
                  'Forward pass accuracy (%)                                          ',
                  'Long passes (%)                          ',
                  'Progressive passes (%)                               ',
                  ' \n                        Progressive runs per 90',
                  '                        Dribbles completed per 90']


    elif position == 'Defensive Midfielder':
        labels = ['                              Defensive duels per 90',
                  '                                   Tackles + interceptions (pAdj)\n\n',
                  '          Aerial wins \n ',
                  'Pass accuracy (%)     \n    \n ',
                  'Forward pass accuracy (%)                                          ',
                  'Progressive passes (%)                               ',
                  'Passes to penalty area per 90                      ',
                  ' \n                        Progressive runs per 90',
                  '                        Dribbles completed per 90']


    elif position == 'Attacking Midfielder':
        labels = ['                             Defensive duels per 90',
                  '                                   Tackles + interceptions (pAdj)\n\n',
                  'xG/Shot \n',
                  'xG per 90  \n ',
                  'Shots per 90      \n    ',
                  'Touches in box per 90                       ',
                  'Dribbles completed per 90                        ',
                  'Passes to penalty area per 90',
                  '\n  xA per 90'
                  ]
    elif position == 'Winger':
        labels = ['                         Defensive duels per 90',
                  '                                   Tackles + interceptions (pAdj)\n\n',
                  'Aerial wins \n ',
                  'xG/Shot \n ',
                  'xG per 90 \n      ',
                  'Shots per 90       \n ',
                  'Touches in box per 90                  ',
                  'xA per 90  ',
                  '\n                        Dribbles completed per 90'
                  ]

    elif position == 'Striker':
        labels = ['                         Defensive duels per 90',
                  '                                   Tackles + interceptions (pAdj)\n\n',
                  'Aerial wins \n ',
                  'xG/Shot \n ',
                  'xG per 90 \n      ',
                  'Shots per 90       \n ',
                  'Touches in box per 90                  ',
                  'xA per 90  ',
                  '\n                        Dribbles completed per 90'
                  ]

    elif position == 'Goalkeeper':
        labels = ['                                  Save percentage',
                  '                                   Goals saved above expectation\n\n',
                  'Claim/punch ratio \n\n',
                  'Pass accuracy (%)                            \n   ',
                  'Forward pass accuracy (%)                                      ',
                  '\n       Long passes (%)']
    else:
        labels = []

    columns = []
    for i in range(len(labels)):
        columns.append(labels[i].strip())
        if 'per 90' in labels[i]:
            labels[i] = labels[i].replace('per 90', '')

    return columns, labels


def new_stats(stats):
    stats['% of passes not backwards'] = 100 - (stats['Back passes per 90'] / stats['Passes per 90'] * 100)
    stats['% of passes forward'] = (stats['Forward passes per 90'] / stats['Passes per 90']) * 100
    stats['Progressive passes (%)'] = (stats['Progressive passes per 90'] / stats['Passes per 90']) * 100
    stats['Long passes (%)'] = (stats['Long passes per 90'] / stats['Passes per 90']) * 100
    stats['Non-cross passes to box'] = stats['Passes to penalty area per 90'] - stats['Crosses per 90']
    stats['Dribbles completed per 90'] = stats['Dribbles per 90'] * (stats['Successful dribbles, %'] / 100)
    stats['Tackles + interceptions (pAdj)'] = stats['PAdj Interceptions'] + stats['PAdj Sliding tackles']
    stats['xG/Shot'] = stats['xG'] / stats['Shots']
    stats['Aerial wins'] = stats['Aerial duels per 90'] * (stats['Aerial duels won, %'] / 100)
    stats['Crosses completed per 90'] = stats['Crosses per 90'] * (stats['Accurate crosses, %'] / 100)
    try:
        stats['Goals saved above expectation'] = stats['xG against'] - stats['Goals total']
        stats = stats.rename(columns={'Save %': 'Save percentage',
                                      'Avg pass length, m': 'Avg pass length (m)'})
    except:
        print('This player is not a goalkeeper')

    stats = stats.rename(columns={'Def duels per 90': 'Defensive duels per 90',
                                  'Lng passes per 90': 'Long passes per 90',
                                  'Fwd passes acc. %': 'Forward pass accuracy (%)',
                                  'Passes acc. %': 'Pass accuracy (%)'})
    return stats

def invert(x, limits):
    """inverts a value x on a scale from
    limits[0] to limits[1]"""
    return limits[1] - (x - limits[0])


def scale_data(data, ranges):
    """scales data[1:] to ranges[0],
    inverts if the scale is reversed"""
    x1, x2 = ranges[0]
    d = data[0]
    if x1 > x2:
        d = invert(d, (x1, x2))
        x1, x2 = x2, x1
    sdata = [d]
    for d, (y1, y2) in zip(data[1:], ranges[1:]):
        if y1 > y2:
            d = invert(d, (y1, y2))
            y1, y2 = y2, y1
        sdata.append((d - y1) / (y2 - y1)
                     * (x2 - x1) + x1)
    return sdata


class ComplexRadar:
    def __init__(self, fig, variables, ranges,
                 n_ordinate_levels=6):
        angles = np.arange(0, 360, 360 / len(variables))

        axes = [fig.add_axes([0.1, 0.1, 0.9, 0.9], polar=True,
                             label=variables[i])
                for i in range(len(variables))]
        l, text = axes[0].set_thetagrids(angles,
                                         labels=variables, rotation=angles)

        for txt, angle in zip(text, angles):
            txt.set_rotation(angle - 90)
        for ax in axes[1:]:
            ax.patch.set_visible(False)
            ax.grid("off")
            ax.xaxis.set_visible(False)
        for i, ax in enumerate(axes):
            grid = np.linspace(*ranges[i],
                               num=n_ordinate_levels)
            if grid[1] - grid[0] < 0.1:
                gridlabel = ["{}".format(round(x, 2))
                             for x in grid]
            else:
                gridlabel = ["{}".format(round(x, 1))
                             for x in grid]

            # Case where grid labels aren't reversed
            if ranges[i][0] > ranges[i][1]:
                gridlabel[0] = ""  # clean up origin
            else:
                grid = grid[::-1]  # hack to invert grid
                gridlabel[0] = ""  # clean up origin
            ax.set_rgrids(grid, labels=gridlabel,
                          angle=angles[i])
            # ax.spines["polar"].set_visible(False)
            ax.set_ylim(*ranges[i])
        # variables for plotting
        self.angle = np.deg2rad(np.r_[angles, angles[0]])
        self.ranges = ranges
        self.ax = axes[0]
        self.labels = text
        self.axes = axes

    def plot(self, data, *args, **kw):
        sdata = scale_data(data, self.ranges)
        self.ax.plot(self.angle, np.r_[sdata, sdata[0]], *args, **kw)

    def fill(self, data, *args, **kw):
        sdata = scale_data(data, self.ranges)
        self.ax.fill(self.angle, np.r_[sdata, sdata[0]], *args, **kw)


def fetch_stat_list(xl, position):
    stat_list = xl
    stat_list = stat_list.set_index('Player')
    stat_list = new_stats(stat_list)
    positions = positionOptions(position)
    columns, labels = positional_stats(position)
    print(columns)
    stat_list = stat_list[stat_list['Main position'].isin(positions)]

    return stat_list

def run(position,file_dir,name1,name2,stat_list,season):

    positions = positionOptions(position)
    columns, labels = positional_stats(position)
    title = {'fontname': 'DejaVu Sans', 'weight': 'bold'}

    stats = stat_list.loc[name1, columns].values
    stats2 = stat_list.loc[name2, columns].values

    ranges = []

    for i in range(len(columns)):
        ranges.append((stat_list[columns[i]].min(), stat_list[columns[i]].quantile(0.95)))
        if stats[i] < ranges[i][0]:
            stats[i] = ranges[i][0]
        elif stats[i] > ranges[i][1]:
            stats[i] = ranges[i][1]
        if stats2[i] < ranges[i][0]:
            stats2[i] = ranges[i][0]
        elif stats2[i] > ranges[i][1]:
            stats2[i] = ranges[i][1]

    # determine directory
    path = os.getcwd()


    if path[0] == '/':
        filename = file_dir + '/radar.png'
    else:
        filename = file_dir + '\\radar.png'

    name = name1



    if type(stat_list.loc[name, 'Team']) == float:
        stat_list.loc[name, 'Team'] = 'Free agent'

    # Plotting
    fig1 = plt.figure(figsize=(6, 6))
    radar = ComplexRadar(fig1, labels, ranges)

    radar.plot(stats, color='#E23D46', label=name1)
    radar.fill(stats, alpha=0.2, color='#E23D46')
    radar.plot(stats2, label=name2)
    radar.fill(stats2, alpha=0.2)
    fig1.text(0.55, 1.18, name1 + ' and ' + name2, **title, color='#E23D46', fontsize='18', ha='center', va='bottom')
    fig1.text(0.55, 1.13, position, color='black', fontsize='14', ha='center', va='bottom')
    fig1.text(0.55, 1.09, stat_list.loc[name1, 'Team'] + ' and ' + stat_list.loc[name2, 'Team'] + ', ' + season,
              color='black', fontsize='14', ha='center', va='bottom')

    name1patch = mpatches.Patch(color='#E23D46', label=name1)
    name2patch = mpatches.Patch(color='blue', label=name2)
    plt.legend(handles=[name1patch, name2patch], bbox_to_anchor=(0, 1))

    if path[0] == '/':
        im1 = image.imread(os.getcwd() + '/app/Images/Logo_Tactalyse_Stats.png')
    else:
        im1 = image.imread(os.getcwd() + '\\app\\Images\\Logo_Tactalyse_Stats.png')
    logo_ax = fig1.add_axes([0.2, -0.08, 0.7, 0.09])
    logo_ax.imshow(im1, aspect='auto', extent=(0, 1000, 0, 300))
    logo_ax.set_xlim(left=0, right=1000)
    logo_ax.axis('off')

    plt.savefig(filename, bbox_inches='tight')
    plt.close()

    return filename
