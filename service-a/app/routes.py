from fastapi import APIRouter
from pydantic import BaseModel
from ipaddress import IPv4Address
from schemas import process_ip


router = APIRouter(prefix="/getcond")

class Ip(BaseModel):
    ip: IPv4Address

@router.post("/")
def get_condinator(ip:Ip):
    return process_ip(str(ip.ip))
