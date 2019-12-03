print(' ************************************** \n **    Welcome to the Snakes Cafe!   ** \n **    Please see our menu below.    ** \n ** \n ** To quit at any time, type "quit" ** \n **************************************\n')

menu = {
  'Appetizers': {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0},
  'Entrees': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden':0}
}

for el in menu:
  print(el, '\n-------')
  for item in menu[el]:
    print(item)
  print(' ')

print(' *********************************** \n ** What would you like to order? ** \n *********************************** ')

answer = input()
while answer != 'quit':
  for key in menu.keys():
    if answer in menu[key].keys():
      menu[el][answer]+= 1
      print(f'{menu[el][answer]} order of {answer} have been added to your meal')
      break

  else:
    print('Sorry this item is unavailable, please order item from our menu')
    

  answer = input()



