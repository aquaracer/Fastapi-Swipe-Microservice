from dataclasses import dataclass

from aiokafka import AIOKafkaConsumer

from src.config.project_config import Settings
from src.swipe.exceptions.swipe_exceptions import ProcessingBrokerMessageError
from src.swipe.repositories.swipe_repository import SwipeRepository


@dataclass
class BrokerConsumer:
    consumer: AIOKafkaConsumer
    settings: Settings
    swipe_repository: SwipeRepository

    async def open_connection(self) -> None:
        await self.consumer.start()

    async def close_connection(self) -> None:
        await self.consumer.stop()

    async def consume_message(self) -> None:
        await self.open_connection()

        try:
            async for message in self.consumer:
                if (
                        message.value.get("event")
                        == self.settings.EVENT_TYPE_PROCESS_SWIPES
                ):
                    await self.process_swipes(
                        swiped_users=message.value.get("swiped_users"),
                        user_id=message.value.get("user_id"),
                    )
        except Exception as error:
            raise ProcessingBrokerMessageError(error) from error
        finally:
            await self.close_connection()

    async def process_swipes(self, swiped_users: list[int], user_id: int) -> None:
        """Обработка свайпов"""

        users_from_existed_swipes = (
            await self.swipe_repository.get_swiped_from_existed_swipes(
                swiped_users=swiped_users, user_id=user_id
            )
        )
        if users_from_existed_swipes:
            await self.swipe_repository.update_swipes(
                users_from_existed_swipes=users_from_existed_swipes, user_id=user_id
            )
            remain_swiped_users = list(
                set(swiped_users) - set(users_from_existed_swipes)
            )
            if remain_swiped_users:
                await self.swipe_repository.create_swipes(
                    users_for_swipes=remain_swiped_users, user_id=user_id
                )
        else:
            await self.swipe_repository.create_swipes(
                users_for_swipes=swiped_users, user_id=user_id
            )
