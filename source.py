# Python D&D game

def roll(rolls, num):
	sum = 0
	from random import randint
	for i in range(rolls):
		sum += randint(1, num)
	return sum


class Monster:
	def __init__(self, name, AC, HP, STR, DEX, CON, INT, WIS, CHA):
		self.name=name
		self.AC=AC
		self.HP=HP
		self.STR=STR
		self.DEX=DEX
		self.CON=CON
		self.INT=INT
		self.WIS=WIS
		self.CHA=CHA
		self.str=int((STR-10)/2)
		self.dex=int((DEX-10)/2)
		self.con=int((CON-10)/2)
		self.int=int((INT-10)/2)
		self.wis=int((WIS-10)/2)
		self.cha=int((CHA-10)/2)
	def swim(self):
		print("The monster is swimming towards you.")

class Zombie(Monster):
	def __init__(self, name, AC=8, rolls=3, num=8, add=9, STR=13, DEX=6, CON=16, INT=3, WIS=6, CHA=5):
		self.name=name
		self.AC=AC
		self.rolls=rolls
		self.num=num
		self.add=add
		self.STR=STR
		self.DEX=DEX
		self.CON=CON
		self.INT=INT
		self.WIS=WIS
		self.CHA=CHA
		self.str=int((STR-10)/2)
		self.dex=int((DEX-10)/2)
		self.con=int((CON-10)/2)
		self.int=int((INT-10)/2)
		self.wis=int((WIS-10)/2)
		self.cha=int((CHA-10)/2)
		self.HP=roll(rolls, num)+add # when referenced here, HP is different for each instance and can be appropriately modified later :)
	#Slam attack
	def attack(self):
		return roll(1, 20) + 3
	def damage(self):
		return roll(1, 6) + self.str
	def exit_message(self):
		print("The Zombie crumbled into pieces.")

Zombie1 = Zombie("Zombie")

class Player:
	def __init__(self, name, lv, AC, HP, STR, DEX, CON, INT, WIS, CHA):
		self.name=name
		self.lv=lv
		self.AC=AC
		self.HP=HP
		self.STR=STR
		self.DEX=DEX
		self.CON=CON
		self.INT=INT
		self.WIS=WIS
		self.CHA=CHA
		self.str=int((STR-10)/2)
		self.dex=int((DEX-10)/2)
		self.con=int((CON-10)/2)
		self.int=int((INT-10)/2)
		self.wis=int((WIS-10)/2)
		self.cha=int((CHA-10)/2)


Player1 = Player("Theren", 1, 15, 30, 15, 13, 16, 10, 9, 7)

class Weapon:
	def __init__(self, name, rolls, num, ability_mod, damage_type):
		self.name=name
		self.rolls=rolls
		self.num=num
		self.ability_mod=ability_mod
		self.damage_type=damage_type

###Weapons
Dagger = Weapon("Dagger", 1, 4, Player1.str, "piercing")

###Combat Sequence
enemy = Zombie1
player_weapon = Dagger
print("A " + enemy.name + " appeared!")
print(enemy.name + "'s HP: " + str(enemy.HP))
###Initiative
turn = 0
Player1.initiative=roll(1, 20) + Player1.dex
enemy.initiative=roll(1, 20) + enemy.dex
if enemy.initiative > Player1.initiative:
	turn += 1
total = 2
###Combat
while True:
	if turn % total == 0:
		attack=roll(1, 20) + player_weapon.ability_mod
		if attack > enemy.AC:
			damage = roll(player_weapon.rolls, player_weapon.num) + player_weapon.ability_mod
			enemy.HP -= damage
			if enemy.HP > 0:
				print("You dealt " + str(damage) + " damage!")
				print(enemy.name + "'s HP: " + str(enemy.HP))
				turn += 1
			else:
				print("You dealt " + str(damage) + " damage!")
				enemy.exit_message()
				print("You defeated the " + enemy.name + "!")
				turn += 1
				break
		else:
			print("You missed.")
			turn += 1
	elif turn % total == 1:
		attack = enemy.attack()
		if attack > Player1.AC:
			damage = enemy.damage()
			Player1.HP -= damage
			if Player1.HP > 0:
				print("The " + enemy.name + " dealt " + str(damage) + " damage!")
				print("Player's HP: " + str(Player1.HP))
				turn +=1
			else:
				print("The " + enemy.name + " dealt " + str(damage) + " damage!")
				print("The " + enemy.name + " knocked you out!")
				turn += 1
				break
		else:
			print("The " + enemy.name + " missed.")
			turn +=1
	else:
		turn +=1
print("What to do next...?")





