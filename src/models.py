import uuid

from sqlalchemy import Column, Enum, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database import Base
from src.enums import EventStatus


class Event(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    status = Column(Enum(EventStatus))


class Bet(Base):
    __tablename__ = "bets"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    amount = Column(Float)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"))
    event = relationship("Event", back_populates="bets")


Event.bets = relationship("Bet", order_by=Bet.id, back_populates="event")
