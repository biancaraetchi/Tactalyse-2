# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/tactalyze"
DATABASE_CONNECT_OPTIONS = {}


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

DIRECTORY_FOR_FILE_SAVE_WINDOWS = "\\app\\model\\"
DIRECTORY_FOR_FILE_SAVE_UNIX = "/app/model/"

POSITIONAL_POINT_WINDOWS = {
    "Attacking Midfielder":['Total actions 8.png','Goals 8.png',
                                     'Assists 8.png','Shots 8.png','xG 8.png',
                                     'Passes 8.png','Crosses 8.png',
                                     'Crosses 8.png', 'Dribbles 8.png', 'Duels 8.png',
                                     'Aerial duels 8.png', 'Interceptions 8.png',
                                     'Losses 8.png', 'Recoveries 8.png',
                                     'Defensive duels 8.png',
                                     'Loose ball duels 8.png', 'Sliding tackles 8.png', 'Clearances 8.png',
                                     'Fouls 8.png',
                                     'Yellow cards 8.png', 'Red cards 8.png',
                                     'Shot assists 8.png', 'Offensive duels 8.png', 'Touches in penalty area 8.png',
                                     'Progressive runs 8.png','Fouls suffered 8.png','Through passes 8.png',
                                     'xA 8.png','Second assists 8.png','Passes to final third 8.png',
                                     'Passes to penalty area 8.png','Received passes 8.png','Forward passes 8.png',
                                     'Back passes 8.png'
                                     ],
    "Center Back":['Total actions 8.png','Passes 8.png','Long passes 8.png',
                   'Dribbles 8.png','Duels 8.png',
                 'Aerial duels 8.png','Interceptions 8.png',
                 'Losses 8.png','Recoveries 8.png',
                   'Defensive duels 8.png',
                   'Loose ball duels 8.png', 'Sliding tackles 8.png', 'Clearances 8.png', 'Fouls 8.png',
                   'Yellow cards 8.png', 'Red cards 8.png',
                   'Shot assists 8.png', 'Offensive duels 8.png'
                   ,'Fouls suffered 8.png','Through passes 8.png',
                   'Passes to final third 8.png',
                   'Passes to penalty area 8.png', 'Received passes 8.png', 'Forward passes 8.png',
                   'Back passes 8.png','Exits 8.png','Passes to goalkeeper 8.png'
                   ],
    "Full Back":['Total actions 8.png','Passes 8.png','Long passes 8.png',
                 'Crosses 8.png','Dribbles 8.png','Duels 8.png',
                 'Aerial duels 8.png','Interceptions 8.png',
                 'Losses 8.png','Recoveries 8.png',
                 'Defensive duels 8.png',
                 'Loose ball duels 8.png', 'Sliding tackles 8.png', 'Clearances 8.png', 'Fouls 8.png',
                 'Yellow cards 8.png', 'Red cards 8.png',
                 'Shot assists 8.png','Offensive duels 8.png','Touches in penalty area 8.png',
                 'Progressive runs 8.png','Fouls suffered 8.png','Through passes 8.png',
                 'xA 8.png','Second assists 8.png','Passes to final third 8.png',
                 'Passes to penalty area 8.png','Received passes 8.png','Forward passes 8.png',
                 'Back passes 8.png','Exits 8.png','Passes to goalkeeper 8.png',
                 ],
    "Defensive Midfielder":['Total actions 8.png','Passes 8.png','Long passes 8.png',
                  'Dribbles 8.png', 'Duels 8.png',
                  'Aerial duels 8.png', 'Interceptions 8.png',
                  'Losses 8.png', 'Recoveries 8.png','Defensive duels 8.png',
                   'Loose ball duels 8.png', 'Sliding tackles 8.png', 'Clearances 8.png', 'Fouls 8.png',
                   'Yellow cards 8.png', 'Red cards 8.png',
                   'Shot assists 8.png', 'Offensive duels 8.png',
                    'Fouls suffered 8.png','Through passes 8.png','Passes to final third 8.png',
                   'Passes to penalty area 8.png', 'Received passes 8.png', 'Forward passes 8.png',
                   'Back passes 8.png','Exits 8.png','Passes to goalkeeper 8.png'
                  ],
    "Winger":['Total actions 8.png','Goals 8.png',
             'Assists 8.png','Shots 8.png','xG 8.png',
             'Passes 8.png','Crosses 8.png',
             'Crosses 8.png', 'Dribbles 8.png', 'Duels 8.png',
             'Aerial duels 8.png', 'Interceptions 8.png',
             'Losses 8.png', 'Recoveries 8.png',
             'Defensive duels 8.png',
             'Loose ball duels 8.png', 'Sliding tackles 8.png', 'Clearances 8.png',
             'Fouls 8.png',
             'Yellow cards 8.png', 'Red cards 8.png',
             'Shot assists 8.png', 'Offensive duels 8.png', 'Touches in penalty area 8.png',
             'Progressive runs 8.png','Fouls suffered 8.png','Through passes 8.png',
             'xA 8.png','Second assists 8.png','Passes to final third 8.png',
             'Passes to penalty area 8.png','Received passes 8.png'
             ],
    "Striker":['Total actions 8.png','Goals 8.png',
             'Assists 8.png','Shots 8.png','xG 8.png',
             'Passes 8.png','Crosses 8.png',
             'Crosses 8.png', 'Dribbles 8.png', 'Duels 8.png',
             'Aerial duels 8.png', 'Interceptions 8.png',
             'Losses 8.png', 'Recoveries 8.png',
             'Defensive duels 8.png',
             'Loose ball duels 8.png', 'Sliding tackles 8.png', 'Clearances 8.png',
             'Fouls 8.png',
             'Yellow cards 8.png', 'Red cards 8.png',
             'Shot assists 8.png', 'Offensive duels 8.png', 'Touches in penalty area 8.png',
             'Progressive runs 8.png','Fouls suffered 8.png','Through passes 8.png',
             'xA 8.png','Second assists 8.png','Passes to final third 8.png',
             'Passes to penalty area 8.png','Received passes 8.png'],
    "Goalkeeper":['Total actions 8.png','Passes 8.png','Long passes 8.png','Dribbles 8.png','Duels 8.png','Aerial duels 8.png','Interceptions 8.png','Defensive duels 8.png',
                  'Loose ball duels 8.png','Sliding tackles 8.png','Clearances 8.png','Fouls 8.png','Yellow cards 8.png','Red cards 8.png',
                  'Fouls suffered 8.png','Received passes 8.png','Conceded goals 8.png','xCG 8.png','Shots against 8.png',
                  'Exits 8.png','Goal kicks 8.png','Short goal kicks 8.png','Long goal kicks 8.png'
                  ]
}

POSITIONAL_POINT_UNIX = {
    "Attacking Midfielder": ['Total actions_8.png', 'Goals_8.png',
                                      'Assists_8.png', 'Shots_8.png', 'xG_8.png',
                                      'Passes_8.png', 'Crosses_8.png',
                                      'Crosses_8.png', 'Dribbles_8.png', 'Duels_8.png',
                                      'Aerial duels_8.png', 'Interceptions_8.png',
                                      'Losses_8.png', 'Recoveries_8.png',
                                      'Defensive duels_8.png',
                                      'Loose ball duels_8.png', 'Sliding tackles_8.png', 'Clearances_8.png',
                                      'Fouls_8.png',
                                      'Yellow cards_8.png', 'Red cards_8.png',
                                      'Shot assists_8.png', 'Offensive duels_8.png', 'Touches in penalty area_8.png',
                                      'Progressive runs_8.png', 'Fouls suffered_8.png', 'Through passes_8.png',
                                      'xA_8.png', 'Second assists_8.png', 'Passes to final third_8.png',
                                      'Passes to penalty area_8.png', 'Received passes_8.png', 'Forward passes_8.png',
                                      'Back passes_8.png'
                                      ],
    "Center Back": ['Total actions_8.png', 'Passes_8.png', 'Long passes_8.png',
                    'Dribbles_8.png', 'Duels_8.png',
                    'Aerial duels_8.png', 'Interceptions_8.png',
                    'Losses_8.png', 'Recoveries_8.png',
                    'Defensive duels_8.png',
                    'Loose ball duels_8.png', 'Sliding tackles_8.png', 'Clearances_8.png', 'Fouls_8.png',
                    'Yellow cards_8.png', 'Red cards_8.png',
                    'Shot assists_8.png', 'Offensive duels_8.png'
        , 'Fouls suffered_8.png', 'Through passes_8.png',
                    'Passes to final third_8.png',
                    'Passes to penalty area_8.png', 'Received passes_8.png', 'Forward passes_8.png',
                    'Back passes_8.png', 'Exits_8.png'
                    ],
    "Full Back": ['Total actions_8.png', 'Passes_8.png', 'Long passes_8.png',
                  'Crosses_8.png', 'Dribbles_8.png', 'Duels_8.png',
                  'Aerial duels_8.png', 'Interceptions_8.png',
                  'Losses_8.png', 'Recoveries_8.png',
                  'Defensive duels_8.png',
                  'Loose ball duels_8.png', 'Sliding tackles_8.png', 'Clearances_8.png', 'Fouls_8.png',
                  'Yellow cards_8.png', 'Red cards_8.png',
                  'Shot assists_8.png', 'Offensive duels_8.png', 'Touches in penalty area_8.png',
                  'Progressive runs_8.png', 'Fouls suffered_8.png', 'Through passes_8.png',
                  'xA_8.png', 'Second assists_8.png', 'Passes to final third_8.png',
                  'Passes to penalty area_8.png', 'Received passes_8.png', 'Forward passes_8.png',
                  'Back passes_8.png', 'Exits_8.png', 'Passes to goalkeeper_8.png',
                  ],
    "Defensive Midfielder": ['Total actions_8.png','Passes_8.png','Long passes_8.png',
                  'Dribbles_8.png', 'Duels_8.png',
                  'Aerial duels_8.png', 'Interceptions_8.png',
                  'Losses_8.png', 'Recoveries_8.png','Defensive duels_8.png',
                   'Loose ball duels_8.png', 'Sliding tackles_8.png', 'Clearances_8.png', 'Fouls_8.png',
                   'Yellow cards_8.png', 'Red cards_8.png',
                   'Shot assists_8.png', 'Offensive duels_8.png',
                    'Fouls suffered_8.png','Through passes_8.png','Passes to final third_8.png',
                   'Passes to penalty area_8.png', 'Received passes_8.png', 'Forward passes_8.png',
                   'Back passes_8.png','Exits_8.png'],
    "Winger": ['Total actions_8.png', 'Goals_8.png',
               'Assists_8.png', 'Shots_8.png', 'xG_8.png',
               'Passes_8.png', 'Crosses_8.png',
               'Crosses_8.png', 'Dribbles_8.png', 'Duels_8.png',
               'Aerial duels_8.png', 'Interceptions_8.png',
               'Losses_8.png', 'Recoveries_8.png',
               'Defensive duels_8.png',
               'Loose ball duels_8.png', 'Sliding tackles_8.png', 'Clearances_8.png',
               'Fouls_8.png',
               'Yellow cards_8.png', 'Red cards_8.png',
               'Shot assists_8.png', 'Offensive duels_8.png', 'Touches in penalty area_8.png',
               'Progressive runs_8.png', 'Fouls suffered_8.png', 'Through passes_8.png',
               'xA_8.png', 'Second assists_8.png', 'Passes to final third_8.png',
               'Passes to penalty area_8.png', 'Received passes_8.png'
               ],
    "Striker": ['Total actions_8.png', 'Goals_8.png',
                'Assists_8.png', 'Shots_8.png', 'xG_8.png',
                'Passes_8.png', 'Crosses_8.png',
                'Crosses_8.png', 'Dribbles_8.png', 'Duels_8.png',
                'Aerial duels_8.png', 'Interceptions_8.png',
                'Losses_8.png', 'Recoveries_8.png',
                'Defensive duels_8.png',
                'Loose ball duels_8.png', 'Sliding tackles_8.png', 'Clearances_8.png',
                'Fouls_8.png',
                'Yellow cards_8.png', 'Red cards_8.png',
                'Shot assists_8.png', 'Offensive duels_8.png', 'Touches in penalty area_8.png',
                'Progressive runs_8.png', 'Fouls suffered_8.png', 'Through passes_8.png',
                'xA_8.png', 'Second assists_8.png', 'Passes to final third_8.png',
                'Passes to penalty area_8.png', 'Received passes_8.png'],
    "Goalkeeper": ['Total actions_8.png', 'Passes_8.png', 'Long passes_8.png', 'Dribbles_8.png', 'Duels_8.png',
                   'Aerial duels_8.png', 'Interceptions_8.png', 'Defensive duels_8.png',
                   'Loose ball duels_8.png', 'Sliding tackles_8.png', 'Clearances_8.png', 'Fouls_8.png',
                   'Yellow cards_8.png', 'Red cards_8.png',
                   'Fouls suffered_8.png', 'Received passes_8.png', 'Conceded goals_8.png', 'xCG_8.png',
                   'Shots against_8.png',
                   'Exits_8.png', 'Goal kicks_8.png', 'Short goal kicks_8.png', 'Long goal kicks_8.png'
                   ]
}

USERNAME = 'loran@tactalyze'
PASSWORD = 'randomCat@123'
