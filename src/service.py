import uuid
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from src.exceptions import EventNotFoundException
from src.models import Bet, Event
from src.schemas import BetResponse


async def create_bet(
    db: AsyncSession, event_id: uuid.UUID, amount: float
) -> BetResponse:
    result = await db.execute(select(Event).filter(Event.id == event_id))
    event = result.scalar_one_or_none()

    if event is None:
        raise EventNotFoundException()

    new_bet = Bet(event_id=event_id, amount=amount)
    db.add(new_bet)
    await db.commit()
    await db.refresh(new_bet)

    return BetResponse(
        id=new_bet.id,
        amount=new_bet.amount,
        event_id=event.id,
        event=Event(id=event.id, status=event.status),
    )


async def get_bets(db: AsyncSession) -> list[BetResponse]:
    result = await db.execute(select(Bet).options(selectinload(Bet.event)))
    bets = result.scalars().all()

    bet_responses = []
    for bet in bets:
        bet_responses.append(BetResponse(id=bet.id, amount=bet.amount, event=bet.event))

    return bet_responses


async def update_event_status(
    db: AsyncSession, event_id: uuid.UUID, status: str
) -> list[BetResponse]:
    result = await db.execute(select(Event).filter(Event.id == event_id))
    event = result.scalar_one_or_none()

    if event is None:
        return []

    event.status = status

    await db.commit()

    result = await db.execute(select(Bet).filter(Bet.event_id == event_id))
    bets = result.scalars().all()

    return [BetResponse.from_orm(bet) for bet in bets]


async def get_events(db: AsyncSession) -> Sequence[Event]:
    result = await db.execute(select(Event))
    return result.scalars().all()
