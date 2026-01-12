from fastapi import APIRouter
from schemas import IpData
from services import *

locations_router = APIRouter(
    prefix="/locations",
    tags=["Locations Storage"])

rh = RedisHandler()

@locations_router.GET("/")
def get_all_data():
    result = rh.fetch_all()

    return result if result else {"error"}

locations_router.post("/")
def insert_data(data:IpData):
    success = rh.insert(data)
    if not success:
        return {"error": "Failed to save to Redis"}
    return {"message": f"Data for {str(data.ip)} stored successfully"}