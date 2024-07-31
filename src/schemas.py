import uuid

from pydantic import BaseModel, Field


class EventResponse(BaseModel):
    id: uuid.UUID
    status: str

    class Config:
        orm_mode = True
        from_attributes = True


class BetCreate(BaseModel):
    event_id: uuid.UUID
    amount: float = Field(..., gt=0)


class BetResponse(BaseModel):
    id: uuid.UUID
    amount: float
    event: EventResponse

    class Config:
        orm_mode = True
        from_attributes = True


class EventUpdate(BaseModel):
    status: str
