import asyncio
from src.postgresql_database_session import (
    ensure_database_exists,
    engine,
    Base,
) 

async def run_migrations():
    await ensure_database_exists()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
asyncio.run(run_migrations())