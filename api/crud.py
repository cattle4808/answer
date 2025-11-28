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

async def change_status(
    script: models.Script,
    status: models.ScriptStatus
) -> models.Script | None:
    try:
        await script.update_from_dict({"status": status})
        await script.save()
        return script
    except Exception as e:
        print("change_script_status failed:", e)
        return None

async def change_first_seen(
    script: models.Script,
    first_seen: datetime
) -> models.Script | None:
    try:
        await script.update_from_dict({"first_seen": first_seen})
        await script.save()
        return script
    except Exception as e:
        print("change_script_first_seen failed:", e)
        return None

async def change_fingerprint(
    script: models.Script,
    fingerprint: str
) -> models.Script | None:
    try:
        await script.update_from_dict({"fingerprint": fingerprint})
        await script.save()
        return script
    except Exception as e:
        print("change_script_fingerprint failed:", e)
        return None