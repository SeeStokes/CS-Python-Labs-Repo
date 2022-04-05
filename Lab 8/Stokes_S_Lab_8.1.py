# Lab 8.1
# The program reads the file’s contents and determines the following:
# The number of uppercase letters in the file
# The number of lowercase letters in the file
# The number of digits in the file
# The number of whitespace characters in the file
######################################################################################################################################################
# Data Dictionary
# Name                                Purpose
#---------                            ----------- 
# count_digit                         integer to represent the number of digits in the file
# count_lowercase                     integer to represent the number of lowercase characters in the file
# count_space                         integer to represent the number of whitespaces in the file
# count_uppercase                     integer to represent the number of uppercase characters in the file
# current_char                        variable to represent the current character in the string
# text_file_contents                  object that allows reading of the file
# text_file_name                      variable representing the file text.txt
# ################################################################################################################################################### 

# Variable representing the file
text_file_name = 'text.txt'

# Opens the file
text_file = open(text_file_name, 'r')

# Reads the file and stores the contents
text_file_contents = text_file.read()

# Initialize counting variables
count_uppercase = 0
count_lowercase = 0
count_digit = 0
count_space = 0

# Iterates over string to count number of uppercase letters, lowercase letters, digits, and whitespaces 
for current_char in text_file_contents:
    if current_char.isupper():
        count_uppercase += 1
    if current_char.islower():
        count_lowercase += 1
    if current_char.isdigit():
        count_digit += 1   
    if current_char.isspace():
        count_space += 1 
    
# Display the counts
print ("Uppercase Letters: " , count_uppercase)
print ("Lowercase Letters: " , count_lowercase)
print ("Digits: " , count_digit)
print ("Whitespaces: " , count_space)