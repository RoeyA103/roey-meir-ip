from fastapi import APIRouter
from services import process_ip
from schemas import Ip

router = APIRouter(prefix="/getcond")



@router.post("/")
def get_condinator(ip:Ip):
    return process_ip(str(ip.ip))
