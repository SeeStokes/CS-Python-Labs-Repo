import Stokes_S_Lab_10_employee

def main():
    employees = []

    for count in range(3):
        name = input("Enter employee name: ")
        id = input("Enter employee ID: ")
        department = input("Enter department: ")
        position = input ("Enter position: ")
        employee = Stokes_S_Lab_10_employee.Employee(name, id, department, position)
        employees.append(employee)
        print()

    employee_number = 1
    for employee in employees:
        print("Employee " + str(employee_number) + ":")
        print(employee, "\n")
        employee_number += 1

main()