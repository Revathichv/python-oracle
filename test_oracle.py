# main.py
from oracle_connect import get_connection
# Replace with the actual filenames where you saved functions 1 & 2
from execute_oracle_query import execute_non_select_query 
from execute_select_query import execute_sel_query, Emp

def main():
    print("=== Step 1: Testing Connection Directly ===")
    conn = get_connection()
    if conn:
        print("Connection check passed.")
        conn.close()  # Manually close our test check connection
    else:
        print("Connection check failed! Please check your credentials.\n")
        return

    print("\n=== Step 2: Testing Non-Select Query (Table Setup & Insert) ===")
    # 1. Create a dummy test table
    create_table_sql = """
    CREATE TABLE emp_test_table_1 (
        id NUMBER,
        name VARCHAR2(50),
        sal NUMBER
    )
    """
    print("Creating test table...")
    execute_non_select_query(create_table_sql)

    # 2. Insert test data
    insert_sql = "INSERT INTO emp_test_table_1 (id, name, sal) VALUES (101, 'Alice Smith', 75000)"
    print("Inserting record...")
    if execute_non_select_query(insert_sql):
        print("Data inserted successfully.")
    else:
        print("Failed to insert data.")

    print("\n=== Step 3: Testing Select Query ===")
    select_sql = "SELECT id, name, sal FROM emp_test_table_1"
    print("Fetching employees...")
    employees = execute_sel_query(select_sql)

    print(f"\nResults Retrieved: {len(employees)}")
    for emp in employees:
        print(f"• ID: {emp.id} | Name: {emp.name} | Salary: ${emp.sal:,.2f}")




if __name__ == "__main__":
    main()
