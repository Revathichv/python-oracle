import oracledb

def get_connection():
    connection=None
    # 1. Define your connection parameters
    db_user = "xxx"
    db_password = "yyy"
    db_host = "localhost"
    db_port = "1521"
    db_service_name = "orcl" # Often something like 'ORCL' or 'XEPDB1'

    try:
        # 2. Establish the connection (Defaults to Thin Mode)
        # This automatically builds a connection string: host:port/service_name
        oracledb.init_oracle_client(lib_dir=r"E:\dktop\pf\oracle\instantclient_23_26") 
        connection = oracledb.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            service_name=db_service_name
        )
        print("Successfully connected to Oracle Database!")
        return connection
    except Exception as e:
        print(f"An error occurred while connecting or querying: {e}")

