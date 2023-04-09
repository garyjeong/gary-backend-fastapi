from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://user:password@postgresserver/db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, 
    pool_pre_ping=True, 
    pool_size=15, 
    max_overflow=0, 
)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args=SQLALCHEMY_ENGINE_CONNECTION_ARGS,
    pool_pre_ping=True,
)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

Base = declarative_base()
