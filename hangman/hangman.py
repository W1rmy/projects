from turtle import *
import random

tems = {
        'Животные': ['кот', 'собака', 'попугай', 'кролик', 'медведь', 'лев', 'тигр'],
        'Овощи': ['огурец', 'помидор', 'картошка', 'лук', 'морковь', 'перец', 'свекла'],
        'Города': ['москва', 'cанкт-петербург', 'уфа', 'казань', 'нижний новгород'],
        'Фрукты': ['яблоко', 'банан', 'апельсин' , 'арбуз', 'виноград', 'груша', 'дыня']
       }

user_tem = input('Выберете тему: "Животные" или "Овощи" или "Города" или "Фрукты"')

while True:
  if user_tem in tems:
    word = random.choice(tems[user_tem])
    break
  else:
    print("Такой темы нет, глупенький")
    user_tem = input('Выберете тему: "Животные" или "Овощи" или "Города" или "Фрукты"')

user_word = ['*'] * len(word)
attempts = 0

while True:
  print(*user_word)
  char = input("Введите букву: ").lower()
  if char in word:
    for i in range(len(word)):
      if word[i] == char:
        user_word[i] = char  
  else:      
    attempts += 1
    print('Неверно!..')
    print('Осталось попыток:', 7 - attempts)
    
  if attempts == 1:
    left(90)
    right(45)
    forward(45)
    right(90)
    forward(45)
  elif attempts == 2:
    back(45)
    left(135)
    forward(90)
  elif attempts == 3:
    right(90)
    forward(45)
  elif attempts == 4:
    right(90)
    forward(10)
    penup()
    forward(15)
    right(90)
    forward(15)
    left(90)
    pendown()
    circle(15)
    penup()
    forward(15)
    left(90)
    forward(15)
    right(90)
    pendown()
  elif attempts == 5:
    forward(70)
  elif attempts == 6:
    right(35)
    forward(45)
    back(45)
    left(70)
    forward(45)
    back(45)
    right(35)
  elif attempts == 7:
    back(55)
    right(45)
    forward(45)
    back(45)
    left(90)
    forward(45)
    
  if attempts == 7:
    print("Вы прооиграли!!!")
    break
    
  if '*' not in user_word:
    print("you win!")
    break
