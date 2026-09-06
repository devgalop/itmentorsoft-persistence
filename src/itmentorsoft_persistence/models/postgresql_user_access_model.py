
from itmentorsoft_persistence.postgresql_database_session import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from datetime import datetime


class UserAccessEntity(Base):
    __tablename__ = "user_access"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), nullable=False)
    retry_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    block_time_seconds: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    blocked: Mapped[bool] = mapped_column(nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())