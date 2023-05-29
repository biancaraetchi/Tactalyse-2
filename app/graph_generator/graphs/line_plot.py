import io

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from .abstract_models import Graph


class LinePlot(Graph):
    """
    Class that represents a line plot for standard/compare data reports with league and personal data
    """
    __position = ''
    __tactalyse = "#EC4A24"
    __black = "#242424"
    __season_color = "#00a70b"
    __player_color = '#f45600'
    __player_sub_color = '#f0a780'
    __compare_color = '#4a24ec'
    __compare_sub_color = '#bbafec'
    __title = "#D46508"
    __subtitle = "#5E5E5E"
    __fig_w = 8
    __fig_h = 7.75
    __bottom_offset = 0.1
    __top_offset = 0.85
    __right_offset = 0.9
    __left_offset = 0.1
    __subtitle_offset = 0.92
    __title_offset = 1.11

    def __init__(self, param_map):
        player_pos = param_map.get('player_pos')
        if player_pos:
            self.__position = player_pos


    def dates_to_int(self, dates):
        """
        Function to change dates(in YYYY-MM-DD format) into int value
        :param dates: data["Date"] in the personal data
        """
        return (dates - dates.min()).dt.days

    def scaled_date_values(self, dates):
        """
        Function to calculate scaled x-values for the plots
        :param dates: data["Date"] in the personal data
        """
        # Calculate time differences in days
        time_diff = dates.diff().dt.days
        time_diff = time_diff.fillna(0)

        # Calculate scaled x-values based on time differences
        scaled_date_values = np.cumsum(time_diff)  # Cumulative sum of time differences
        return scaled_date_values


    def get_xlabels(self, data):
        dates = pd.to_datetime(data["Date"], format='%Y-%m-%d')
        dates = dates.sort_values().reset_index(drop=True)
        scaled_x_values = self.scaled_date_values(dates)

        year = dates.dt.year
        month = dates.dt.month

        year_indices = []
        for y in year.unique():
            year_dates = dates[year == y]
            first_of_july = year_dates[(month >= 7) & (year_dates.dt.day > 1)].index.min()
            if pd.notnull(first_of_july):
                year_indices.append(first_of_july)
        year_x_values = []
        for i in year_indices:
            year_x_values.append(scaled_x_values[i])
        date_strings = dates.iloc[year_indices].dt.strftime('%Y-%m-%d')
        years = date_strings.str.slice(start=2, stop=4)
        seasons = [f"{n}/{int(n)+1}" for n in years]

        return scaled_x_values, year_x_values, seasons

    def average_entries(self, x_vals, y_vals, window=5):
        """
        Function to get mean values of the x and y valuesf according to the target plots
        :param x_vals: target data which will be placed in x axis in the plot
        :param y_vals: target data which will be placed in y axis in the plot
        :param window = 5: rolling function will be performed with 5 data
        """
        avg_x = x_vals.rolling(window=window).mean()
        avg_y = y_vals.rolling(window=window).mean()
        return avg_x, avg_y

    def create_plot(self, ax, dates_x_values, data, color, label, order):
        """
        Function creates line plots based on the data
        :param ax: current Axes object 
        :param dates_x_values: calculated x values based on dates
        :param data: player data for the plots
        :param color: the color of the line
        """
        sns.lineplot(x=dates_x_values, y=data, ax=ax, color=color, label=label, zorder=order, linewidth=1)

    def create_sub_plot_data(self, subcolumns, player_data, column_index):
        """
        Function creates sub line plots data based on the player data
        :param subcolumns: indicate columns for the sub plot
        :param player_data: data file which the sub plot will be based on
        :param column_index: give index for the columns
        """
        player_sub_data, second_column = None, None
        if len(subcolumns) > 1:
            second_column = subcolumns[1].strip()
            player_sub_data = player_data[player_data.columns[column_index+1]][::-1].reset_index(drop=True)
        return player_sub_data, second_column

    def plot_player(self, ax, player_x_values, player_stat_data, player, stat, color, player_sub_data=None,
                    sub_stat=None, sub_color=None):
        """
        Function creates players' line plots based on the player data
        :param ax: current Axes object
        :param player_x_values: indicate player's stat data's x values
        :param player: name of the target player
        :param stat: stat's of the target player
        :param color: color of the line plots
        """
        x_vals, y_vals = self.average_entries(player_x_values, player_stat_data)
        label = stat + " for " + player
        self.create_plot(ax, x_vals, y_vals, color, label, order=1)
        if player_sub_data is not None:
            x_vals, y_vals = self.average_entries(player_x_values, player_sub_data)
            label = sub_stat.capitalize() + " for " + player
            self.create_plot(ax, x_vals, y_vals, sub_color, label, order=1)

    def draw_years(self, ax, year_x_values, years):
        """
        Function draw years line in the plots
        :param ax: current Axes object
        :param year_x_values: indicate year's x values for drawing plot
        :param years: years in the data
        """
        plt.xlabel("Season", fontsize=14)
        ax.set(xticks=year_x_values, xticklabels=years)
        no_label = False
        for year in year_x_values:
            if no_label:
                ax.axvline(x=year, linestyle="dashed", color=self.__season_color)
            else:
                ax.axvline(x=year, linestyle="dashed", color=self.__season_color, label="Season")
                no_label = True
        return ax

    def draw_tactalyse_dates(self, ax, data, start_date, end_date):
        """
        Function draw Tactalyse start and end date line in the plots
        :param ax: current Axes object
        :param start_date: indicate start date of the employee
        :param end_date: indicate end date of the employee
        """
        dates = pd.to_datetime(data["Date"], format='%Y-%m-%d')
        dates = dates.sort_values().reset_index(drop=True)
        start = pd.Timestamp(start_date)
        end = pd.Timestamp(end_date)

        scaled_x_values = self.scaled_date_values(dates)
        start_idx = dates.searchsorted(start, side='left') - 1
        start_x = scaled_x_values[start_idx]
        end_idx = dates.searchsorted(end, side='left') - 1
        end_x = scaled_x_values[end_idx]

        if 0 <= start_idx <= len(dates):
            ax.axvline(x=start_x, linestyle="-", label="Tactalyse contract", color=self.__black)
            if start_idx < end_idx <= len(dates):
                ax.axvline(x=end_x, linestyle="-", color=self.__black)
        return ax

    def set_layout(self, ax, p2, stat):
        """
        Function set layout of the plots
        :param ax: current Axes object
        :param p1: indicate player 1
        :param p2: indicate player 2
        :param stat: indicate stats of the player
        """
        plt.ylabel(stat, fontsize=14)
        title = "Stat: " + stat
        subtitle = ""
        if p2 is not None:
            subtitle += "Compared with " + p2 + "\n"
        plt.suptitle(subtitle, fontsize=15, y=self.__subtitle_offset, color=self.__subtitle)
        ax.set_title(title, fontsize=18, fontweight=0, color=self.__title, weight="bold", y=self.__title_offset)

        return ax

    def draw(self, param_map):
        """
        Function draw the plot
        :param param_map: include all parameters for drawing line plots. This includes 
        "player_data, column_name, start_date, end_date, player, compare, compare_data"
        """
        player_data = param_map.get('player_data')
        column_name = param_map.get('columns')
        start_date = param_map.get('start_date')
        end_date = param_map.get('end_date')
        player = param_map.get('player')
        compare = param_map.get('compare')
        compare_data = param_map.get('compare_data')

        fig, ax = plt.subplots(figsize=(self.__fig_w, self.__fig_h), gridspec_kw={'top': self.__top_offset,
                                                                                  'bottom': self.__bottom_offset,
                                                                                  'left': self.__left_offset,
                                                                                  'right': self.__right_offset})
        ax.clear()

        player_x_values, year_x_values, years = self.get_xlabels(player_data)
        subcolumns = column_name.split("/")
        column_index = player_data.columns.get_loc(column_name)
        player_stat_data = player_data[player_data.columns[column_index]][::-1].reset_index(drop=True)

        player_sub_data, second_column = self.create_sub_plot_data(subcolumns, player_data, column_index)

        self.plot_player(ax, player_x_values, player_stat_data, player, subcolumns[0],
                         self.__player_color, player_sub_data, second_column, self.__player_sub_color)

        if compare and isinstance(compare_data, pd.DataFrame):
            compare_x_values, _, _ = self.get_xlabels(compare_data)
            compare_stat_data = compare_data[column_name][::-1].reset_index(drop=True)

            compare_sub_data, second_column = self.create_sub_plot_data(subcolumns, compare_data, column_index)

            self.plot_player(ax, compare_x_values, compare_stat_data, compare, subcolumns[0],
                             self.__compare_color, compare_sub_data, second_column, self.__compare_sub_color)

        mean = np.mean(player_stat_data)
        label = "Mean for " + player
        ax.axhline(y=mean, color='black', linestyle="dashed", label=label)

        ax = self.draw_years(ax, year_x_values, years)

        if start_date:
            ax = self.draw_tactalyse_dates(ax, player_data, start_date, end_date)

        ax = self.set_layout(ax, compare, column_name)

        plt.legend(bbox_to_anchor=(0.5, 1), loc='upper center', fontsize="medium")

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()
        return buffer.getvalue()

    def draw_all(self, param_map):
        """
        Function draw the all plots
        :param param_map: include all parameters for drawing line plots. This includes 
        "player_data, column_name, start_date, end_date, player, compare, compare_data"
        """
        columns = param_map.get('columns')
        plots = []
        for column in columns:
            param_map['columns'] = column
            plots.append(self.draw(param_map))
        if len(plots) == 1:
            return plots[0]
        return plots
