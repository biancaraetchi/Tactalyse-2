"""
This script is for reading an excel file with player statistics downloaded
from Wyscout. The excel file should have been downloaded with the stats
package: all stats.

Yields a DataFrame with all the necessary statistics
@author: Maksym Kadiri
@author: Pierre Chang
"""
import os
import sys
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import controller.ScoutForm
import controller.FileHandler


def createDF(filestream):
    """
    reads excel file without stats and turns it into a data frame
    """
    xl = pd.ExcelFile(file)
    stats = xl.parse('PlayerStats')

    stats.insert(0, 'Home', 0)
    stats.insert(1, 'Away', 0)
    stats.insert(2, 'Home_Score', 0)
    stats.insert(3, 'Away_Score', 0)

    for i in range(len(stats)):
        if stats.Match[i].endswith(')'):
            Match, Score, P = stats.Match[i].rsplit(' ', 2)
        else:
            Match, Score = stats.Match[i].rsplit(' ', 1)

        stats.loc[i, 'Home'], stats.loc[i, 'Away'] = Match.split(' - ')
        stats.loc[i, 'Home_Score'], stats.loc[i, 'Away_Score'] = Score.split(':', 1)

        y, m, d = stats['Date'][i].split('-')
        stats.loc[i, 'Date'] = datetime.date(int(y), int(m), int(d))

    stats.rename(columns={'Total actions / successful': 'Total actions',
                          'Unnamed: 6': 'Successful actions',
                          'Shots / on target': 'Shots',
                          'Unnamed: 10': 'Shots on target',
                          'Passes / accurate': 'Passes',
                          'Unnamed: 13': 'Accurate passes',
                          'Long passes / accurate': 'Long passes',
                          'Unnamed: 15': 'Accurate long passes',
                          'Crosses / accurate': 'Crosses',
                          'Unnamed: 17': 'Accurate crosses',
                          'Dribbles / successful': 'Dribbles',
                          'Unnamed: 19': 'Successful dribbles',
                          'Duels / won': 'Duels',
                          'Unnamed: 21': 'Duels won',
                          'Aerial duels / won': 'Aerial duels',
                          'Unnamed: 23': 'Aerial duels won',
                          'Losses / own half': 'Losses',
                          'Unnamed: 26': 'Losses own half',
                          'Recoveries / opp. half': 'Recoveries',
                          'Unnamed: 28': 'Recoveries opp half',
                          'Defensive duels / won': 'Defensive duels',
                          'Unnamed: 32': 'Defensive duels won',
                          'Loose ball duels / won': 'Loose ball duels',
                          'Unnamed: 34': 'Loose ball duels won',
                          'Sliding tackles / successful': 'Sliding tackles',
                          'Unnamed: 36': 'Successful sliding tackles',
                          'Offensive duels / won': 'Offensive duels',
                          'Unnamed: 43': 'Offensive duels won',

                          'Through passes / accurate': 'Through passes',
                          'Unnamed: 49': 'Accurate through passes',

                          'Passes to final third / accurate': 'Passes to final third',
                          'Unnamed: 53': 'Accurate passes to final third',
                          'Passes to penalty area / accurate': 'Passes to penalty area',
                          'Unnamed: 55': 'Accurate passes to penalty area',
                          'Forward passes / accurate': 'Forward passes',
                          'Unnamed: 58': 'Accurate forward passes',
                          'Back passes / accurate': 'Back passes',

                          'Unnamed: 60': 'Accurate back passes',
                          'Saves / with reflexes': 'Saves',
                          'Unnamed: 65': 'Saves with reflexes',
                          'Exits / accurate': 'Exits',
                          'Passes to goalkeeper / accurate': 'Passes to goalkeeper',
                          'Unnamed: 68': 'Accurate passes to goalkeeper'}, inplace=True)
    return stats


def per90(stats):
    """
    Input:  Data frame of all statistics of a player, downloaded via Wyscout,
            Create via CreateDF
    Output: the statistics per 90 minutes
    """
    # Copy the first descriptive columns from input
    statistics_per90 = stats[['Home', 'Away', 'Home_Score', 'Away_Score', 'Match', 'Competition', 'Date', 'Position',
                              'Minutes played']].copy()

    # Calculate all remaining statistics in per 90 metrics
    for col in list(stats.columns[9:]):
        statistics_per90[col] = stats[col] / stats['Minutes played'] * 90

    # Add some statistics describing percentages and ratios of other stats
    statistics_per90['Action success%'] = statistics_per90['Successful actions'] / statistics_per90[
        'Total actions'] * 100
    statistics_per90['Pass success%'] = statistics_per90['Accurate passes'] / statistics_per90['Passes'] * 100
    statistics_per90['Long pass success%'] = statistics_per90['Accurate long passes'] / statistics_per90[
        'Long passes'] * 100
    statistics_per90['Cross success%'] = statistics_per90['Accurate crosses'] / statistics_per90['Crosses'] * 100
    statistics_per90['Long pass%'] = statistics_per90['Long passes'] / statistics_per90['Passes'] * 100
    statistics_per90['Dribble success%'] = statistics_per90['Successful dribbles'] / statistics_per90['Dribbles'] * 100
    statistics_per90['Duel win%'] = statistics_per90['Duels won'] / statistics_per90['Duels'] * 100
    statistics_per90['Aerial duel win%'] = statistics_per90['Aerial duels won'] / statistics_per90['Aerial duels'] * 100
    statistics_per90['Defensive duel win%'] = statistics_per90['Defensive duels won'] / statistics_per90[
        'Defensive duels'] * 100

    statistics_per90['Offensive duel win%'] = statistics_per90['Offensive duels won'] / statistics_per90[
        'Offensive duels'] * 100
    statistics_per90['Passes to final third success%'] = statistics_per90['Accurate passes to final third'] / \
                                                         statistics_per90['Passes to final third'] * 100
    statistics_per90['Passes to final third%'] = statistics_per90['Passes to final third'] / statistics_per90[
        'Passes'] * 100
    statistics_per90['Passes to box success%'] = statistics_per90['Accurate passes to penalty area'] / statistics_per90[
        'Passes to penalty area'] * 100
    statistics_per90['Passes to box%'] = statistics_per90['Passes to penalty area'] / statistics_per90['Passes'] * 100
    statistics_per90['Forward passes success%'] = statistics_per90['Accurate forward passes'] / statistics_per90[
        'Forward passes'] * 100
    statistics_per90['Forward pass%'] = statistics_per90['Forward passes'] / statistics_per90['Passes'] * 100
    statistics_per90['Back passes success%'] = statistics_per90['Accurate back passes'] / statistics_per90[
        'Back passes'] * 100
    statistics_per90['Back pass%'] = statistics_per90['Back passes'] / statistics_per90['Passes'] * 100
    statistics_per90['Recoveries Losses ratio'] = statistics_per90['Recoveries'] / statistics_per90['Losses']
    statistics_per90['Forward Backward Pass ratio'] = statistics_per90['Forward passes'] / statistics_per90[
        'Back passes']

    # Goalkeepers only
    if 'xCG' in statistics_per90.columns:
        statistics_per90['Save percentage'] = statistics_per90['Saves'] / statistics_per90['Shots against'] * 100

    # NaNs are replaced by zeros to be able to graph data
    statistics_per90 = statistics_per90.fillna(0)

    return statistics_per90


def nearest_ind(items, pivot):
    """
    Finds the date in a column that is closest to given date (pivot)
    """
    time_diff = np.abs([date - pivot for date in items])
    return time_diff.argmin(0)


# def run(player1, player2,  dates):
# Create a form for year of signing and time frame of the analysis
dates = controller.ScoutForm.create_form("Date of signing")
##########################
player1 = controller.FileHandler.select_file("Player 1", [("Excel files", ".xlsx .xls")])  # Scouting's excel
player2 = controller.FileHandler.select_file("Player 2", [("Excel files", ".xlsx .xls")])

# This will be True when user presses 'cancel'
if not isinstance(player1, str):
    sys.exit()

# Check if the player already has a folder
path = os.getcwd()

# Create Data frame of all stats
Stats_player1 = createDF(player1)
Stats_player1 = Stats_player1[Stats_player1['Minutes played'] >= 20]
Stats_player1 = Stats_player1[::-1].reset_index()

# Create Data frame of all stats
Stats_player2 = createDF(player2)
Stats_player2 = Stats_player2[Stats_player2['Minutes played'] >= 20]
Stats_player2 = Stats_player2[::-1].reset_index()

# Calculate all stats in per 90 metrics
stats_per90_player1 = per90(Stats_player1)
stats_per90_player2 = per90(Stats_player2)

#  The date of signing with Tactalyse (player 1)
year = int(dates.year)
month = int(dates.month)
day = int(dates.day)

#  2 year frame period for the graphs
year_frame = int(dates.year_frame)

# get current date
current_date = datetime.date.today()

# Find the dates that match closest to start date and start season date
start_index = nearest_ind(stats_per90_player1['Date'], datetime.date(year, month, day))

# Labels showing the start / end of football seasons
# takes current date as a reference for plotting and depending on the choice given in the form counts back
# either 3 or 4 football seasons and generates the graphs for that time frame
if year_frame == 3:
    season_index_player1 = nearest_ind(stats_per90_player1['Date'], datetime.date(current_date.year - 3, 12, 31))
    season_index1_player1 = nearest_ind(stats_per90_player1['Date'], datetime.date(current_date.year - 2, 12, 31))
    season_index2_player1 = nearest_ind(stats_per90_player1['Date'], datetime.date(current_date.year - 1, 12, 31))
    season_index3_player1 = nearest_ind(stats_per90_player1['Date'],
                                        datetime.date(current_date.year, current_date.month, current_date.day))
    season_index4_player1 = 0

    season_index_player2 = nearest_ind(stats_per90_player2['Date'], datetime.date(current_date.year - 3, 12, 31))
    season_index3_player2 = nearest_ind(stats_per90_player2['Date'],
                                        datetime.date(current_date.year, current_date.month, current_date.day))
    season_index4_player2 = 0

    season_ticks3 = [str(current_date.year - 2), str(current_date.year - 1), str(current_date.year)]
    season_ticks4 = []

elif year_frame == 4:
    season_index_player1 = nearest_ind(stats_per90_player1['Date'], datetime.date(current_date.year - 4, 12, 31))
    season_index1_player1 = nearest_ind(stats_per90_player1['Date'], datetime.date(current_date.year - 3, 12, 31))
    season_index2_player1 = nearest_ind(stats_per90_player1['Date'], datetime.date(current_date.year - 2, 12, 31))
    season_index3_player1 = nearest_ind(stats_per90_player1['Date'], datetime.date(current_date.year - 1, 12, 31))
    season_index4_player1 = nearest_ind(stats_per90_player1['Date'],
                                        datetime.date(current_date.year, current_date.month, current_date.day))

    season_index_player2 = nearest_ind(stats_per90_player2['Date'], datetime.date(current_date.year - 4, 12, 31))
    season_index1_player2 = nearest_ind(stats_per90_player2['Date'], datetime.date(current_date.year - 3, 12, 31))
    season_index2_player2 = nearest_ind(stats_per90_player2['Date'], datetime.date(current_date.year - 2, 12, 31))
    season_index3_player2 = nearest_ind(stats_per90_player2['Date'], datetime.date(current_date.year - 1, 12, 31))
    season_index4_player2 = nearest_ind(stats_per90_player2['Date'],
                                        datetime.date(current_date.year, current_date.month, current_date.day))

    season_ticks4 = [str(current_date.year - 3), str(current_date.year - 2), str(current_date.year - 1),
                     str(current_date.year)]
    season_ticks3 = []

# Edge case which will generate a 4 year graph in case unexpected error has occurred
# somewhere during the form filling or input. We made sure this is never executed by adding a number of checks
# prior to this point, and limited the choice option of the user
else:
    season_index_player1 = nearest_ind(stats_per90_player1['Date'],
                                       datetime.date(current_date.year - 4, current_date.month, current_date.day))
    season_index1_player1 = nearest_ind(stats_per90_player1['Date'],
                                        datetime.date(current_date.year - 3, current_date.month, current_date.day))
    season_index2_player1 = nearest_ind(stats_per90_player1['Date'],
                                        datetime.date(current_date.year - 2, current_date.month, current_date.day))
    season_index3_player1 = nearest_ind(stats_per90_player1['Date'],
                                        datetime.date(current_date.year - 1, current_date.month, current_date.day))
    season_index4_player1 = nearest_ind(stats_per90_player1['Date'],
                                        datetime.date(current_date.year, current_date.month, current_date.day))

    season_index_player2 = nearest_ind(stats_per90_player2['Date'],
                                       datetime.date(current_date.year - 4, current_date.month, current_date.day))
    season_index3_player2 = nearest_ind(stats_per90_player2['Date'],
                                        datetime.date(current_date.year - 1, current_date.month, current_date.day))
    season_index4_player2 = nearest_ind(stats_per90_player2['Date'],
                                        datetime.date(current_date.year, current_date.month, current_date.day))

    season_ticks4 = [str(current_date.year - 3), str(current_date.year - 2), str(current_date.year - 1),
                     str(current_date.year)]
    season_ticks3 = []

window = 8

# trim the data frame based on the time period of analysis chosen
# If 3 years were selected, all games that re not in the 3 year period will be removed
if year_frame == 3:
    if season_index1_player1 > 0:
        stats_per90_player1 = stats_per90_player1[season_index_player1 - 4: season_index3_player1 + 4]
        stats_per90_player2 = stats_per90_player2[season_index_player2 - 4: season_index3_player2 + 4]


# If 4 years were selected, all games that re not in the 3 year period will be removed
elif year_frame == 4:
    if season_index1_player1 > 0:
        stats_per90_player1 = stats_per90_player1[season_index_player1 - 4: season_index4_player1 + 4]
        stats_per90_player2 = stats_per90_player2[season_index_player2 - 4: season_index4_player2 + 4]

plot_name = ''

# Plot the stats, together with the dates
# Plotting is done through the columns in the data frame, using the names as references for plots
for column in list(stats_per90_player1.columns[9:]):
    if 'accurate' in column.lower() or 'won' in column.lower() or 'own half' in column.lower() or 'opp half' in column.lower() or 'on target' in column.lower() or 'successful' in column.lower():
        continue
    fig, ax = plt.subplots()

    ax.axvline(x=start_index, color='#E23D46', linewidth=2, label='Start Tactalyse')

    # Grey line will be used to label the end of the year (football season on the graphs)
    if year_frame == 3:
        ax.axvline(x=season_index_player1, color='gray', linestyle='--')  # marks end of current_year - 3
        ax.axvline(x=season_index1_player1, color='gray', linestyle='--')  # marks end of current_year - 2
        ax.axvline(x=season_index2_player1, color='gray', linestyle='--')  # marks end of current_year - 1

    if year_frame == 4:
        ax.axvline(x=season_index_player1, color='gray', linestyle='--')  # marks end of current_year - 4
        ax.axvline(x=season_index1_player1, color='gray', linestyle='--')  # marks end of current_year - 3
        ax.axvline(x=season_index2_player1, color='gray', linestyle='--')  # marks end of current_year - 2
        ax.axvline(x=season_index3_player1, color='gray', linestyle='--')  # marks end of current_year - 1

    if column[-1] == '%':
        plt.title(plot_name + '\n' + column)
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(), marker='.', color='black',
                label='_Total')
        ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
                label='_Total')

    elif 'passes' in column.lower() and 'accurate' not in column.lower() and 'received' not in column.lower() and 'percentage' not in column.lower():
        plt.title(plot_name + '\n' + column + ' per 90 minutes')

        # player 1 plot
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(), marker='.', color='black',
                label='Total')
        ax.plot(stats_per90_player1['Accurate ' + column.lower()].rolling(window, center=True).mean(),
                marker='.', color='gray', label='Accurate')
        # player 2 plot
        ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
                label='Total')
        ax.plot(stats_per90_player2['Accurate ' + column.lower()].rolling(window, center=True).mean(),
                marker='.', color='cyan', label='Accurate')

    elif 'percentage of passes' in column.lower():
        plt.title(plot_name + '\n' + column)
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(), marker='.', color='black',
                label='_Total')

        ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
                label='_Total')

    elif column == 'Crosses':
        plt.title(plot_name + '\n' + column + ' per 90 minutes')

        # Player 1
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(), marker='.', color='black',
                label='Total')
        ax.plot(stats_per90_player1['Accurate ' + column.lower()].rolling(window, center=True).mean(),
                marker='.', color='gray', label='Accurate')

        # Player 2
        ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
                label='Total')
        ax.plot(stats_per90_player2['Accurate ' + column.lower()].rolling(window, center=True).mean(),
                marker='.', color='cyan', label='Accurate')

    elif column == 'Offensive duels' or column == 'Defensive duels' or column == 'Aerial duels' or column == 'Duels':
        plt.title(plot_name + '\n' + column + ' per 90 minutes')

        # Player 1
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(), marker='.', color='black',
                label='Total')
        ax.plot(stats_per90_player1[column + ' won'].rolling(window, center=True).mean(), marker='.',
                color='gray', label='Won')

        # Player 2
        ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
                label='Total')
        ax.plot(stats_per90_player2[column + ' won'].rolling(window, center=True).mean(), marker='.',
                color='cyan', label='Won')

    elif column == 'Losses':
        plt.title(plot_name + '\n' + column + ' per 90 minutes')

        # Player 1
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(), marker='.', color='black',
                label='Total')
        ax.plot(stats_per90_player1[column + ' own half'].rolling(window, center=True).mean(), marker='.',
                color='gray', label='Own half')

        # Player 2
        ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
                label='Total')
        ax.plot(stats_per90_player2[column + ' own half'].rolling(window, center=True).mean(), marker='.',
                color='cyan', label='Own half')

    elif column == 'Recoveries':
        plt.title(plot_name + '\n' + column + ' per 90 minutes')

        # Player 1
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(), marker='.', color='black',
                label='Total')
        ax.plot(stats_per90_player1[column + ' opp half'].rolling(window, center=True).mean(), marker='.',
                color='gray', label='Opp half')

        # Player 2
        ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
                label='Total')
        ax.plot(stats_per90_player2[column + ' opp half'].rolling(window, center=True).mean(), marker='.',
                color='cyan', label='Opp half')

    elif column == 'Shots':
        plt.title(plot_name + '\n' + column + ' per 90 minutes')
        # Player 1
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(), marker='.', color='black',
                label='Total')
        ax.plot(stats_per90_player1[column + ' on target'].rolling(window, center=True).mean(), marker='.',
                color='gray', label='On target')

        # Player 2
        ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
                label='Total')
        ax.plot(stats_per90_player2[column + ' on target'].rolling(window, center=True).mean(), marker='.',
                color='cyan', label='On target')

    elif column == 'Sliding tackles' or column == 'Dribbles':
        plt.title(plot_name + '\n' + column + ' per 90 minutes')

        # Player 1
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(), marker='.', color='black',
                label='Total')
        ax.plot(stats_per90_player1['Successful ' + column.lower()].rolling(window, center=True).mean(),
                marker='.', color='gray', label='Successful')

        # Player 2
        ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
                label='Total')
        ax.plot(stats_per90_player2['Successful ' + column.lower()].rolling(window, center=True).mean(),
                marker='.', color='cyan', label='Successful')

    elif column == 'Total actions':
        plt.title(plot_name + '\n' + column + ' per 90 minutes')

        # Player 1
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(), marker='.', color='black',
                label='Total')
        ax.plot(
            stats_per90_player1['Successful ' + column.split(' ')[1]].rolling(window, center=True).mean(), marker='.',
            color='gray', label='Won')

        # Player 2
        ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
                label='Total')
        ax.plot(stats_per90_player2['Successful ' + column.split(' ')[1]].rolling(window, center=True).mean(),
                marker='.', color='cyan', label='Won')

    else:
        plt.title(plot_name + '\n' + column + ' per 90 minutes')
        ax.plot(stats_per90_player1[column].rolling(window, center=True).mean(),
                stats_per90_player2[column].rolling(window, center=True).mean(),
                marker='.', color='black',
                label='_Total')

        # ax.plot(stats_per90_player2[column].rolling(window, center=True).mean(), marker='.', color='blue',
        #         label='_Total')

    plt.legend(frameon=False)

    # Plot the indexes representing the years of the analysis
    # E.g. the x axis of the graph represents years, when 3 year frame is selected the labels will be
    # 2019, 2020, 2021
    if year_frame == 3:
        plt.xticks([season_index_player1, season_index1_player1, season_index2_player1], season_ticks3)

    if year_frame == 4:
        plt.xticks([season_index_player1, season_index1_player1, season_index2_player1, season_index3_player1],
                   season_ticks4)

    plt.tick_params(bottom=True)

    # Path to save the graphs.
    # Note since the application will be used on Mac OS only the path problems may arise on windows
    if path[0] == '/':
        fig_name = path + '/Stats Progression/' + column + '_' + str(window) + '.png'
        print(fig_name)
        print(path)
    else:
        fig_name = path + '\\Stats Progression\\' + column + ' ' + str(window) + '.png'

    plt.savefig(fig_name, dpi=250, bbox_inches='tight')
    plt.close()
    break

print("        Processing finalized         ")

# if __name__ == "__main__":
#     # Create a form for year of signing and time frame of the analysis
#     scout_form = controller.ScoutForm.create_form("Date of signing")
#     ##########################
#     player1 = controller.FileHandler.select_file("Player 1", [("Excel files", ".xlsx .xls")])  # Scouting's excel
#     player2 = controller.FileHandler.select_file("Player 2", [("Excel files", ".xlsx .xls")])
#     run(player1, player2, scout_form)
