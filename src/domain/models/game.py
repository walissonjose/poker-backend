from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY, UUID, BOOLEAN
from .generic_model import GenericModel


class Game(GenericModel):
    __tablename__ = 'game'
    id: UUID = Column('game_cd_game', UUID, primary_key=True)
    opponent_mail: str = Column('game_tx_opponent_email', String, nullable=False)
    first_hand: list[str] = Column('game_li_first_hand', ARRAY(String), nullable=False)
    second_hand: list[str] = Column('game_li_second_hand', ARRAY(String))
    hand_changes: list[str] = Column('game_li_changes', ARRAY(String))
    is_finished: bool = Column('game_in_finished', BOOLEAN, default=False)
    result: str = Column('game_tx_result', String)
    first_bet: int = Column('game_nr_first_bet', Integer)
    second_bet: int = Column('game_nr_second_bet', Integer)
    game_pot: int = Column('game_nr_pot', Integer, default=(first_bet + second_bet))
    balance: int = Column('game_nr_balance', Integer)