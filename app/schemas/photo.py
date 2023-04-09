from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.mysql import UUID
from app.database.session import Base

class Photo(Base):
    __tablename__ = "photo"
    __table_args__ = {"comment" : "포토북, 사진 데이터"}
    
    id: int = Column(
        Integer, primary_key=True, autoincrement=True, comment="사진 Row ID"
    )
    uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, comment="사진 UUID, Front 제공용 ID")
    
    memo = Column(String(1000), nullable=True, comment="사진 메모")
    url = Column(String(500), nullable=False, comment="사진 URL")
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())
    deleted_at = Column(DateTime(), ondelete=datetime.now())
    
    
    
