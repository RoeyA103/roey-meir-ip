import os
import requests
from dotenv import load_dotenv

load_dotenv()

def process_ip(ip: str)->dict:
    try:
        location = get_ip_location(ip)
        result = send_location_to_service(ip,location)
        return {
            "sent": True,
            "location": location,
            "remote_response": result
        }
    except requests.RequestException as e:
        return {"sent": False, "error": str(e)}
    except ValueError as e:
        return {"sent": False, "error": str(e)}


def get_ip_location(ip:str)->dict:
    url = f"{os.getenv('IP_API')}{ip}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()

    if data.get("status") != "success":
        raise ValueError("IP location lookup failed")
    return {"lat": data["lat"], "lon": data["lon"]}



def send_location_to_service(ip,location: dict) -> dict:
    url = f"{os.getenv('REDIS_HOST')}/locations"
    payload = {
        "ip": ip,
        "coordinates":{
            "lat": location["lat"],
            "lon": location["lon"]
        }
    }
    response = requests.post(url,json=payload,timeout=5)
    response.raise_for_status()
    return response.json()

def get_all_coordinates():
    url = f"{os.getenv('REDIS_HOST')}/locations"
    response = requests.get(url,timeout=5)
    response.raise_for_status()
    return response.json()

def coordinates_to_map():
    url = f"{os.getenv('STREAMLIT_HOST')}/locations"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response