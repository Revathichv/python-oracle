import oracledb

# 1. Initialize the connection pool
pool = oracledb.create_pool(
    user="your_username",
    password="your_password",
    dsn="your_host:1521/your_service_name",
    min=2,             # Minimum connections to keep open
    max=10,            # Maximum allowed connections
    increment=1,       # How many connections to add when pool is full
    getmode=oracledb.POOL_GETMODE_WAIT
)

# 2. Acquire a connection from the pool
# Using a context manager automatically returns the connection to the pool when done
with pool.acquire() as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT USER FROM DUAL")
        result = cursor.fetchone()
        print(f"Connected as: {result[0]}")

# 3. Close the pool during application shutdown
pool.close()
