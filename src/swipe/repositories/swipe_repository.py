from dataclasses import dataclass

from sqlalchemy import and_, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.swipe_model import SwipeDB


@dataclass
class SwipeRepository:
    db_session: AsyncSession

    async def get_swiped_from_existed_swipes(
            self, swiped_users: list, user_id: int
    ) -> list[int]:
        """Получение списка id юзеров, с которыми есть свайп у текущего юзера"""

        query = select(SwipeDB.user_a_id).where(
            and_(SwipeDB.user_a_id.in_(swiped_users), SwipeDB.user_b_id == user_id)
        )
        async with self.db_session as session:
            user_ids: list[int] = (await session.execute(query)).scalars().all()
            return user_ids

    async def update_swipes(
            self, users_from_existed_swipes: list[int], user_id
    ) -> None:
        """Обновление свайпов для юзеров, у  которых есть свайп с текущим юзером"""
        query = (
            update(SwipeDB)
            .where(
                and_(
                    SwipeDB.user_a_id.in_(users_from_existed_swipes),
                    SwipeDB.user_b_id == user_id,
                )
            )
            .values(decision_b=True)
        )

        async with self.db_session as session:
            await session.execute(query)
            await session.commit()

    async def create_swipes(self, users_for_swipes: list[int], user_id: int) -> None:
        """Создаение свайпов"""
        query = insert(SwipeDB).values(
            [
                {"user_a_id": user_id, "user_b_id": user_for_swipe, "decision_a": True}
                for user_for_swipe in users_for_swipes
            ]
        )
        async with self.db_session as session:
            await session.execute(query)
            await session.commit()
