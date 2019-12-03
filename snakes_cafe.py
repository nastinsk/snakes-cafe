print(' ************************************** \n **    Welcome to the Snakes Cafe!   ** \n **    Please see our menu below.    ** \n ** \n ** To quit at any time, type "quit" ** \n **************************************\n')

menu = {
  'Appetizers': {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0},
  'Entrees': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden': 0},
  'Desserts': {'Ice Cream': 0, 'Cake': 0, 'Pie': 0},
  'Drinks': {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
}

for el in menu:
  print(el, '\n-------')
  for item in menu[el]:
    print(item)
  print(' ')

print(' *********************************** \n ** What would you like to order? ** \n *********************************** \n')

answer = input().lower().capitalize()

while answer != 'Quit':

  for key in menu.keys():

    if answer in menu[key].keys():
      menu[key][answer]+= 1

      if menu[key][answer] == 1:
        print(f'{menu[key][answer]} order of {answer} has been added to your meal')
        break

      else:
        print(f'{menu[key][answer]} orders of {answer} have been added to your meal')
        break
  
  else:
    print('Sorry this item is unavailable, please order item from our menu')

  answer = input().lower().capitalize()



