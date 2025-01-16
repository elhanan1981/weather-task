from fastapi import APIRouter
from database.create_tables import initialize_database
import logging

router = APIRouter()

@router.put("/init")
async def startup_event():
    if not initialize_database():
        logging.error("Failed to initialize database!")
        return {"message": "The init failed!"}
    return {"message": "The init succeeded!"}

@router.get("/")
async def check_connection():
    return {"message": "Welcome to Weather API"}

