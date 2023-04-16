from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from app.database.session import Base


class Folder(Base):
    __tablename__ = "folder"
    __table_args__ = {"comment": "사진첩 폴더"}

    uuid: UUID = Column(
        UUIDType(binary=False),
        primary_key=True,
        unique=True,
        default=uuid4,
        comment="폴더 UUID, Front 제공용 ID",
    )

    name: str = Column(String(50), nullable=False, comment="폴더 이름")
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    photos = relationship("Photo", back_populates="folder")
