# validators.py
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException, status
from . import models
from core.configs import settings

def base_script_found_validate(script: models.Script):
    if not script:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="script_not_found")

def validate_used(script: models.Script):
    base_script_found_validate(script)
    if script.max_used is not None and script.used >= script.max_used:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="usage_limit_reached")

def validate_first_seen(script: models.Script):
    base_script_found_validate(script)
    if not script.first_seen:
        return
    now = datetime.now(timezone.utc)
    limit_time = script.first_seen + timedelta(minutes=settings.SCRIPT_ACTIVE_TIME_MINUTES)
    if now > limit_time:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="usage_time_expired")
