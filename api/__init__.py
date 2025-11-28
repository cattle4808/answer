from fastapi import APIRouter, Depends
from starlette.responses import Response

from datetime import datetime

from . import models
from . import crud
from . import services
from . import schemas
from . import middleware


router = APIRouter(
    prefix='/api/scripts',
   # dependencies=[Depends(middleware.auth_required)]
)


@router.post("/create")
async def create_script():
    return await services.generate_script()

@router.patch("/{name}/change_status", response_model=schemas.Script_Pydantic)
async def change_script_status(name: str, status: models.ScriptStatus):
    script = await crud.get_script_by_name(name)
    if not script:
        return Response(status_code=500)
    return await crud.change_status(script, status)

@router.patch("/{name}/change_first_seen", response_model=schemas.Script_Pydantic)
async def change_script_first_seen(name: str, first_seen: datetime):
    script = await crud.get_script_by_name(name)
    if not script:
        return Response(status_code=500)
    return await crud.change_first_seen(script, first_seen)

@router.patch("/{name}/change_fingerprint", response_model=schemas.Script_Pydantic)
async def change_script_fingerprint(name: str, fingerprint: str):
    script = await crud.get_script_by_name(name)
    if not script:
        return Response(status_code=500)
    return await crud.change_fingerprint(script, fingerprint)