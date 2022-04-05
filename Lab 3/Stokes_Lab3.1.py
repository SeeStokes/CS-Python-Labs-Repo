#========================================================================================================================================================================================================
#  Program Name: Volume Discounts                      Author(s): Sierra Stokes                                                                                                                         |
#  Date Created: 9/15/2021                     Program Location: Desktop                                                                                                                                |
#  Created in partial fulfillment of the coursework for COSC 1336-014 at                                                                                                                                |
#    Austin Community College                                                                                                                                                                           |
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|                                                                                                                            
#  Copyright (c) 2021 By Sierra Stokes                                                                                                                                                                  |
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|                                                                                                                            
#  Purpose of Program:  This program asks the user to enter the number of software packages purchased.                                                                                                  |  
#                       The program then displays the dollar amount of the discount (if any) and the total amount                                                                                       | 
#                       of the purchase after discount.                                                                                                                                                 |
#=======================================================================================================================================================================================================|                                                                                                                           
# Data Dictionary                                                                                                                                                                                       |
#  Name                                     Type           Range          Use                                                                                                                           |
#  ---------------                          -----          ----------     -----------------------------------------                                                                                     |
#  discount_A                               integer        10             Constant to represent the discount threshold for 0-9 packages purchased                                                       |                                                    
#  discount_A_percentage                    float          .1             Constant to represent a 10% discount rate                                                                                     |
#  discount_B                               integer        50             Constant to represent the discount threshold for 10-49 packages purchased                                                     |
#  discount_B_percentage                    float          .2             Constant to represent a 20% discount rate                                                                                     |
#  discount_C                               integer        100            Constant to represent the discount threshold for 50-149 packages purchased                                                    |           
#  discount_C_percentage                    float          .3             Constant to represent a 30% discount rate                                                                                     |
#  discount_D                               integer        150            Constant to represent the discount threshold for 150 or more packages purchased                                               |
#  discount_D_percentage                    float          .4             Constant to represent a 40% discount rate                                                                                     |
#  no_discount                              integer         0             Constant to represent no discount given for less than 10 packages purchased                                                   |
#  no_discount_amount                       integer         0             Constant to represnet the a $0.00 discount applied to total purchase price                                                    |
#  no_discount_percentage                   integer         0             Constant to represent a 0%  discount rate                                                                                     |
#  number_of_packages                       integer        any int        Number of software packages specified by the user                                                                             |
#  package_price                            integer         149           Constant to represent the price per software package                                                                          |
#  rounded_no_discount_amount               string         any string     Price of software package purchase with no discount applied rounded to the nearest hundredth                                  |
#  rounded_total_amount                     string         any string     Total price of softare package purchase with the conditional discount applied rounded to the nearest hundredth                |
#  rounded_total_discount_amount            string         any string     Amount of money the discount will reduce the total price of the software package purchase rounded to the nearest hundredth    |
#  rounded_total_no_discount_amount         string         any string     Price of purchase with no discount applied rounded to the nearest hundredth                                                   |
#  total_amount                             float          any decimal    Total price of softare package purchase with the conditional discount applied                                                 |
#  total_discount_amount                    float          any decimal    Amount of money the discount will reduce the total price of the software package purchase                                     |
#  total_no_discount_amount                 integer        0              Price of purchase with no discount applied                                                                                    |
#=======================================================================================================================================================================================================|
#  Functions used: None                                                                                                                                                                                 |                                                                                                                                                                                |
#                                                                                                                                                                                                       |
#                                                                                                                                                                                                       |
#                                                                                                                                                                                                       |
#=======================================================================================================================================================================================================|

#MAIN Code Begins Here ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

# This program asks the user to enter the number of software packages purchased.                                                                                         
# The program then calculates and displays the dollar amount of the discount (if any) and the total amount of the purchase after discount.

# Named constants to represent the discount thresholds
no_discount = 0
discount_A = 10
discount_B = 50
discount_C = 100
discount_D = 150
no_discount_percentage = 0
discount_A_percentage = .1
discount_B_percentage = .2
discount_C_percentage = .3
discount_D_percentage = .4
package_price = 149


# Input 
# User will input the number of software packages purchased 
number_of_packages = int(input('Enter the number of servings of software packages purchased: '))

# Determine the discount amount
# Calculate total price with discount
# Display total dollar amount of the discount applied for the user
# Display the total dollar amount of the software package purchase with discount applied for the user
if number_of_packages < discount_A: 
    total_no_discount_amount = (number_of_packages * package_price) * no_discount_percentage
    total_amount = (number_of_packages * package_price) - total_no_discount_amount
    rounded_total_no_discount_amount = format(total_no_discount_amount, ',.2f')
    rounded_total_amount = format(total_amount, ',.2f')
    print('Discount Amount: $' + rounded_total_no_discount_amount)
    print ('Total Amount: $' + rounded_total_amount)
# If customer purchases less than 10 packages, then they get a 0% discount applied (no discount)

elif number_of_packages >= discount_A and number_of_packages < discount_B:
    total_discount_amount = (number_of_packages * package_price) * discount_A_percentage
    total_amount = (number_of_packages * package_price) - total_discount_amount
    rounded_total_discount_amount = format(total_discount_amount, ',.2f')
    rounded_total_amount = format(total_amount, ',.2f')
    print('Discount Amount: $' + rounded_total_discount_amount)
    print ('Total Amount: $' + rounded_total_amount)
# If customer purchases between 10-49 packages, then they get a 10% discount applied

elif number_of_packages >= discount_B and number_of_packages < discount_C:
    total_discount_amount = (number_of_packages * package_price) * discount_B_percentage
    total_amount = (number_of_packages * package_price) - total_discount_amount
    rounded_total_discount_amount = format(total_discount_amount, ',.2f')
    rounded_total_amount = format(total_amount, ',.2f')
    print('Discount Amount: $' + rounded_total_discount_amount)
    print ('Total Amount: $' + rounded_total_amount)
# If customer purchases between 50-99 packages, then they get a 20% discount applied

elif number_of_packages >= discount_C and number_of_packages < discount_D:
    total_discount_amount = (number_of_packages * package_price) * discount_C_percentage
    total_amount = (number_of_packages * package_price) - total_discount_amount
    rounded_total_discount_amount = format(total_discount_amount, ',.2f')
    rounded_total_amount = format(total_amount, ',.2f')
    print('Discount Amount: $' + rounded_total_discount_amount)
    print ('Total Amount: $' + rounded_total_amount)
# If customer purchases between 100-149 packages, then they get a 30% discount applied

elif number_of_packages >= discount_D:
    total_discount_amount = (number_of_packages * package_price) * discount_D_percentage
    total_amount = (number_of_packages * package_price) - total_discount_amount
    rounded_total_discount_amount = format(total_discount_amount, ',.2f')
    rounded_total_amount = format(total_amount, ',.2f')
    print('Discount Amount: $' + rounded_total_discount_amount)
    print ('Total Amount: $' + rounded_total_amount)
# If customer purchases more than 150 packages, then they get a 40% discount applied


