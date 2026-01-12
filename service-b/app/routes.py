from fastapi import APIRouter
from schemas import IpData

locations_router = APIRouter(
    prefix="/locations",
    tags=["Locations Storage"])


@locations_router.GET("/")
def get_all_data():
    pass

locations_router.post("/")
def insert_data(data:IpData):
    pass