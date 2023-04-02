class Player:
    __player_name = "Name"
    __player_position = "Position"
    __player_height = "Height"
    __player_agent = "Agent"
    __player_age = "Age"
    __player_country = "Country"
    __player_club = "Club"
    __player_league = "League"
    __player_weight = "Weight"
    __player_foot = "Foot"
    __player_on_loan = "OnLoan"
    __player_contract_date = "ContractDate"
    __player_num_matches = "NumMatches"

    def set_personal_info(self, player_name, league_df):
        self.__player_name = player_name
        self.__player_height = str(league_df.loc[league_df['Player'] == player_name, 'Height'].values[0])
        self.__player_age = str(league_df.loc[league_df['Player'] == player_name, 'Age'].values[0])
        self.__player_country = league_df.loc[league_df['Player'] == player_name, 'Birth country'].values[0]
        self.__player_weight = str(league_df.loc[league_df['Player'] == player_name, 'Weight'].values[0])

    def set_football_info(self, player_name, league_df, position):
        self.__player_position = position
        self.__player_club = league_df.loc[league_df['Player'] == player_name, 'Team'].values[0]

        # Placeholder, might be extracted from the league excel file name
        self.__player_league = "ENG2"

        self.__player_foot = league_df.loc[league_df['Player'] == player_name, 'Foot'].values[0]
        self.__player_on_loan = league_df.loc[league_df['Player'] == player_name, 'On loan'].values[0]
        self.__player_contract_date = league_df.loc[league_df['Player'] == player_name, 'Contract expires'].values[0]
        self.__player_num_matches = str(league_df.loc[league_df['Player'] == player_name, 'Matches played'].values[0])

    def get_player_name(self):
        return self.__player_name

    def get_player_position(self):
        return self.__player_position

    def get_player_height(self):
        return self.__player_height

    def get_player_agent(self):
        return self.__player_agent

    def get_player_age(self):
        return self.__player_age

    def get_player_country(self):
        return self.__player_country

    def get_player_club(self):
        return self.__player_club

    def get_player_league(self):
        return self.__player_league

    def get_player_weight(self):
        return self.__player_weight

    def get_player_foot(self):
        return self.__player_foot

    def get_player_on_loan(self):
        return self.__player_on_loan

    def get_player_contract_date(self):
        return self.__player_contract_date

    def get_player_num_matches(self):
        return self.__player_num_matches
