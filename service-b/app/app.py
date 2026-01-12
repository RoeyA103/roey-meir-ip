from fastapi import FastAPI
from routes import locations_router
from schemas import *


app = FastAPI()

@app.get("/")
def health():
    return {"Message":"GET /locations return all redis storege , POST /locations get {ip:coordinates}"}

app.include_router(locations_router)
