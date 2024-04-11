from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY, UUID, BOOLEAN
from .generic_model import GenericModel


class Game(GenericModel):
    __tablename__ = "game"
    id: UUID = Column('game_cd_game', UUID, primary_key=True)
    opponent_mail: str = Column('game_tx_opponent_email', String, nullable=False)
    hand: list[str] = Column('game_li_hand', ARRAY(String), nullable=False)
    result: str = Column('game_tx_result', String)
    first_bet: int = Column('game_nr_first_bet', Integer)
    opponent_first_bet: int = Column('game_nr_opponent_first_bet', Integer)
    game_pot: int = Column('game_nr_pot', Integer)
    balance: int = Column('game_nr_balance', Integer)