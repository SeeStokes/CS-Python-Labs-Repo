###############################################################################################################################################################
# Program Name: Employee Class          Author: Sierra E. Stokes
# Date Created: 12/5/2021                                                   
# Created in partial fulfillment of the coursework for COSC 1336-0XX at Austin Community College
###############################################################################################################################################################
# Purpose of the Class: The file contains the class definition for an Employee. It consist of getter and setter methods
# for the employee's name, id, department, and position.
###############################################################################################################################################################
# Functions:
# Name                    Inputs                  Use                                                                                   
# ----------------        -------------------     -------------------------------------------------------------------------------------------------------------
# set_name                name                    Updates the employee's name
# set_id_number           id_number               Updates the employee's id number
# set_department          department              Updates the employee's department
# set_job_title           job_title               Updates the employee's job title
# get_name                                        Gets the employee's name
# get_id_number                                   Gets the employee's id number
# get_department                                  Gets the employee's department
# get_job_title                                   Gets the employee's job title
# __str__                                         Returns a string representation of the employee object that includes name, id, department, and position                                        
#                                                                                                                                                                                                                                                          
# Data Dictionary
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Name                    Type                       Range   
# ------                  ------                     --------      
# __name                  string                     any string                    Variable for the employee name.
# __id_number             string                     any string                    Variable for the employee id.
# __department            string                     any string                    Variable for the employee department.
# __job_title             string                     any string                    Variable for the employee position.
###############################################################################################################################################################

class Employee:

    # The __init__ method initializes the employee object.
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
      
    # Setter for the name
    def set_name(self, name):
        self.__name = name

    # Setter for the id number
    def set_id_number(self, id_number):
        self.__id_number = id_number

    # Setter for the department
    def set_department(self, department):
        self.__department = department

    # Setter for the job title
    def set_job_title(self, job_title):
        self.__job_title = job_title

    # Getter for the name
    def get_name(self):
        return self.__name

    # Getter for the id number
    def get_id_number(self):
        return self.__id_number

    # Getter for the department
    def get_department(self):
        return self.__department

    # Getter for the job title
    def get_job_title(self):
        return self.__job_title

    # Defines the string representation of an employee object
    def __str__(self):
        return "Name: " + self.__name + "\nID number: " + self.__id_number + "\nDepartment: " + self.__department + "\nTitle: " + self.__job_title
