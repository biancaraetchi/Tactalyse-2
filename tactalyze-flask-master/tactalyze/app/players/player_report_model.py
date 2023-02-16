from dataclasses import dataclass

from sqlalchemy import Integer, String, Column, Date, BLOB, ForeignKey
from app import db


@dataclass
class PlayersReport(db.Model):
    __tablename__ = "players_interim_report"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    position = Column(String, nullable=False)
    name = Column(String, nullable=False)
    competition = Column(String, nullable=False)

    def __init__(self, player_id, pos, name, comp
                 ):
        self.name = name
        self.position = pos
        self.player_id = player_id
        self.competition = comp
