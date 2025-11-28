from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from datetime import datetime

from typing import Optional

from tortoise.fields import Field

from . import models


Script_Pydantic = pydantic_model_creator(models.Script, name="Script")


class ChangeScriptStatusSchema(BaseModel):
    name: str = Field()
    status: models.ScriptStatus = models.ScriptStatus.INACTIVE

class ChangeScriptFirstSeenSchema(BaseModel):
    name: str
    first_seen: datetime = datetime.now()

class ChangeScriptFingerprintSchema(BaseModel):
    name: str
    fingerprint: str

class CreateScriptSchema(BaseModel):
    name: Optional[str] = None