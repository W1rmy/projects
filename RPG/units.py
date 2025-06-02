class Unit:
  hp_max = 0
  hp = hp_max
  armor = {}
  weapon = {}
  name = ""

  def atack(self):
    return self.weapon[list(self.weapon.keys())[0]] 
  
  def deffense(self, damage):
    if list(self.armor.values())[0] // 2 < damage:
      self.hp -= (damage - list(self.armor.values())[0] // 2)
      
      if self.hp < 0:
        self.hp = 0
    else:
      print("Броню не получилось пробить, купите новое оружие в Market")

  def info(self):
    print(f"Имя: {self.name}, hp: {self.hp}, armor: {self.armor}, weapons: {self.weapon}")

  def damage(self):
    return list(self.weapon.values())[0]


class Hero(Unit):
  hp_max = 40
  hp = hp_max
  armor = {"bandage" : 1}
  weapon = {"stick": 2}
  name = "Гегр"
  heals = {"kompot lvl 1" : 15, "kompot lvl 2" : 25, "kompot lvl 3" : 45}
  coins = 0
  inventory = {"armors": {}, "weapons": {}, "heals": {"kompot lvl 1" : 1, "kompot lvl 2" : 0, "kompot lvl 3" : 0}}


  def item_in_inventory(self):
    if self.inventory in self.inventory["armors"] or self.inventory in self.inventory["weapons"] or self.inventory in self.inventory["heals"]:
      print("В инвентаре есть предметы")
     
  def add_heal(self, heal):
    self.inventory["heals"][heal] += 1
    print(f"Вы положили в инвентарь {heal}")
  
  def add_weapon(self, new_weapon):
    self.inventory["weapons"] = self.inventory["weapons"] | new_weapon
    print(f"Вы положили в инвентарь оружие {new_weapon}")
    
  def add_armor(self, new_armor):
    self.inventory["armors"] = self.inventory["armors"] | new_armor
    print(f"Вы положили в инвентарь броню {new_armor}")
  
  def switch_weapon(self):
    print("У вас есть оружие(я)", self.inventory["weapons"])
    weapon = input("Выберите оружие: ") 
    if weapon not in self.inventory["weapons"]:
      print("У вас нет такого оружия")
    else:
      self.add_weapon(self.weapon)
      self.weapon = {weapon: self.inventory["weapons"][weapon]}
      del self.inventory["weapons"][weapon]
      print("Вы успешно сменили оружие на", weapon)
  
  def switch_armor(self):
    print("У вас есть брони", self.inventory["armors"])
    armor = input("Выберите броню: ") 
    if armor not in self.inventory["armors"]:
      print("У вас нет такой брони")
    else:
      self.add_armor(self.armor)
      self.armor = {armor: self.inventory["armors"][armor]}
      del self.inventory["armors"][armor]
      print("Вы успешно сменили оружие на", armor)
      
  def use_heal(self):
    print("У вас есть хилки", self.inventory['heals'])
    heal = input("Выберите хилку: ")
    if heal in self.inventory["heals"] and self.inventory["heals"][heal] > 0:
      if self.hp == self.hp_max:
        print("У вас фулл хп")
      else:
        self.hp += self.heals[heal]
        self.inventory["heals"][heal] -= 1 
        
        if self.hp > self.hp_max:
          self.hp = self.hp_max

        print(f"Вы использовали {heal}, ваше количество жизний {self.hp}/{self.hp_max}")
    else:
      print("У вас нет такой хилки")
   

class Goblin(Unit):
  hp_max = 20
  hp = hp_max
  armor = {"leather armbands": 3}
  weapon = {"axe": 10}
  using_weapon = "arm"
  using_armor = "leather armbands"
  name = "goblin"
  spears = 3

  def __init__(self, name="goblin", hp_max=20, damage=10, armor=3):
    self.name = name
    self.hp_max = hp_max
    self.hp = hp_max
    self.weapon[list(self.weapon.keys())[0]] = damage
    self.armor[list(self.armor.keys())[0]] = armor

  def thorw_spear(self):
    if self.spears > 0:
      self.spears -= 1
      return self.weapon["axe"] + 5
    else:
      print("Гоблин потерял копью у гоблина (-100 соц. рейтинга, -кошка жена, миска рис) не влиет на игру")
      return 0
  

class Gnom(Unit):
  hp_max = 20
  hp = hp_max
  armor = {"gnom_armor": 5 }
  weapon = {"stone_sword": 6 }
  using_weapon = "stone_sword"
  using_armor = "gnom_armor"
  name = "Gnom"

  def __init__(self, name="Gnom", hp_max=20, damage=6, armor=5):
    self.name = name
    self.hp_max = hp_max
    self.hp = hp_max
    self.weapon[list(self.weapon.keys())[0]] = damage
    self.armor[list(self.armor.keys())[0]] = armor
  
  def rage(self):
    return self.weapon[self.using_weapon] * 2

class Ghost(Unit):
  hp_max = 23
  hp = hp_max
  armor = {"Ghost": 3}
  weapon = {"Ghost": 3}
  using_weapon = "arm"
  using_armor = "Ghost"
  name = "Ghost"

  def __init__(self, name="Ghost", hp_max=23, damage=3, armor=3):
    self.name = name
    self.hp_max = hp_max
    self.hp = hp_max
    self.weapon[list(self.weapon.keys())[0]] = damage
    self.armor[list(self.armor.keys())[0]] = armor

  
  def lower_attk_hero(self, hero, coff):
    hero.using_weapons //= coff
