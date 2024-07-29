from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database_connection import database_handler


Base = database_handler.base


class Users(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
