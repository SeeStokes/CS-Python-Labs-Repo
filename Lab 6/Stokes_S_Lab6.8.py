####################################################################################################################################################
# Program Name: Random Number File Reader          Author: Sierra E. Stokes
# Date Created: 10/17/2021                                                   
# Created in partial fulfillment of the coursework for COSC 1336-0XX at Austin Community College
###################################################################################################################################################
# Purpose of Program: This program reads the random numbers from a file then displays the numbers, the sum of the numbers, the number of 
# numbers read from the file, and the average of the numbers. 
####################################################################################################################################################
# Data Dictionary: 
# Name                          Type        Range         Use
# ----------------              -------     ----------    -------------------
# line                          String      Integer       variable to represent the lines with numbers in the file
# line_count                    Integer     Any integer   variable to represent the number of random numbers in the file
# line_value                    Integer     1 - 500       variable to represent the value of the random number
# line_value_average            Float       Any float     variable to represent the average of the numbers in the file
# line_value_sum                Integer     Any integer   variable to represent the sum of the random numbers in the file        
# open_random_number_file       Object         ?          allows reading of the file 
# random_number_file_name       String         ?          variable to represent the file created  
#####################################################################################################################################################
# Functions used: None
####################################################################################################################

### MAIN code starts here ????????

# Test block for errors
try:
    # Variable representing the file
    random_number_file_name = 'random_numbers_file.txt'

    # Opens the file
    open_random_number_file = open(random_number_file_name, 'r')

    # Set sum and number of random numbers accumulators to 0
    line_value_sum = 0
    line_count = 0

    # Reads the first line in the file 
    line = open_random_number_file.readline()

    # This loop sums the numbers in the files and counts how many numbers were read from the file
    while line != '':    
        line_value = int(line.rstrip('\n'))    
        line_value_sum += line_value 
        line_count += 1
        line_value_average = float(line_value_sum/line_count)
        print (line_value)  
        line = open_random_number_file.readline()

    # Displays the number of random numbers read from the file and the sum of the numbers
    print('Number of random numbers read from the file: ', line_count)
    print('Sum of the numbers: ', line_value_sum )
    print('Average of numbers: ' , format(line_value_average, '.2f'))
    print('Program will now exit.')
    
# Error handling
except IOError:
    print('An error occurred trying to read the file', random_number_file_name)
except ValueError:
    print('ERROR: File contained an invalid value.')
except:
    print('ERROR: An error occurred.')


