import sqlite3

def initialize_db():
    """Initialize the SQLite database and create table if it doesn't exist."""
    connection = sqlite3.connect('employee.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            eid INTEGER PRIMARY KEY,
            ename TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def add_employee(eid, ename):
    """Add employee details to the database."""
    connection = sqlite3.connect('employee.db')
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO employees (eid, ename) VALUES (?, ?)', (eid, ename))
        connection.commit()
        print("Employee added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Employee ID already exists.")
    connection.close()

def search_employee(eid):
    """Search for an employee by ID."""
    connection = sqlite3.connect('employee.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM employees WHERE eid = ?', (eid,))
    result = cursor.fetchone()
    if result:
        print(f"Employee found: ID = {result[0]}, Name = {result[1]}")
    else:
        print("Employee not found.")
    connection.close()

def delete_employee(eid):
    """Delete a specified employee record."""
    connection = sqlite3.connect('employee.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM employees WHERE eid = ?', (eid,))
    if cursor.rowcount > 0:
        print("Employee deleted successfully.")
    else:
        print("Employee ID not found.")
    connection.commit()
    connection.close()

def find_duplicates():
    """Find and print duplicate employee names."""
    connection = sqlite3.connect('employee.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT ename, COUNT(*) as count 
        FROM employees 
        GROUP BY ename 
        HAVING COUNT(*) > 1
    ''')
    duplicates = cursor.fetchall()
    if duplicates:
        print("Duplicate employee names found:")
        for record in duplicates:
            print(f"Name = {record[0]}, Count = {record[1]}")
    else:
        print("No duplicate employee names found.")
    connection.close()

def menu():
    """Display menu options to the user."""
    while True:
        print("\nEmployee Database Menu:")
        print("1. Add Employee")
        print("2. Search Employee by ID")
        print("3. Delete Employee by ID")
        print("4. Find Duplicate Records")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            eid = int(input("Enter Employee ID: "))
            ename = input("Enter Employee Name: ")
            add_employee(eid, ename)
        elif choice == '2':
            eid = int(input("Enter Employee ID to search: "))
            search_employee(eid)
        elif choice == '3':
            eid = int(input("Enter Employee ID to delete: "))
            delete_employee(eid)
        elif choice == '4':
            find_duplicates()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    initialize_db()
    menu()
