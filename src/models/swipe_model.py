from sqlalchemy.orm import Mapped, mapped_column

from src.config.database import Base


class SwipeDB(Base):
    __tablename__ = "swipes"

    user_a_id: Mapped[int]
    user_b_id: Mapped[int]
    decision_a: Mapped[bool | None] = mapped_column(nullable=True)
    decision_b: Mapped[bool | None] = mapped_column(nullable=True)
