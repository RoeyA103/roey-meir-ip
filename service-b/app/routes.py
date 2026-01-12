from fastapi import APIRouter

locations_router = APIRouter(
    prefix="/locations",
    tags=["Locations Storage"])


@locations_router.GET("/")
def get_all_data():
    pass

locations_router.post("/")
def insert_data(data:IpData):
    pass