from fastapi import APIRouter
from schemas import IpData
from services import *
from dotenv import load_dotenv
import os

load_dotenv()  

db_host = os.getenv("DATABASE_HOST")
db_port = os.getenv("DATABASE_PORT",6379)

locations_router = APIRouter(
    prefix="/locations",
    tags=["Locations Storage"])

rh = RedisHandler(host=db_host,port=db_port)

@locations_router.get("/")
def get_all_data():
    result = rh.fetch_all()

    return result if result else {"error"}

@locations_router.post("/")
def insert_data(data:IpData):
    success = rh.insert(data)
    if not success:
        return {"error": "Failed to save to Redis"}
    return {"message": f"Data for {str(data.ip)} stored successfully"}