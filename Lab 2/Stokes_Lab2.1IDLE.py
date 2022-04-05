#Input
user_input = input('\nHow many servings would you like to make?: ')
number_of_servings = int(user_input)

#Process
Servings=1
Tomato_Sauce = 0.5
Tomato_Paste = .08
Garlic = 0.5
Oregano = 0.25

cups_TomatoSauce  = (Tomato_Sauce * number_of_servings)
tablespoons_TomatoPaste  = (Tomato_Paste * number_of_servings)
cloves_Garlic = (Garlic * number_of_servings)
tablespoons_Oregano  = (Oregano * number_of_servings)

#Output
print('\nNumber of servings =', number_of_servings, end='\n\n')
print('Recipe will be as follows:')
print('Tomato sauce =', format(cups_TomatoSauce,',.2f'),('cups'))
print('Tomato paste =', format(tablespoons_TomatoPaste, ',.2f'), ('tablespoons'))
print('Garlic =', format(cloves_Garlic, ',.2f'), ('cloves'))
print('Oregano =', format(tablespoons_Oregano, ',.2f'), ('tablespoons'),end='\n\n')




