# Lab 8.2
# The program reads a string from the user containing a date in the form mm/dd/yyyy then prints 
# the date in the format: Month D, YY.
#######################################################################################################################################
# Data Dictionary
# Name                              Purpose
# ---------                         --------------
# day                               integer variable to represent the day 
# month                             string variable to represent the month in 1-12 format
# month_name                        string variable to represent the name of the month 
# split_date                        list of strings variable to represent the date split into month, date, and year segments
# user_date                         string variable to represent the date the user inputs 
# year                              string variable to represent the year 
########################################################################################################################################## 
# month_converstion function
# This function converts the month number (01-12) to the corresponding month name
# Data Dictionary
# Name                              Purpose
# ---------                         --------------
# month_number                      string variable to represent the month in 1-12 format
############################################################################################################################################
def month_conversion (month_number):
    if month_number == '01':
        return 'January'
    if month_number == '02':
        return 'February'
    if month_number == '03':
        return 'March'
    if month_number == '04':
        return 'April'
    if month_number == '05':
        return 'May'
    if month_number == '06':
        return 'June'
    if month_number == '07':
        return 'July'
    if month_number == '08':
        return 'August'
    if month_number == '09':
        return 'September'
    if month_number == '10':
        return 'October'
    if month_number == '11':
        return 'November'
    if month_number == '12':
        return 'December'

# Ask the user to enter a date in the format mm/dd/yyyy    
user_date = input("Enter a date in the format mm/dd/yyyy: ")

# Split the string at / and get the individual segments
split_date = user_date.split('/')
month = split_date[0]
day = int(split_date[1])
year = split_date[2]

# Call the month_conversion function 
month_name = month_conversion(month)

# Display the date in the format Month name-Day-Year 
print(month_name + ' ' + str(day) + ',' + ' ' + year)