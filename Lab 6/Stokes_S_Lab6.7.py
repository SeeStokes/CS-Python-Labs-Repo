####################################################################################################################################################
# Program Name: Random Number File Writer          Author: Sierra E. Stokes
# Date Created: 10/17/2021                                                   
# Created in partial fulfillment of the coursework for COSC 1336-0XX at Austin Community College
###################################################################################################################################################
# Purpose of Program: This program writes a series of random numbers in the range of 1 to 500 to a file. The program lets 
# the user specify how many random numbers the file will hold.
####################################################################################################################################################
# Data Dictionary: 
# Name                          Type        Range         Use
# ----------------              -------     ----------    -------------------
# outfile                       Object         ?          allows writing to the file
# random_number                 Integer     1 - 500       variable to represent random number
# random_number_file_name       String         ?          variable to represent the file name 
# requested_numbers_random      Integer     Any int       variable to represent how many random numbers the user wants the file to hold
# requested_random_number_file  Integer     Any int       variable to represent requested number of random numbers in the range   
#####################################################################################################################################################
# Functions used: None
####################################################################################################################

### MAIN code starts here ????????
import random

# Test block for errors
try:
    # User enters number of random numbers they want in the file
    # Creates a file with the numbers 
    requested_numbers_random = int(input("How many random numbers will the file hold: "))
    random_number_file_name = 'random_numbers_file.txt'

    outfile = open(random_number_file_name, 'w')
    
    # For loop generates the number of random numbers that the user requested and writes it to the file
    for requested_random_number_file in range(0, requested_numbers_random):
        random_number = random.randrange(1, 500) 
        outfile.write(str(random_number) + '\n') 
    
    # Closes the file and displays end message for the user
    outfile.close()
    print('Successfully created file', random_number_file_name, '\nProgram will now exit.')

# Error handling    
except IOError:
    print('An error occurred trying to write the file', random_number_file_name)
except ValueError:
    print('ERROR: Please enter an integer value.')
except:
    print('ERROR: An error occurred.')


