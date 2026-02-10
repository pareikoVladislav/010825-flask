from datetime import datetime, date, UTC
from decimal import Decimal

from sqlalchemy import Integer, String, Float, UniqueConstraint, DateTime, ForeignKey, Date, Numeric
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from practicums.practicum_2.database_connection import engine


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
    )

