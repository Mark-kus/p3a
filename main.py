from fastapi import FastAPI

from routes.user import user_router
from database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router, prefix="/user", tags=["user"])