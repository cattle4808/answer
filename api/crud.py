from typing import Optional, Any
from . import models


async def create_script(
    name: str,
    status: models.ScriptStatus,
    max_used: int = 50
) -> models.Script:
    return await models.Script.create(
        name=name,
        status=status,
        max_used=max_used,
    )

async def get_script_by_name(name: str) -> Optional[models.Script]:
    return await models.Script.get_or_none(name=name)

async def update_script_fields(script: models.Script, **fields: Any) -> models.Script:
    await script.update_from_dict(fields)
    await script.save()
    return await models.Script.get(id=script.id)

async def change_status(script: models.Script, status: models.ScriptStatus) -> models.Script:
    return await update_script_fields(script, status=status)

async def change_first_seen(script: models.Script, first_seen) -> models.Script:
    return await update_script_fields(script, first_seen=first_seen)

async def change_fingerprint(script: models.Script, fingerprint: str) -> models.Script:
    return await update_script_fields(script, fingerprint=fingerprint)
