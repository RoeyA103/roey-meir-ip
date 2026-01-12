from fastapi import FastAPI
from routes import locations_router
import uvicorn


app = FastAPI()

@app.get("/")
def root():
    return {"Message":"GET /locations return all redis storege , POST /locations send {ip,coordinates}"}

app.include_router(locations_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
