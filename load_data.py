import asyncio
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db, init_db
from src.enums import EventStatus
from src.models import Bet, Event


async def init_test_data(db: AsyncSession):
    event1 = Event(id=uuid.uuid4(), status=EventStatus.NOT_PLAYED)
    event2 = Event(id=uuid.uuid4(), status=EventStatus.NOT_PLAYED)
    event3 = Event(id=uuid.uuid4(), status=EventStatus.NOT_PLAYED)
    event4 = Event(id=uuid.uuid4(), status=EventStatus.NOT_PLAYED)
    db.add_all([event1, event2, event3, event4])
    await db.commit()

    bet1 = Bet(id=uuid.uuid4(), amount=100.0, event_id=event1.id)
    db.add(bet1)
    await db.commit()


async def main():
    await init_db()

    async for session in get_db():
        await init_test_data(session)
        break


if __name__ == "__main__":
    asyncio.run(main())
