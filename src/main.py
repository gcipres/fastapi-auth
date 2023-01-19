from fastapi import FastAPI
from src.auth import routers as auth_routers

app = FastAPI()

#Routes
app.include_router(auth_routers.router)

@app.get("/ping")
async def root():
    return "auth app is running!"
