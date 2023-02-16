import datetime
class Players():
    name = ""
    position = ""
    height = ""
    dob = datetime.date
    agent = ""
    club = ""
    country = ""
    league = ""

    def __init__(self, name, position, height, dob,  agent, club, league, country
                 ):
        self.name = name
        self.position = position
        self.height = height
        self.dob = dob
        self.agent = agent
        self.club = club
        self.country = country
        self.league = league