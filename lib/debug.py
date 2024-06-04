# lib/debug.py

from employee import Employee
from department import Department

# Drop tables if they exist
Employee.drop_table()
Department.drop_table()

# Create tables
Employee.create_table()
Department.create_table()

# Create a department and save it to the database
hr = Department.create("HR", "New York")

# Create an employee and save it to the database
john = Employee.create("John Doe", "Manager", hr.id)

# Fetch the department and print its employees
fetched_hr = Department.find_by_id(hr.id)
print(fetched_hr.employees())
