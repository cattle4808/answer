from . import models
from datetime import datetime


async def create_script(
        name: str,
        status: models.ScriptStatus,
        fingerprint: str | None = None,
    ) -> models.Script:
    return await models.Script.create(
        name=name,
        status=status,
        fingerprint=fingerprint,
    )


async def get_script_by_name(
        name: str,
    ) -> models.Script | None:
    return await models.Script.get_or_none(name=name)

