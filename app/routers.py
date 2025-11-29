from fastapi import APIRouter, HTTPException
from starlette.responses import Response

from api import get_script
from api import services
from api import validators
from api import crud

from . import BASE_SCRIPT


router = APIRouter()


@router.get("/script/{name}")
async def get_script_js(name: str):
    script = await crud.get_script_by_name(name)

    if not script:
        return Response(status_code=500)

    try:
        validators.validate_used(script)
    except HTTPException as e:
        return Response(status_code=500)

    return Response(
        content=BASE_SCRIPT,
        media_type="application/javascript",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Cache-Control": "no-store",
            "X-Content-Type-Options": "nosniff",
        },
    )

