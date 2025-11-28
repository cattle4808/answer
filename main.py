from fastapi import FastAPI

from core import db
from v1 import router as v1_router

app = FastAPI()
app.include_router(v1_router)

@app.on_event("startup")
async def startup_event():
    await db.init()

@app.on_event("shutdown")
async def shutdown_event():
    await db.close()