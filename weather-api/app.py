from fastapi import FastAPI
from dotenv import load_dotenv
from database.create_tables import initialize_database

import logging

load_dotenv()
app = FastAPI()
        
@app.put("/init")
async def startup_event():
    if not initialize_database():
        logging.error("Failed to initialize database!")
        return {"the init failed!!"}
    return {"the init successed!!"}

@app.get("/")
async def read_root():
    return {"message": "Welcome to Weather API"}
