from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Category(Base):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    # questions: Mapped[list["Question"]] = relationship(back_populates="category")

    questions = relationship(
        'Question',
        back_populates='category'
    )



