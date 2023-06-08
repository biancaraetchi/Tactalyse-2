from app.data.excel_reader import ExcelReader


class Preprocessor:

    def extract_player(self, league_df, player_name):
        """
        Function that extracts a single row from a football league dataframe only containing a desired player's data.

        :param league_df: Dataframe containing league data of football players.
        :param player_name: Name of the player whose data to extract.
        :return: A DataFrame containing a single row with the data of the specified player.
        """

        row_df = league_df[league_df['Player'] == player_name]
        return row_df

    def position_dictionary(self):
        """
        Creates a collection of all position codes, with their associated general position in full words.
        Work in progress.

        :return: Dictionary containing all position abbreviations as keys, and the associated general positions as values.
        """

        pos_dict = dict.fromkeys(['RW', 'RWF', 'LWF', 'LW'], 'Winger')
        pos_dict.update(dict.fromkeys(['GK'], 'Goalkeeper'))
        pos_dict.update(dict.fromkeys(['LB', 'LB5', 'LWB', 'RB', 'RB5', 'RWB'], 'Full Back'))
        pos_dict.update(dict.fromkeys(['RCB', 'RCB3', 'CB', 'LCB', 'LCB3'], 'Center Back'))
        pos_dict.update(
            dict.fromkeys(['DMF', 'LCMF', 'RCMF', 'LDMF', 'RDMF', 'LCMF3', 'RCMF3'], 'Defensive Midfielder'))
        pos_dict.update(dict.fromkeys(['AMF', 'LAMF', 'RAMF'], 'Attacking Midfielder'))
        pos_dict.update(dict.fromkeys(['CF', 'LCF', 'RCF'], 'Striker'))

        return pos_dict

    def shortened_dictionary(self):
        """
        Creates a collection of all position codes, with their associated general position as abbreviations.
        Work in progress.

        :return: Dictionary containing all position abbreviations as keys, and the associated general position abbreviations
                 as values.
        """
        pos_dict = dict.fromkeys(['RW', 'RWF', 'LWF', 'LW'], 'WI')
        pos_dict.update(dict.fromkeys(['GK'], 'GK'))
        pos_dict.update(dict.fromkeys(['LB', 'LB5', 'LWB', 'RB', 'RB5', 'RWB'], 'FB'))
        pos_dict.update(dict.fromkeys(['RCB', 'RCB3', 'CB', 'LCB', 'LCB3'], 'CB'))
        pos_dict.update(dict.fromkeys(['DMF', 'LCMF', 'RCMF', 'LDMF', 'RDMF', 'LCMF3', 'RCMF3'], 'DM'))
        pos_dict.update(dict.fromkeys(['AMF', 'LAMF', 'RAMF'], 'AM'))
        pos_dict.update(dict.fromkeys(['CF', 'LCF', 'RCF'], 'ST'))

        return pos_dict

    def league_category_dictionary(self):
        """
        Creates a collection of all positions, along with the league stats that should be graphed in the radio chart for
        each position.
        Work in progress.

        :return: Dictionary containing all positions as keys, and the associated stats as values.
        """
        shots_blocked = 'Shots blocked per 90'
        off_duels = 'Offensive duels per 90'
        def_duels = 'Defensive duels per 90'
        interceptions = 'Interceptions per 90'
        sliding_tackles = 'Sliding tackles per 90'
        long_passes = 'Long passes per 90'
        dribbles = 'Dribbles per 90'
        goals = 'Goals per 90'
        crosses = 'Crosses per 90'
        fouls = 'Fouls per 90'
        prog_runs = 'Progressive runs per 90'
        assists = 'Assists per 90'

        atk_list = [prog_runs, assists, goals, dribbles, off_duels, fouls]
        def_list = [goals, crosses, dribbles, interceptions, def_duels, fouls]

        cat_dict = dict.fromkeys(['GK'], [shots_blocked, def_duels,
                                          interceptions, sliding_tackles,
                                          long_passes, dribbles])
        cat_dict.update(dict.fromkeys(['FB'], def_list))
        cat_dict.update(dict.fromkeys(['CB'], def_list))
        cat_dict.update(dict.fromkeys(['DM'], def_list))
        cat_dict.update(dict.fromkeys(['AM'], atk_list))
        cat_dict.update(dict.fromkeys(['WI'], atk_list))
        cat_dict.update(dict.fromkeys(['ST'], atk_list))
        return cat_dict

    def main_position(self, player_row):
        """
        Function that retrieves the main position of a football player.

        :param player_row: Dataframe containing the league data of a single player.
        :return: The first position in the list of player positions.
        """
        player_positions = player_row['Position'].iloc[0]
        first_position = player_positions.split(', ')[0]
        return first_position

    def in_league(self, league_file, player_name):
        """
        Function that checks if the player is included in the league file

        :param league_file: Excel file containing football league data.
        :param player_name: Name of the player whose data to extract.
        :return: True if they're in the league file, false if not
        """

        league_df = ExcelReader().all_league_data(league_file)
        if player_name in league_df['Player'].values:
            return True
        else:
            return False
