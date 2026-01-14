from fastapi import APIRouter
from services import process_ip, get_all_coordinates
from schemas import Ip

router = APIRouter(prefix="/getcond")



@router.post("/")
def create_coordinate(ip:Ip):
    return process_ip(str(ip.ip))

@router.get("/")
def coordinates():
    return get_all_coordinates()