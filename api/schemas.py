from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from typing import Optional

from . import models


Script_Pydantic = pydantic_model_creator(models.Script, name="Script")


class ChangeScriptStatusSchema(BaseModel):
    name: str
    status: models.ScriptStatus

class CreateScriptSchema(BaseModel):
    name: Optional[str] = None