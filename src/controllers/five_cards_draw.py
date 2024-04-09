from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.five_cards_draw import MatchIn, MatchOut

from config.database import get_session
from services import five_cards_draw as five_cards_draw_service

router = APIRouter()

POKER_TAG = "Poker: Five Cards Draw"


@router.post("/first-round", summary="First round of Five Cards Draw", tags=[POKER_TAG], response_model=MatchOut)
def first_round(match: MatchIn, db: Session = Depends(get_session)):
    return five_cards_draw_service.first_round(match, db)