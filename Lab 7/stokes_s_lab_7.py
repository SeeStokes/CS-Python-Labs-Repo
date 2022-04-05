###############################################################################################################################################################
# Program Name: Larger Than n Program          Author: Sierra E. Stokes
# Date Created: 11/7/2021                                                   
# Created in partial fulfillment of the coursework for COSC 1336-0XX at Austin Community College
#######################################################################################################################################################################################################################################################################
# Purpose of the Program: The program accepts input of 10 integers from the user and an integer, n, that will be the search number.
# The program compares all numbers in the list of numbers from the user to n. 
# Finally, the program displays: The original list, n, and a list of numbers greater than n.
#######################################################################################################################################################################################################################################################################
# Functions used:
# Name                    Inputs                  Use                                                                                   Data Dictionary
# ----------------        -------------------     ---------------------------------------                                               --------------------------------------------------------------------------------------------------------------------------------
#                                                                                                                                       Name                    Type                       Range                                  Use
#                                                                                                                                       ------                  ------                     --------                               --------                                                                                                   
# main                                            Accepts input 10 integers from the user and an integer n that will be                 integer_list            list                       any integer                            holds the user inputted list of ten integers
#                                                 the search number. Main calls the function display_larger and passes                  user_integer            integer                    any integer                            variable that represents user inputted integers
#                                                 2 arguments: the 10 integers stored in a list, and the number n.                                             
# 
#                                       
# 
# 
# 
# 
# 
# 
#           
# display_larger         integer_list, n          Compares all numbers in the list of numbers from the user to n then displays          integer_item           integer                     any integer in integer_list            variable that represents the integers in integer_list 
#                                                 the original user inputted numbers, n, and the list of numbers greater than n.        larger_integers        list                        any integer in integer_list            holds the integers greater than n 
#                                                                                                                                                                                          greater than n                         
#                                                                                                                                       n                      integer                     any integer                            variable that represents user inputted integer that is the search number                                            
#
#
#
#
#
#
#

#####################################################################################################################################################################################################################################################################

### MAIN code starts here ????????

def main ():
    # create the original list where the 10 user inputted numbers will be stored
    integer_list = []
    print("Enter a list of ten integers.")
    for user_integer in range(10):
        user_integer = int(input("Enter a number: "))
        integer_list.append(user_integer)
    # ask for the search number, n
    n = int(input("Enter the number you wish to test if the list elements are greater than: ")) 
    # call the function, display_larger, passing the 10 integers stored in the original list, and the number, n, through
    display_larger(integer_list, n)


def display_larger (integer_list,n):
    # create the list where integers larger than n will be stored
    larger_integers=[]
    # compare the numbers in the original list to n
    for integer_item in integer_list:
        if integer_item > n:
            larger_integers.append(integer_item)
    # display the original user inputted numbers, n, and the list of numbers greater than n
    print ("Number: ", n)
    print ("List of numbers: ")
    print (integer_list)
    print ("List of numbers that are larger than" ,n, ":")
    print (larger_integers)

# Call the main function         
main()

