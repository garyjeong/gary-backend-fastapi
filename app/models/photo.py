from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from app.database.session import Base


class Photo(Base):
    __tablename__ = "photo"
    __table_args__ = {"comment": "포토북, 사진 데이터"}

    uuid: UUID = Column(
        UUIDType(binary=False),
        primary_key=True,
        unique=True,
        default=uuid4,
        comment="사진 UUID, Front 제공용 ID",
    )

    memo: Optional[str] = Column(String(1000), nullable=True, comment="사진 메모")
    url: str = Column(String(500), nullable=False, comment="사진 URL")
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    folder_uuid: UUID = Column(
        UUIDType(binary=False),
        ForeignKey("folder.uuid"),
        nullable=False,
        comment="폴더 UUID",
    )
