package_price= 149
packages_purchased = int(input('Enter the number of servings of software packages purchased: '))
if packages_purchased < 10:
    print ('No discount applied.')
    print ("Total Amount" , package_price)