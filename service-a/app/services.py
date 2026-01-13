import requests



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
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()

    if data.get("status") != "success":
        raise ValueError("IP location lookup failed")
    return {"latitude": data["lat"], "longitude": data["lon"]}



def send_location_to_service(ip,location: dict) -> dict:
    url = "http://api-b-service:8080/location"

    payload = {
        "ip": ip,
        "cordinates":{
            "latitude": location["latitude"],
            "longitude": location["longitude"]
        }
    }
    response = requests.post(url,json=payload,timeout=5)

    response.raise_for_status()

    return response.json()