from units import Hero, Gnom, Goblin, Ghost
from fights import goblin_fight, gnom_fight, ghost_fight
from places import market, cave, goods, swords
import time


hero = Hero()

print("После обычного школьного дня вы идёте по дороге домой и видете портал.")
time.sleep(4)

a = input("Войти в портал? (да/нет): ")
if a != "да":
  print("Он слишком манит вас.")
 
print("Вы подходите ближе и чувствуете необычную энергию исходящую из него.")
time.sleep(4)
print("Вы с опаской косаетесь его и что-то резко начинает менятся.")
time.sleep(4)
print("Не успев моргнуть вы видите как привычные дома меняются на необочные пейзажи")
time.sleep(4)
print("Ты осознаешь что оказался в новом мире")

b = input("готовы ли вы к приключениям? (да/нет): ")
if b == "да":
  print("Ну что ж, начнём!")
else:
  print("Уже никуда не дется, пойдём!")
  
print("Осматревшись вы понимаете что лежите на грядке капусты")  
time.sleep(4)
print("Вдруг раздается чей-то не довольный крик")
time.sleep(4)
print("Кто-то: ЧЁ ты делаешь у меня в огороде!?")
time.sleep(4)

print("Вы: *невнятные звуки*")
time.sleep(4)
print("Гоблин-Боблин: А, понятно, я Гоблин-Боблин, зачастили к нам попаданцы")
time.sleep(4)
print("Гоблин-Боблин: Ну ладно, я готов дать тебе задание за которое я дам тебе 100 монет и kompot, ты согласен?")
time.sleep(4)
n = input("Ты согласен? (да/нет): ")
time.sleep(4)

if n == "да":
  time.sleep(4)
  print("Гоблин-Боблин: Хорошо, тогда давай начнём!")
else:
  print("Вы: *невнятные звуки*")
  print("У тебя нет выбора, дорогой друг")


print("Гоблин-Боблин: Смотри, иди в магазин и купи себе оружие, а то задание будет невыполнимым")
hero.coins += 100


print("*Вы получили компот первого уровня и 100 монет*")


places = ["Home", "Market", "Cave", "Forest", "Castle", "Exit"]
starter_turn = input("Введите куда вы хотите пойти Home/Market/Cave/Forest/Castle/Exit: ").strip().capitalize()

while starter_turn != "Market":
  print("Вы не можете войти в подземелье, пока вы не купите оружие")
  starter_turn = input("Введите куда вы хотите пойти Home/Market/Cave/Forest/Castle/Exit: ").strip().capitalize()
market(hero, swords)


turn = input("Введите куда вы хотите пойти Home/Market/Cave/Forest/Castle/Exit: ").strip().capitalize()
while True:
  print()
  if turn == "Market":
    market(hero, swords)
  elif turn == "Cave":
    print(hero.weapon.get("stick"))
    if hero.weapon.get("stick") is not None:
      print("Вы не можете войти в подземелье, пока вы не купите оружие")
    else:
      print("Вы входите в пещеру")
      cave(hero)


  turn = input("Введите куда вы хотите пойти: ").strip().capitalize()
