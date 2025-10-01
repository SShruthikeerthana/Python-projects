import random 

while True:
  choice = input('\U0001F3B2 Roll the dice? (y/n): ').lower()
     
  if choice == 'y':
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'({die1}, {die2})')
      res=die1+die2
      print(f'sum:{res}')
      if res ==6:
          print('You win!')
          break
      elif res==3:
          print('you lose!')
          break
  elif choice == 'n':
      print('Thanks for playing!')
      break
  else:
      print('Invalid choice!')