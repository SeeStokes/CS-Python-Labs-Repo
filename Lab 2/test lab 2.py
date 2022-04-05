#1. Input
user_input = input('\nEnter the number of servings of spaghetti sauce you want to make: ')
number_of_servings = int(user_input)

#2. Process
servings=4
cups_tomato_sauce_per_serving = 2/servings
cups_tomato_paste_per_serving = 1/(3*servings)
cloves_garlic_per_serving = 2/servings
tablespoons_oregano_per_serving = 1/servings

cups_tomato_sauce  = (cups_tomato_sauce_per_serving * number_of_servings)
rounded_cups_tomato_sauce = format(cups_tomato_sauce, '.2f')

cups_tomato_paste  = (cups_tomato_paste_per_serving * number_of_servings)
cloves_garlic = (cloves_garlic_per_serving * number_of_servings)
tablespoons_oregano  = (tablespoons_oregano_per_serving * number_of_servings)


#3. Output
print('To make ' + format(number_of_servings, '.2f') + ' servings of spaghetti sauce, you will need:')

print(rounded_cups_tomato_sauce + 'cups of tomato sauce')
print(f'{cups_tomato_paste} cups of tomato paste')
print(f'{cloves_garlic} cloves of garlic')
print(f'{tablespoons_oregano} tablespoons of oregano')








