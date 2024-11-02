from sqlalchemy import Column, DateTime, Integer, String

from database import Base


class LogModel(Base):
    __tablename__ = "logs"

    log_id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    created_at = Column(DateTime)