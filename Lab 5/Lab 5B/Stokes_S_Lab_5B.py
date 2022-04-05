###############################################################################################################################################################
# Program Name: Falling Objects Program          Author: Sierra E. Stokes
# Date Created: 10/10/2021                                                   
# Created in partial fulfillment of the coursework for COSC 1336-0XX at Austin Community College
###############################################################################################################################################################
# Purpose of Program: This progam calculates the distance in meters(m) based on the object’s falling distance and displays the results for the user.
###############################################################################################################################################################
# Data Dictionary: 
# Name                       Type        Range         Use
# ----------------           -------     ----------    -------------------
# distance_meters            Float       4.90-490.00   variable to represent the distance(m) the object travels in 1-10 seconds
###############################################################################################################################################################
# Functions used:
# Name                    Inputs                  Use
# ----------------        -------------------     ---------------------------------------
# main                                            displays the distance(m) an object falls in meters for 1-10 seconds
# falling_distance         time                   calculates and returns the distance(m) the object falls in a specific time period             
###############################################################################################################################################################

### MAIN code starts here ????????

# Imports the distance module with the falling_distance function
import distance

# This function displays the distance(m) an object falls for 1-10 seconds
def main ():  
    print ('Time(s)\t\tFalling Distance(m)')    
    print ('--------------------------------------------------------')
    for time in range(1, 11):
        distance_meters = distance.falling_distance(time)
        print(time, '\t\t', format (distance_meters, '.2f'))
        
# Main function is called to execute the program.        
main()