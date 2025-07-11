from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.swipe.dependencies.swipe_dependency import get_broker_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):
    broker_consumer = await get_broker_consumer()
    await broker_consumer.consume_callback_message()
    yield


app = FastAPI(lifespan=lifespan)
