from fastapi import APIRouter
from pydantic import BaseModel, Field
from ipaddress import IPv4Address
from schemas import landmark

class Ip(BaseModel):
    ip: IPv4Address
    # ip: str = Field(regex=r'^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$')

router = APIRouter(prefix="/getcond")

@router.post("/")
def get_condinator(ip:Ip):
    return landmark(ip)
