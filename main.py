import sqlite3

# Connect to database
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL,
    email TEXT
)
""")
conn.commit()


# Add Employee
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        email = input("Enter Email: ")

        cursor.execute(
            "INSERT INTO employees VALUES (?, ?, ?, ?, ?)",
            (emp_id, name, department, salary, email)
        )

        conn.commit()
        print("Employee added successfully!")

    except sqlite3.IntegrityError:
        print("Employee ID already exists!")

    except ValueError:
        print("Invalid input!")


# View Employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No employees found.")
    else:
        for row in rows:
            print("-" * 30)
            print("ID         :", row[0])
            print("Name       :", row[1])
            print("Department :", row[2])
            print("Salary     :", row[3])
            print("Email      :", row[4])


# Search Employee
def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))

    cursor.execute(
        "SELECT * FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    employee = cursor.fetchone()

    if employee:
        print("-" * 30)
        print("ID         :", employee[0])
        print("Name       :", employee[1])
        print("Department :", employee[2])
        print("Salary     :", employee[3])
        print("Email      :", employee[4])
    else:
        print("Employee not found.")


# Update Employee
def update_employee():
    emp_id = int(input("Enter Employee ID: "))
    new_salary = float(input("Enter New Salary: "))

    cursor.execute(
        "UPDATE employees SET salary=? WHERE emp_id=?",
        (new_salary, emp_id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Salary updated successfully!")
    else:
        print("Employee not found.")


# Delete Employee
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    confirm = input("Are you sure? (y/n): ")

    if confirm.lower() == "y":
        cursor.execute(
            "DELETE FROM employees WHERE emp_id=?",
            (emp_id,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")
    else:
        print("Deletion cancelled.")


# Main Program
while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee()

        elif choice == 2:
            view_employees()

        elif choice == 3:
            search_employee()

        elif choice == 4:
            update_employee()

        elif choice == 5:
            delete_employee()

        elif choice == 6:
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")

# Close connection
conn.close()