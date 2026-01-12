from pydantic import BaseModel ,IPv4Address

class IpData(BaseModel):
    ip:IPv4Address
    coordinates:str