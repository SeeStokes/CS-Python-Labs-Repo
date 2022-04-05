# ==========================================================================================================================================================================================================================
# Program Name: How Much Spaghetti Sauce?                      Author: Sierra Stokes                                                                                                                                        |
# Date Created: September 2, 2021                                                                                                                                                                                           |
# Created in partil fulfillment of the coursework for COSC 1336-014 at Austin Community College                                                                                                                             |
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Copyright (c) 2021 by Sierra Stokes                                                                                                                                                                                       |
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Purpose of Program: The program asks the user to enter how many servings they want to make.                                                                                                                               |
# Then the program will calculate the amount of each ingredient needed for the                                                                                                                                              |
# number of servings the user has specified. Finally, the program will display the amounts for the user.                                                                                                                    |
# Program status: Complete                                                                                                                                                                                                  |
# ===========================================================================================================================================================================================================================
# Data Dictionary                                                                                                                                                                                                           |
#   Name                                    Type               Range                            Use                                                                                                                         |
#   -----                                   -------            ---------------                  ------------------------                                                                                                    |
#   number_of_servings                      float               maximum 1.8 x 10^308            number of serving specified by the user                                                                                     |
#   rounded_number_of_servings              string              any sequence of characters      number of servings specified by the user rounded to the nearest hundredth                                                   |
#   recipe_servings                         integer             4.00                            number of servings in the original spaghetti sauce recipe provided by Dr. Al                                                |
#   cups_tomato_sauce_per_serving           float               .50                             cups of tomato sauce in one serving of the original spaghetti sauce recipe                                                  |             
#   cups_tomato_paste_per_serving           float               .08                             cups of tomato paste  in one serving of the original spaghetti sauce recipe                                                 |
#   cloves_garlic_per_serving               float               .50                             cloves garlic in one serving of the original spaghetti sauce recipe                                                         |
#   tablespoons_oregano_per_serving         float               .25                             tablespoons of oregano in one serving of the original spaghetti sauce recipe                                                |
#   cups_tomato_sauce                       float               maximum 1.8 x 10^308            amount of tomato sauce needed for the user to make the number of servings they specified                                    |
#   cloves_garlic                           float               maximum 1.8 x 10^308            amount of garlic cloves needed for the user to make the number of servings they specified                                   |
#   tablespoons_oregano                     float               maximum 1.8 x 10^308            tablespoons of oregano needed for the user to make the number of servings they specified                                    |
#   rounded_cups_tomato_sauce               string              any sequence of characters      amount of tomato sauce needed for the user to make the number of servings they specified rounded to the nearest hundredth   |
#   rounded_cups_tomato_paste               string              any sequence of characters      amount of tomato paste needed for the user to make the number of servings they specified rounded to the nearest hundredth   |
#   rounded_cloves_garlic                   string              any sequence of characters      amount of garlic cloves needed for the user to make the number of servings they specified rounded to the nearest hundredth  |
#   rounded_tablespoons_oregano             string              any sequence of characters      tablespoons of oregano needed for the user to make the number of servings they specified rounded to the nearest hundredth   |
#                                                                                                                                                                                                                           |
# ===========================================================================================================================================================================================================================
#   Functions used:                                                                                                                                                                                                         |
#    Name                        Inputs                        Use                                                                                                                                                          |
#   ----------------             ---------------               ----------                                                                                                                                                   |
#   input                        keyboard                      user enters number of servings of spaghetti sauce they want to make to be run by the program                                                                 |
#   format                       any string value              rounds decimal values to the nearest hundredth                                                                                                               |
#   print                        any string value              displays results for the user                                                                                                                                |
#                                                                                                                                                                                                                           |
# ===========================================================================================================================================================================================================================

#MAIN Code Begins Here ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
#---------
# Input 
# User will input the number of servings they are requesting 
number_of_servings = float(input('Enter the number of servings of spaghetti sauce you want to make: '))
rounded_number_of_servings = format(number_of_servings, '.2f')

# Process
# Calculate the amount of each ingredient for a single serving
recipe_servings = 4
cups_tomato_sauce_per_serving = 2/recipe_servings
cups_tomato_paste_per_serving = 1/(3*recipe_servings)
cloves_garlic_per_serving = 2/recipe_servings
tablespoons_oregano_per_serving = 1/recipe_servings

# Calculate the amount of each ingredient needed for the user's requested number of servings
cups_tomato_sauce  = (cups_tomato_sauce_per_serving * number_of_servings)
cups_tomato_paste  = (cups_tomato_paste_per_serving * number_of_servings)
cloves_garlic = (cloves_garlic_per_serving * number_of_servings)
tablespoons_oregano  = (tablespoons_oregano_per_serving * number_of_servings)

# Format the amounts of each ingredient for the user's recipe to a string rounded to the nearest hundredth 
rounded_cups_tomato_sauce = format(cups_tomato_sauce, '.2f')
rounded_cups_tomato_paste = format(cups_tomato_paste, '.2f')
rounded_cloves_garlic = format (cloves_garlic, '.2f')
rounded_tablespoons_oregano = format(tablespoons_oregano, '.2f')

# Output the amounts of each ingredient for the user's recipe rounded to the nearest hundredth 
print('To make ' + rounded_number_of_servings + ' servings of spaghetti sauce, you will need:')
print(rounded_cups_tomato_sauce + ' cups of tomato sauce')
print(rounded_cups_tomato_paste + ' cups of tomato paste')
print(rounded_cloves_garlic + ' cloves of garlic')
print(rounded_tablespoons_oregano + ' tablespoons of oregano')