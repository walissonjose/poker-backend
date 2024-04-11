from .generic_schema import GenericSchema
from pydantic import Field, EmailStr
import uuid
from uuid import UUID


class FirstRoundIn(GenericSchema):
    match_id: UUID = Field(default=uuid.uuid4)
    cards: list[str] = []
    opponent_id: EmailStr = Field(default="johndoe@mail.com")


class FirstRoundOut(GenericSchema):
    bet: int = Field(default=5)
    cards_to_swap: list[str] = []


class SecondRoundIn(GenericSchema):
    match_id: UUID = Field(default=uuid.uuid4)
    new_cards: list[str] = []
    match_bet: int = Field(default=5)
    

class SecondRoundOut(GenericSchema):
    bet: int = Field(default=5)

