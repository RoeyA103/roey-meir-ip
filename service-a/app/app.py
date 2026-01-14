import uvicorn
from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return "Message: To send IP, run a POST request to '/getcond', to get all coordinates, run a GET request '/getcond' to list all saved ip:coordinates"




if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost",port=8000 , reload=True)
