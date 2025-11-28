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
async def change_script_status(params=Depends(schemas.ChangeScriptStatusSchema)):
    script = await crud.get_script_by_name(params.name)
    if not script:
        return Response(status_code=500)
    return await crud.change_status(script, params.status)

@router.patch("/{name}/change_first_seen", response_model=schemas.Script_Pydantic)
async def change_script_first_seen(params=Depends(schemas.ChangeScriptFirstSeenSchema)):
    script = await crud.get_script_by_name(params.name)
    if not script:
        return Response(status_code=500)
    return await crud.change_first_seen(script, params.first_seen)

@router.patch("/{name}/change_fingerprint", response_model=schemas.Script_Pydantic)
async def change_script_fingerprint(params=Depends(schemas.ChangeScriptFingerprintSchema)):
    script = await crud.get_script_by_name(params.name)
    if not script:
        return Response(status_code=500)
    return await crud.change_fingerprint(script, params.fingerprint)