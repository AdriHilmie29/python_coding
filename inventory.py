# A local bakery is developing an inventory system. The system will ask the user to input the quantity and price for each item. 
# The items are butter, eggs, flour, sugar and chocolates.
# The program will read and calculate the total value of the items in the inventory. 
# Coding by Bellamy



butter_price = input('Enter price of butter : RM')
butter_quantity = input('Enter quantity of butter:')
butter_price = int(butter_price)
butter_quantity = int(butter_quantity)
print(' ')

eggs_price = input('Enter price of eggs: RM')
eggs_quantity = input('Enter quantity of eggs:')
eggs_price = int(eggs_price)
eggs_quantity = int(eggs_quantity)
print(' ')

flour_price = input('Enter price of flour: RM')
flour_quantity = input('Enter quantity of flour:')
flour_price = int(flour_price)
flour_quantity = int(flour_quantity)
print(' ')

sugar_price = input('Enter price of sugar: RM')
sugar_quantity = input('Enter quantity of sugar:')
sugar_price = int(sugar_price)
sugar_quantity = int(sugar_quantity)
print(' ')

chocolate_price = input('Enter price of chocolate: RM')
chocolate_quantity = input('Enter quantity of chocolate:')
chocolate_price = int(chocolate_price)
chocolate_quantity = int(chocolate_quantity)
print(' ')

inventory_cost = butter_price*butter_quantity + eggs_price*eggs_quantity + flour_price*flour_quantity + sugar_price*sugar_quantity + chocolate_price*chocolate_quantity
print('Total value of inventory: RM', inventory_cost)
print(' ')

input('Press ENTER to exit')
