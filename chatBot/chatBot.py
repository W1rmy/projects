attempts = 1
print("Привет, я чат-бот Майнкрафт - это моя жизнь!, я задам тебе пару вопросов по Майнкрафт")

print('Первый вопрос: Какой самый ценный материал с версии 1.16?')
player_answer1 = input('Ответ = ')
while player_answer1 != 'незерит':
  print('Ваш ответ не верен')
  player_answer1 = input('Ответ = ')
  attempts += 1
print('Молодец, правильно')

print('Второй вопрос: Кагого цвета был первая кровать?')
player_answer2 = input('Ответ = ')
while player_answer2 != 'красного':
  print('Ваш ответ не верен')
  player_answer2 = input('Ответ = ')
  attempts += 1
print('здорово!')

print('Третий вопрос: На какой версии впервые был найден херобрин?')
player_answer3 = input('Ответ = ')
while player_answer3 != 'Alpha 1.0.16_02':
  print('Ваш ответ не верен')
  player_answer3 = input('Ответ = ')
  attempts += 1 
print('здорово!')
print('Четвертый вопрос: Какая игра была популярна и похожа на майнкрафт, в названии этой игры было слово "онлайн" ')
player_answer4 = input('Ответ = ')
while player_answer4 != 'Копатель онлайн':
  print('Ваш ответ не верен')
  player_answer4 = input('Ответ = ')
  attempts += 1
print('Пятый вопрос: сколько всего видов тропических рыб в майнкрафте на данный момент?')
player_answer5 = input('Ответ = ')
print('не правильно')
print('ахахаха, шучу их 3584')
if player_answer5 == 3584:
  print('Чтооооо, вы правда это знаете??')
print('Следующий вопрос: Какая выысота была максимальной от версии 1.12.2 - 1.14.1? Ответ дайте в одном числе')
player_answer6 = input('Ответ = ')
while player_answer6 != '256':
  print('Ваш ответ не верен')
  player_answer6 = input('Ответ = ')
  attempts += 1
print('Седьмой вопрос: Как приручить попугая? Ответ дайте одоним словом в Иминительном падеже')  
player_answer7 = input('Ответ = ')
while player_answer7 != 'Семянами':
  print('Ваш ответ не верен')
  player_answer7 = input('Ответ = ')
  attempts += 1
print('Восьмой вопрос: Где достать элитры? Пример ответа: В деревне')  
player_answer8 = input('Ответ = ')
while player_answer8 != 'В городе края':
  print('Ваш ответ не верен')
  player_answer8 = input('Ответ = ')
  attempts += 1
print('Девятый вопрос: Можно ли ложиться спать в аду или эндер мире? В ответе вы должны написать: нет или да')  
player_answer9 = input('Ответ =Да ')
while player_answer9 != '':
  print('Ваш ответ не верен')
  player_answer9 = input('Ответ = ')
  attempts += 1
print(f'Вы потратили {counter} попыток')
print('Не стал писать много вопросов, чтобы вас не мучить :]')
