###############################################################################################################################################################
# Program Name: Employee Class Program          Author: Sierra E. Stokes
# Date Created: 12/5/2021                                                   
# Created in partial fulfillment of the coursework for COSC 1336-0XX at Austin Community College
###############################################################################################################################################################
# Purpose of the Program: The program accepts input of  3 employees' name, id, department, and position from the user.
# It then uses those inputs to create an employee object for each employee entered by the user and prints out that object.
###############################################################################################################################################################
# Functions used:
# Name                    Inputs                  Use                                                                                   
# ----------------        -------------------     -------------------------------------------------------------------------------------------------------------                                                                                                                         
# main                                            Gets employee name, id, department, and position values from the user                 
#                                                 for 3 empoyees and then creates employee objects from those values.                   
#                                                 Finally, it prints out the 3 employee objects.                                        
#                                                                                                                                       
#                                                                                                                                       
#                                                                                                                                       
# Data Dictionary
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Name                    Type                       Range   
# ------                  ------                     --------      
# employees               list of employee objects   3 employee objects            Holds the employee objects generated from the user entered values.    
# name                    string                     any string                    Variable for the user entered employee name. Used as an argument to create a new employee object. 
# id                      string                     any string                    Variable for the user entered employee id. Used as an argument to create a new employee object.
# department              string                     any string                    Variable for the user entered employee department. Used as an argument to create a new employee object.
# position                string                     any string                    Variable for the user entered employee position. Used as an argument to create a new employee object.
# employee                employee object            any employee object           Variable for the employee object created from the user entered values above.                                   
###############################################################################################################################################################

import Stokes_S_Lab_10_employee

def main():
    # Create a list that will hold the employee objects
    employees = []

    # For loop that creates 3 employee objects from user entered values
    for i in range(3):
        # Get the user to enter employee name, id, department, and position
        name = input("Enter employee name: ")
        id = input("Enter employee ID: ")
        department = input("Enter department: ")
        position = input ("Enter position: ")

        # Use the user entered values to create a new employee object
        employee = Stokes_S_Lab_10_employee.Employee(name, id, department, position)

        # Add the new employee object to the list
        employees.append(employee)

        # Print a new line to separate this employee from the next
        print()

    # Print out the 3 employee objects
    print("Employee 1:")
    print(employees[0], "\n")

    print("Employee 2:")
    print(employees[1], "\n")

    print("Employee 3:")
    print(employees[2], "\n")

main()