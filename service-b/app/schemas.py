from ipaddress import IPv4Address
from pydantic import BaseModel, Field

class Coordinates(BaseModel):
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)

class IpData(BaseModel):
    ip: IPv4Address
    coordinates: Coordinates
