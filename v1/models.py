from tortoise import fields, models
from enum import StrEnum


class ScriptStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    LIMIT = "limit"
    EXPIRED = "expired"


class BaseModel(models.Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True

class Script(BaseModel):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=10, unique=True)

    status = fields.CharEnumField(
        enum_type=ScriptStatus,
        default=ScriptStatus.INACTIVE,
        max_length=255,
    )
    fingerprint = fields.CharField(max_length=255, null=True)
    first_seen = fields.DatetimeField(null=True)

    def __str__(self):
        return f"{self.id}:{self.name}"

    class Meta:
        table = "scripts"

class Answer(BaseModel):
    id = fields.IntField(primary_key=True)
    script = fields.ForeignKeyField("models.Script", related_name="answers")

    answer_path = fields.TextField()
    output = fields.TextField(null=True)

    def __str__(self):
        return f"{self.id}:{self.script.name}"

    class Meta:
        table = "answers"


