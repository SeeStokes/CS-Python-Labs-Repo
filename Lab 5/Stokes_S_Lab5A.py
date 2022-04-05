####################################################################################################################################################
# Program Name: Restaurant Rating and Stars Calculator          Author: Sierra E. Stokes
# Date Created: 9/28/2021                                                   
# Created in partial fulfillment of the coursework for COSC 1336-0XX at Austin Community College
###################################################################################################################################################
# Purpose of Program: A restaurant receives numeric scores of 0-10 from five different food critics. The higher 
# the score, the better the rating. The average score translates into a 1–5 star rating. The program gets input
# of five numeric critics scores from the user. Then it calculates the average numeric score for the restaurant. 
# The program displays the average score and star rating.
####################################################################################################################################################
# Data Dictionary: 
# Name                       Type        Range         Use
# ----------------           -------     ----------    -------------------
# average_score              Float       Any float     variable to represent the average score
# critic_average_score       Float       0 - 10        variable to represent the average of scores for the restaurant
# critic_score               Float       Any float     variable to represent a score entered by the user
# critic_score_sum           Float       0 - 50        variable to represent the sum of numberic scores entered by the user
# max_valid_score_inputs     Integer     5             constant variable to represent the max number of valid scores inputted by the user
# star_rating                String      0 - 5 stars   variable to represent the star rating based on the average of scores entered by the user
# valid_score_inputs         Integer     0 - 5         variable to represent numeric scores between 0-10 inputted by the user
#####################################################################################################################################################
# Functions used:
# Name                    Inputs                  Use
# ----------------        -------------------     ---------------------------------------
# main                                            Gets the inputs from the user, calculates the average, 
#                                                 and displays their star rating   
# determine_stars         average_score           Determines the appropriate star rating based on             
#                                                 the given average score
####################################################################################################################

### MAIN code starts here ????????

# This function uses the given star rating thresholds to assign the star rating 
# of the restaurant based on the average of it's scores inputted by the user.
# Displays the average score and star rating for the user.
def determine_stars(average_score):
    star_rating = ""
    if average_score >= 9.0:
        star_rating = "*****"
    
    elif average_score < 9.0 and average_score >= 8.0:
        star_rating = "****"

    elif average_score < 8.0 and average_score >= 7.0:
        star_rating = "***"

    elif average_score < 7.0 and average_score >= 6.0:
        star_rating = "**"

    elif average_score < 6.0 and average_score >= 5.0:
        star_rating = "*"

    else:  
        star_rating = "0 stars"

    print("Your score of", format(average_score, '.2f'), "gives you", star_rating)

# This function gets five valid inputs (numeric score inputs between 0-10) from the user and calculates 
# the average of the five scores. If the user enters an invalid score (less than 0 or greater than 10), it displays
# an error message and requests a new input until it gets five valid inputs from the user. 
# The average is then passed into the determine_stars function to display the results for the user.
def main ():
    max_valid_score_inputs = 5
    critic_score_sum = 0
    valid_score_inputs = 0
    while valid_score_inputs < max_valid_score_inputs:
        critic_score = float(input("Enter critic's score between 0 and 10: "))
        if critic_score >= 0 and critic_score <= 10:
            critic_score_sum += critic_score
            valid_score_inputs += 1
        else:
            print("Error: Invalid score")
    
    critic_average_score = critic_score_sum/max_valid_score_inputs 
    determine_stars(critic_average_score)

# Main function is called to execute the program.
main()