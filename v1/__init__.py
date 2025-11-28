from fastapi import APIRouter

from . import models
from . import crud
from . import services


router = APIRouter()


@router.post("/scripts/create")
async def create_script():
    return await services.generate_script()

@router.post("/scripts/{name}/change_status")
async def change_script_status(name: int, status: models.ScriptStatus):
    return await services.change_script_status(name, status)

