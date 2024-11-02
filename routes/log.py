from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.log import LogModel
from database import get_db

log_router = APIRouter()


@log_router.get("/")
async def get_logs(db: Session = Depends(get_db)):
    return db.query(LogModel).all()
