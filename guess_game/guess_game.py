from random import randint

print('Добро пожаловать в игру "Угадай число"')
x = int(input('Введите натуральное число, между которого будет считаться рандом:' ))
y = int(input('Введите другое натуральное число, между которого будет считаться рандом:'))

while x == y:
  print('Равные числа нельзя')
  y = int(input('Введите другое натуральное число, между которого будет считаться рандом:'))

if y > x:
  print(f'Я загадал число от {x} до {y}')
else:
  print(f'Я загадал число от {y} до {x}')

print('Попробуй угадать его за минимальное количество попыток')
print('(Загаданное число не изменяется)')

if x < y:
  number = randint(x, y)
else:
  number = randint(y, x)
  
counter = 0 

while True:
  player_answer = int(input('введите число:'))
  if  player_answer == number:
    print('Ты угадал!!!!')
    counter += 1
    break
  else:
    print('Ты не угадал')
    counter += 1

if counter == 1:
  print(f'Вы потратили {counter} попытку')
elif counter ==2 or counter == 3 or counter == 4:
  print(f'Вы потратили {counter} попытки')
else:
  print(f'Вы потратили {counter} попыток ')
