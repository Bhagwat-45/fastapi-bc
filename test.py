import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="root",
        database="postgres",   # <-- change only this
    )

    print(await conn.fetch("SELECT current_database(), version()"))
    await conn.close()

asyncio.run(main())