from sqlalchemy.orm import Session
from src.domain.models.game import Game


def create_game(game: Game, db: Session):
    db.add(game)
    db.commit()
    db.refresh(game)
    return game


def get_game(match_id, db):
    return db.query(Game).filter(Game.id == match_id).first()


def update_game(game: Game, db: Session):
    db.commit()
    db.refresh(game)
    return game
