from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from core.db import Base


class Script(Base):
    __tablename__ = "scripts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(10), index=True)
    fingerprint = Column(String, nullable=True)

    first_seen = Column(DateTime, default=datetime.utcnow)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"Script(id={self.id}, name={self.name})"
    
