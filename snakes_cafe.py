#====================SNAKES CAFE============================

# initial signboard
print('\n \n ************************************** \n **    Welcome to the Snakes Cafe!   ** \n **    Please see our menu below.    ** \n ** \n ** To quit at any time, type "quit" ** \n **************************************\n')

# all menu items stored in nested dictionary
menu = {
  'Appetizers': {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0},
  'Entrees': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden': 0},
  'Desserts': {'Ice Cream': 0, 'Cake': 0, 'Pie': 0},
  'Drinks': {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
}

#print all menu items according to template
for el in menu:
  print(el, '\n-------')
  for item in menu[el]:
    print(item)
  print(' ')

print(' *********************************** \n ** What would you like to order? ** \n *********************************** \n')

# initial input
answer = input().lower().capitalize()

# if user didn't run 'quit" command stay in this loop
while answer != 'Quit':

  # check if we have the input item in our menu
  for key in menu.keys():

    if answer in menu[key].keys():

      #if item exists increment its value
      menu[key][answer]+= 1

      #logic for output for a single or multiple orders
      if menu[key][answer] == 1:
        print(f'** {menu[key][answer]} order of {answer} has been added to your meal **')
        break

      else:
        print(f'** {menu[key][answer]} orders of {answer} have been added to your meal **')
        break
  
  # print this output if item not exists in our menu 
  else:
    print('** Sorry this item is unavailable, please order item from our menu **')

  # ask user again
  answer = input().lower().capitalize()



