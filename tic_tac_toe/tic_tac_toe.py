from random import randint 

name1 = input("введите имя игрока 1:")
name2 = input("введите имя игрока 2:")

if randint(1, 2) == 1:
  firstPlayer = name2
  secondPlayer = name1
else:
  firstPlayer = name1
  secondPlayer = name2

board = ['_'] * 9
signs = ['X', 'O']

turns = 0
endgame = False

print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])
print()

while turns != 9:
  if endgame:
    break
  
  sign = signs[turns % 2]
  if sign == 'X':
    print(f'{firstPlayer} ходит сейчас ')
  else:
    print(f"{secondPlayer} ходит сейчас")
  
  place = int(input(f'Куда хотите поставить {sign}: '))
  while board[place - 1] != '_':   
    print("это клетка занята")
    place = int(input(f'Куда хотите поставить {sign}: '))

  board[place - 1] = sign 
  
  print(board[0], board[1], board[2])
  print(board[3], board[4], board[5])
  print(board[6], board[7], board[8])
  print()

  # проверка победы в строчку
  for i in range(0, 9, 3): # i = 0, i = 3, i = 6
    if board[i] == board[i + 1] == board[i + 2] != '_':
      print(f'{sign} win!')  
      endgame = True
      break

  # проверка победы в столбец
  for i in range(3):
    if board[i] == board[i + 3] == board[i + 6] != '_':
      print(f'{sign} win!')
      endgame = True
      break

  # проверка победы по диагонали
  if board[0] == board[4] == board[8] != '_' or board[2] == board[4] == board[6] != '_':
    print(f'{sign} win!')
    endgame = True
    break
  
  
  turns += 1
