from ipaddress import IPv4Address

from pydantic import BaseModel


class Ip(BaseModel):
    ip: IPv4Address