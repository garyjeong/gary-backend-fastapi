import uuid

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.mysql import UUID
from app.database.session import Base

class Folder(Base):
    __tablename__ = "folder"
    __table_args__ = {"comment" : "사진첩 폴더"}
    
    id: int = Column(
        Integer, primary_key=True, autoincrement=True, comment="Row ID"
    )
    uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, comment="폴더 UUID, Front 제공용 ID")
    
    name = Column(String(50), nullable=False, comment="폴더 이름")
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())
    deleted_at = Column(DateTime(), ondelete=datetime.now())
    
    
    
