
from oracle_connect import get_connection
import oracledb

def execute_non_select_query(query):
    try:
        connection=get_connection()
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except oracledb.DatabaseError as e:
        error_obj, = e.args
        print(f"Oracle Database Error: {error_obj.message}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    return True