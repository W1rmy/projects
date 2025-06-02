import random
import time
from units import Gnom, Goblin, Ghost, Hero


def gnom_fight(hero, gnom=Gnom()):
  print("Вы встречаете гнома")
  time.sleep(2)
  print("Бой началсся")
  
  while hero.hp > 0 or gnom.hp > 0:
    deistvie = input("Что вы хотите сделать, attack, heal или run?: ").lower().rstrip().lstrip()
    if deistvie == "attack":
      print("Вы атакуете гнома")
      time.sleep(2)
      gnom.deffense(hero.damage())
      print(f"У гнома осталось хп {gnom.hp}/{gnom.hp_max}")
      time.sleep(2)
    elif deistvie == "heal":
      hero.use_heal()
    elif deistvie == "run":
      print("Вы убежали от гнома")
      return

    if gnom.hp == 0:
      print("Гном повержен")
      hero.coins += random.randint(20, 40)
      break
    
    time.sleep(2)
    print("Гном атакует вас") 

    if gnom.hp < 8:
      hero.deffense(gnom.rage())
      print("Гном разозлился, его атака умножилась на 2!!!!")
    else:
      hero.deffense(gnom.damage())


    print(f"У вас осталось хп {hero.hp}/{hero.hp_max}")

    if hero.hp == 0:
      print("Вы проиграли, гг")
      break   


def goblin_fight(hero, goblin=Goblin()):
  print("Вы встречаете гоблина")
  time.sleep(2)
  print("Бой началсся")

  while hero.hp > 0 or goblin.hp > 0:
    deistvie = input("Что вы хотите сделать, attack, heal или run?: ").lower().rstrip().lstrip()
    if deistvie == "attack":
      print("Вы атакуете гоблина")
      time.sleep(2)
      goblin.deffense(hero.damage())
      print(f"У гоблина осталось хп {goblin.hp}/{goblin.hp_max}")
    elif deistvie == "heal":
      hero.use_heal()
    elif deistvie == "run":
      print("Вы убежали от гоблина")
      return

    if goblin.hp == 0:
      print("Гоблин повержен")
      hero.coins += random.randint(30, 50)
      break

    time.sleep(2)
    print("гоблин атакует вас") 

    if random.randint(0, 100) > 70:
      hero.deffense(goblin.thorw_spear())
      print("Гоблин кидает копьё, его текущая атака увеличелась на 5!")
    else:
      hero.deffense(goblin.damage())

    print(f"У вас осталось хп {hero.hp}/{hero.hp_max}")

    if hero.hp == 0:
      print("Вы проиграли, гг")
      break


def ghost_fight(hero, ghost=Ghost()):
  lower_hero_attack = 1
  print("Вы встречаете призрака")
  time.sleep(2)
  print("Бой началсся")
  
  while hero.hp > 0 or ghost.hp > 0:
    deistvie = input("Что вы хотите сделать, attack, heal или run?: ").lower().rstrip().lstrip()
    if deistvie == "attack":
      print("Вы атакуете призрака")
      time.sleep(2)
      ghost.deffense(hero.damage() // lower_hero_attack)
      print(f"У призрака осталось хп {ghost.hp}/{ghost.hp_max}")
    elif deistvie == "heal":
      hero.use_heal()
    elif deistvie == "run":
      print("Вы убежали от призрака")
      return
      
    if ghost.hp == 0:
      print("призрак повержен")
      print("Вы покинули пещеру победителем")
      hero.coins += random.randint(20, 40)
      print("вы получили монеты","и у вас", hero.coins, "монет")
      break
    
    time.sleep(2)
    print("призрак атакует вас") 

    if random.randint(0, 100) > 80:
      print(f"Призрак сводит вас с ума, ваша атака уменьшена в {lower_hero_attack}")
      lower_hero_attack += 1
    else:
      hero.deffense(ghost.damage())
      
    print(f"У вас осталось хп {hero.hp}/{hero.hp_max}")

    if hero.hp == 0:
      print("Вы проиграли, гг")
      break 
