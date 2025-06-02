import random

ocko_hum = 1488 * 0
ocko_ai =  0
rsp = ['камень', 'ножницы', 'бумага']
rsp_hum = input('камень ножницы или бумага: ')
rsp_ai = random.choice(rsp)

while ocko_hum <= 3 or ocko_ai <= 3:
  print(f'Вы выбрали {rsp_hum}, компьютер выбрал {rsp_ai}')
  
  if rsp_hum == 'ножницы' and rsp_ai == 'бумага':
    ocko_hum += 1
  if rsp_hum == 'бумага' and rsp_ai == "ножницы":
    ocko_ai += 1
  if rsp_hum == "камень" and rsp_ai == "ножницы":
    ocko_hum += 1
  if rsp_ai == rsp_hum:
    ocko_ai += 0.5
    ocko_hum += 0.5
  if rsp_hum == "бумага" and rsp_ai == "камень": 
    ocko_hum += 1
  if rsp_ai == "бумага" and rsp_hum == "камень":
    ocko_ai += 1
  if rsp_ai == "камень" and rsp_hum == "ножницы":
    ocko_ai += 1
    
  print(f'Вы {ocko_hum}, компьютер {ocko_ai}')
  
  rsp_hum = input('камень ножницы или бумага: ')
  rsp_ai = random.choice(rsp)

  
