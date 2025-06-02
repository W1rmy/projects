from fights import goblin_fight, gnom_fight, ghost_fight
from units import Gnom, Goblin, Ghost, Hero
import random 

goods = [
    {"id": 1, "item": {"Iron_Armor": 8}, "info": "броня выкованая гномом, 8 защиты", "cost": 150, "type": "armors"},
    {"id": 2, "item": {"Kompot_armror": 99999999999}, "info": "о ней ничего неизвестно, ? защиты", "cost": 9999999999, "type": "armors"},
    {"id": 3, "item": {"Gold_Armor": 10}, "info": "броня выкованая гоблином за неделю, 10 защиты", "cost": 200, "type": "armors"},
    {"id": 4, "item": {"Chain_Armor": 6}, "info": "тот-же самый герой, который не герой продал броню гоблинам, которые продали её нам, 6 защиты", "cost": 100, "type": "armors"},
    {"id": 5, "item": {"Diamond-Iron_Armor": 15}, "info": "герой, который герой отдал нам эту броню после выполнения заданий, 15 защиты ", "cost": 250, "type": "armors"},
    {"id": 6, "item": {"Knife": 6}, "info": "нож мясника, наносит 6 урона", "cost": 100, "type": "weapons"},
    {"id": 7, "item": {"Axe": 8}, "info": "Топор варвара, наносит 8 урона", "cost": 150, "type": "weapons"},
    {"id": 8, "item": {"Diamond_Sword": 10}, "info": "Герой, какой-то не герой, меч то потерял. Наносит 10 урона", "cost": 200, "type": "weapons"},
    {"id": 9, "item": {"Iron_Sword": 6}, "info": "Меч гоблина, ничего особенного,наносит 7 урона", "cost": 125, "type": "weapons"},
    {"id": 10, "item": {"Enchanted_Stick": random.randint(5, 7)}, "info": "Палка, которую зачаровал герой, который герой. Всегда наносит от 5 до 7 урона", "cost": 125, "type": "weapons"},
    {"id": 11, "item": "kompot lvl 1", "info": "газировка2 < Бабушкин компот > газировка1. Хилит 15 hp", "cost": 20, "type": "heals"},
    {"id": 12, "item": "kompot lvl 2", "info": "газировка2 < Бабушкин компот > газировка1. Хилит 25 hp", "cost": 40, "type": "heals"},
    {"id": 13, "item": "kompot lvl 3", "info": "газировка2 < Бабушкин компот > газировка1. Хилит 45 hp", "cost": 100, "type": "heals"},
  ]

swords = [
    {"id": 1, "item": {"Knife": 5}, "info": "нож мясника, наносит 6 урона", "cost": 100, "type": "weapons"},
    {"id": 2, "item": {"Axe": 8}, "info": "Топор варвара, наносит 8 урона", "cost": 150, "type": "weapons"},
    {"id": 3, "item": {"Diamond_Sword": 10}, "info": "Герой, какой-то не герой, меч то потерял. Наносит 10 урона", "cost": 200, "type": "weapons"},
    {"id": 4, "item": {"Iron_Sword": 6}, "info": "Меч гоблина, ничего особенного,наносит 7 урона", "cost": 125, "type": "weapons"},
    {"id": 5, "item": {"Enchanted_Stick": random.randint(5, 7)}, "info": "Палка, которую зачаровал герой, который герой. Рандомно наносит от 5 до 7 урона", "cost": 125, "type": "weapons"},
  ]


def market(hero, goods):
  print("Добро пожаловать в магазин")
  print(f'У вас {hero.coins} монет')
  
  for good in goods:
    for key in good:
      print(f"{key}: {good[key]}")
    print("--------------------------------------------")

  buy = int(input("Что хотите купить? (Введите id): "))
  print(f'У вас {hero.coins} монет')

  while buy != 777:  
    if len(goods) + 1 > buy > 0:
      good = goods[buy - 1]
      if hero.coins >= good["cost"]:
        hero.coins -= good["cost"]
        if good["type"] == "armors":
          hero.add_armor(good["item"])
          hero.switch_armor()
        elif good["type"] == "weapons":
          hero.add_weapon(good["item"])
          hero.switch_weapon()
        else:
          hero.add_heal(good["item"])
      else:
        print("Не хвататет монет")
    else:
      print("Данного товара нет")
    print(f'У вас {hero.coins} монет')
    buy = int(input("Что хотите купить? (Введите id или 777 для завершения покупок): "))
    

def cave(hero):
  ghost_fight(hero)
  if hero.hp == 0:
    print("Вы проиграли")
    hero.hp = hero.hp_max
    return
  goblin_fight(hero)
  if hero.hp == 0:
    print("Вы проиграли")
    hero.hp = hero.hp_max
    return
  gnom_fight(hero)


def cave_lvl_2(hero):
  ghost = Ghost(name="Ghost", armor=6, hp_max=66)
  goblin = Goblin(name="goblin", hp_max=30, damage=15, armor=5)
  gnom = Gnom()
  if hero.hp == 0:
    print("Вы проиграли")
    hero.hp = hero.hp_max
    return
  ghost_fight(hero)
  goblin_fight(hero)
  gnom_fight(hero)
