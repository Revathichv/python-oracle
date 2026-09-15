import asyncio
import oracledb

async def main():
    # Initialize the async pool
    pool = await oracledb.create_pool_async(
        user="your_username",
        password="your_password",
        dsn="your_host:1521/your_service_name",
        min=2,
        max=10
    )

    # Acquire and use connection asynchronously
    async with pool.acquire() as connection:
        async with connection.cursor() as cursor:
            await cursor.execute("SELECT USER FROM DUAL")
            result = await cursor.fetchone()
            print(f"Async connected as: {result[0]}")

    # Clean up the pool
    await pool.close()

asyncio.run(main())
