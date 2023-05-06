from uuid import UUID, uuid4

from sqlalchemy import TIMESTAMP, VARCHAR, Column, ForeignKey, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.session import Base


class Photo(Base):
    __tablename__ = "photo"
    __table_args__ = {"comment": "포토북, 사진 데이터"}

    uuid = Column(
        String(36),
        primary_key=True,
        unique=True,
        nullable=False,
        default=lambda: str(uuid4()),
        comment="사진 UUID, Front 제공용 ID",
    )
    memo = Column(String(1000), nullable=True, comment="사진 메모")
    url = Column(String(400), nullable=False, comment="사진 URL")
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
        TIMESTAMP(6), nullable=True, default=None, comment="삭제 일자"
    )
    folder_uuid = Column(
        String(255),
        ForeignKey("folder.uuid", ondelete="CASCADE"),
        nullable=True,
        comment="폴더 UUID",
    )

    folder = relationship("Folder", back_populates="photos")
