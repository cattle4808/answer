import copy

from . import models
from . import crud
from core.configs import settings

from typing import Optional
import random



async def generate_name() -> Optional[str]:
    choices = settings.NAME_CHOICES
    min_len = settings.MIN_SCRIPT_NAME_LENGTH
    max_len = settings.MAX_SCRIPT_NAME_LENGTH
    fallback_len = settings.IF_SCRIPT_NAME_EXISTS
    max_attempts = settings.REPEAT_SCRIPT_NAME_GENERATE

    length = copy.copy(min_len)

    for _ in range(max_attempts):
        name = "".join(random.choice(choices) for _ in range(length))
        if await crud.get_script_by_name(name) is None:
            return name

        length += 1

    fallback = "".join(random.choice(choices) for _ in range(fallback_len))
    if await crud.get_script_by_name(fallback) is None:
        return fallback

    return None


async def generate_script(name: str = None) -> Optional[models.Script]:
    name = name or await generate_name()
    if not name:
        return None

    try:
        return await crud.create_script(
            name=name,
            status=models.ScriptStatus.INACTIVE,
        )
    except Exception as e:
        print("create_script failed:", e)
        return None

