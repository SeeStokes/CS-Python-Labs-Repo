#======================================================================================================================================================================================|
#  Program Name: Budgeted vs. Actual Expenses                     Author(s): Sierra Stokes                                                                                             |
#  Date Created: 9/20/2021                      Program Location: Desktop                                                                                                              |
#  Created in partial fulfillment of the coursework for COSC 1336-014 at                                                                                                               |
#    Austin Community College                                                                                                                                                          |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
#  Copyright (c) 2021 By Sierra E. Stokes                                                                                                                                              |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
#  Purpose of Program: asks the user to enter the amount that he or she has budgeted for a month and to enter each of his or her expenses for the month. The program keeps             | 
#                      a running total and then displays the amount that the user is over or under their budget.                                                                       |
#======================================================================================================================================================================================|
# Data Dictionary                                                                                                                                                                      |
#  Name                             Type                    Range                       Use                                                                                            |
#  ------                           -----                   ----------                  -----------------------------------------                                                      |
# monthly_expense_item_amount       float                   any float value             variable to represent users line item expenses                                                 | 
# over_budget_amount                float                   any float value             variable to represent the amount by which the user was over budget on their expenses           |
# over_under_budget_amount          float                   any float value             variable to represent the the users budget minus the value of their expenses                   |  
# running_total_expense_spent       float                   any float value             constant to represent the cumulative total of the users line item expenses                     | 
# total_monthly_budget_amount       float                   any float value             variable to represent the amount the user budgeted for the month                               | 
#======================================================================================================================================================================================|
#  Functions used: None                                                                                                                                                                |
#======================================================================================================================================================================================|

#MAIN Code Begins Here ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????|

# set cumulative total expenses to zero
running_total_expense_spent = 0

# get the users budget and expenses for the current month
total_monthly_budget_amount = float(input('Enter amount budgeted for the month: '))
monthly_expense_item_amount = float(input('Enter an amount spent (0 to quit): '))

# Calculate a series of expenses from a user to calculate the cumulative total
while monthly_expense_item_amount != 0:
    running_total_expense_spent += monthly_expense_item_amount
    monthly_expense_item_amount = float(input('Enter an amount spent (0 to quit): '))

# Calculate whether users cumulative expenses went over or under budget
# Print the appropriate print statement for the user that displays their budget, 
# their cumulative total expenses, and how by how much they went over/under on their budget
over_under_budget_amount = total_monthly_budget_amount - running_total_expense_spent
print('Budgeted: $', format(total_monthly_budget_amount, '.2f'))
print('Spent: $', format(running_total_expense_spent, '.2f'))

if over_under_budget_amount == 0:
    print('You spent your budgeted amount.')

elif over_under_budget_amount > 0:
    print('You are $' , format(over_under_budget_amount, '.2f') , 'under budget. Great job!')

elif over_under_budget_amount < 0:
    over_budget_amount = over_under_budget_amount * -1
    print('You are $', format(over_budget_amount, '.2f'), 'over budget. Plan better next time.')
