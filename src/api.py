import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.exceptions import InvalidEventStatusException
from src.schemas import BetCreate, BetResponse, EventResponse, EventUpdate
from src.service import create_bet, get_bets, get_events, update_event_status

router = APIRouter()

get_db_session = Depends(get_db)


@router.post("/bets", response_model=BetResponse)
async def create_bet_endpoint(bet: BetCreate, db: AsyncSession = get_db_session):
    return await create_bet(db, bet.event_id, bet.amount)


@router.get("/bets", response_model=list[BetResponse])
async def get_bets_endpoint(db: AsyncSession = get_db_session):
    return await get_bets(db)


@router.put("/events/{event_id}")
async def update_event_endpoint(
    event_id: uuid.UUID, event_update: EventUpdate, db: AsyncSession = get_db_session
):
    if event_update.status not in ["WIN", "LOSE"]:
        raise InvalidEventStatusException()
    updated_bets = await update_event_status(db, event_id, event_update.status)
    return {"updated_bets": len(updated_bets)}


@router.get("/events", response_model=list[EventResponse])
async def get_events_endpoint(db: AsyncSession = get_db_session):
    events = await get_events(db)
    return [EventResponse.from_orm(event) for event in events]
