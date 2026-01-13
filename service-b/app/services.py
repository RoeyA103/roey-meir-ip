from schemas import IpData
from abc import ABC, abstractmethod
import redis
import json

class BaseStorage(ABC):
    @abstractmethod
    def insert(self, data) -> bool:
        pass

    @abstractmethod
    def fetch_all(self) -> list:
        pass

class RedisHandler(BaseStorage):
    def __init__(self,host,port):
        self.hash_name = "locations"
        self.host = host
        self.port = port



    def insert(self, data: IpData) -> bool:
        try:
            r = redis.Redis(host=self.host , port=self.port)

            ip_str = str(data.ip)
            coord_json = json.dumps(data.coordinates.dict())
            
            r.hset(self.hash_name, ip_str, coord_json)

            r.close()
            return True
        except Exception as e:
            print(f"Error saving {data.ip}: {e}")
            return False


    def fetch_all(self):
        try:
            r = redis.Redis(host=self.host , port=self.port ,decode_responses=True)

            raw = r.hgetall(self.hash_name)
            return [
                IpData(ip=ip, coordinates=json.loads(val)) 
                for ip, val in raw.items()
            ]
        except Exception:
            return []