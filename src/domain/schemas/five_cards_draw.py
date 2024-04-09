from .generic_schema import GenericSchema
from pydantic import UUID, Field, EmailStr
import uuid


class MatchIn(GenericSchema):
    match_id: UUID = Field(default=uuid.uuid4)
    cards: list[str] = []
    opponent_id: EmailStr = Field(default="johndoe@mail.com")


class MatchOut(GenericSchema):
    bet: int = Field(default=5)
    cards_to_swap: list[str] = []
