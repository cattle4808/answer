from . import models
from datetime import datetime


async def create_script(
        name: str,
        status: models.ScriptStatus,
        fingerprint: str | None = None,
        first_seen: datetime | None = None,
    ) -> models.Script:
    return await models.Script.create(
        name=name,
        status=status,
        fingerprint=fingerprint,
        first_seen=first_seen,
    )


async def get_script_by_name(
        name: str,
    ) -> models.Script | None:
    return await models.Script.get_or_none(name=name)


async def change_script_status(
        script: models.Script,
        status: models.ScriptStatus,
    ) -> models.Script:
    return await script.update_from_dict({"status": status})
