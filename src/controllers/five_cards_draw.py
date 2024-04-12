from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.domain.schemas.five_cards_draw import FirstRoundIn, FirstRoundOut, SecondRoundIn, SecondRoundOut, \
    RoundResultIn, Login

from src.config.database import get_session
from src.services import five_cards_draw as five_cards_draw_service

router = APIRouter()

POKER_TAG = "Poker: Five Cards Draw"


@router.post("/first-round", summary="First round of Five Cards Draw", tags=[POKER_TAG], response_model=FirstRoundOut)
def first_round(match: FirstRoundIn, db: Session = Depends(get_session)):
    return five_cards_draw_service.first_round(match, db)


@router.post("/second-round", summary="Second round of Five Cards Draw", tags=[POKER_TAG],
             response_model=SecondRoundOut)
def second_round(match: SecondRoundIn, db: Session = Depends(get_session)):
    return five_cards_draw_service.second_round(match, db)


@router.post("/result", summary="Result of Five Cards Draw", tags=[POKER_TAG])
def result(match: RoundResultIn, db: Session = Depends(get_session)):
    return five_cards_draw_service.result(match, db)


@router.get("/health/liveness", summary="Health check for Five Cards Draw", tags=[POKER_TAG], status_code=200)
def health():
    return {"status": "ok"}


@router.post("/join-game", summary="Join a game of Five Cards Draw", tags=[POKER_TAG], response_model=Login,
             status_code=200)
def join_game(login: Login, db: Session = Depends(get_session)):
    return five_cards_draw_service.join_game(login)
