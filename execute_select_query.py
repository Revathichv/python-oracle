from oracle_connect import get_connection
import oracledb
from dataclasses import dataclass

@dataclass
class Emp:
    id: int
    name: str
    sal: float

def execute_sel_query(query):
    emp_list = []
    try:
        connection=get_connection()
        with connection.cursor() as cursor:
            cursor.execute(query)
            for row in cursor:
                    # row[0] is id, row[1] is name, row[2] is sal
                    employee = Emp(id=row[0], name=row[1], sal=row[2])
                    emp_list.append(employee)
    except oracledb.DatabaseError as e:
        error_obj, = e.args
        print(f"Oracle Database Error: {error_obj.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return emp_list