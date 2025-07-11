from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.broker.kafka_accessor import get_aiokafka_consumer
from src.config.database import get_db_session
from src.config.project_config import Settings
from src.swipe.adapters.consumers.kafka_consumer import BrokerConsumer
from src.swipe.repositories.swipe_repository import SwipeRepository


async def get_swipe_repository(
    db_session: AsyncSession = Depends(get_db_session),
) -> SwipeRepository:
    return SwipeRepository(db_session=db_session)


async def get_broker_consumer() -> BrokerConsumer:
    aiokafka_consumer = get_aiokafka_consumer()
    db_session = await get_db_session().__anext__()
    swipe_repository = SwipeRepository(db_session=db_session)
    return BrokerConsumer(
        consumer=aiokafka_consumer,
        settings=Settings(),
        swipe_repository=swipe_repository,
    )
