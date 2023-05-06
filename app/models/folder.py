from uuid import UUID, uuid4

from sqlalchemy import TIMESTAMP, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.session import Base


class Folder(Base):
    __tablename__ = "folder"
    __table_args__ = {"comment": "사진첩 폴더"}

    uuid: UUID = Column(
        String(36),
        primary_key=True,
        unique=True,
        nullable=False,
        default=lambda: str(uuid4()),
        comment="폴더 UUID, Front 제공용 ID",
    )

    name: str = Column(
        String(20), nullable=False, comment="폴더 이름"
    )
    created_at = Column(
        TIMESTAMP(6),
        server_default=func.now(),
        nullable=False,
        comment="생성 일자",
    )
    updated_at = Column(
        TIMESTAMP(6),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="수정 일자",
    )
    deleted_at = Column(
        TIMESTAMP(6),
        nullable=True,
        default=None,
        comment="삭제 일자",
    )

    photos = relationship("Photo", back_populates="folder")
