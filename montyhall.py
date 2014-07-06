

import os
import random



class Door:

	def __init__(self,name,prize,unopened):
		self.name = name
		self.prize = prize
		self.unopened = unopened

	def getName(self):
		return self.name

	def hasPrize(self):
		return self.prize

	def isOpen(self):
		return not self.unopened

	def opened(self):
		self.unopened = False

	def __str__(self):
		return 'Name:{0} Prize:{1} unopened:{2}'.format(self.name, self.prize, self.unopened)

class Game():

	def __init__(self, size=3):
		self.doors = []
		self.prizeDoor = None
		self.setPrize()
		self.size = size


	def setPrize(self):
		names=[str(x+1) for x in range(self.size)]
		prizeDoor = random.sample(names,1)[0]
		# door = None
		for name in names:
			if name == prizeDoor:
				door = Door(name, True, True)
				self.prizeDoor = name
			else:
				door = Door(name,False,True)

			self.doors.append(door)

	def reset(self):
		self.doors=[]
		self.setPrize()

	def unopenedDoors(self):
		return [door for door in self.doors if not door.isOpen()]

	def gameLoop(self, auto = False, ans='y'):

		if not auto:
			choice = raw_input('Choose a door 1,2 or 3: ')
		else:	
			choice = random.sample([str(x+1) for x in range(self.size)],1)[0]

		remainingDoors = [door for door in self.doors if (not door.getName() == choice) and not door.hasPrize()]

		doorToOpen = random.sample(remainingDoors,1)[0]

		if not auto:
			print ('\n{0} has been opened and does not contain any prize.').format(doorToOpen.getName())

		doorToOpen.opened()


		if not auto:
			ps = ('\nYour current door is {0}. Do you wish to change? Enter y to change, n to stay on the same door: ').format(choice)
			ans = raw_input(ps)

		if ans == 'y':
			choice = [door.getName() for door in self.unopenedDoors() if not door.getName() == choice][0]
		

		if choice == self.prizeDoor:
			if not auto:
				print ('You chose {0} and you win the prize!').format(choice)
			return True
		else:
			if not auto:
				print 'You have lost. The prize was behind {0}'.format(self.prizeDoor)
			return False


if __name__=='__main__':

	newgame = Game()


	wins = 0
	for i in range(1000):
		n = newgame.gameLoop(auto=True)

		wins += 1 if n else 0
		# raw_input('wins:{0}'.format(wins))
		os.system('cls')
		newgame.reset()

	print 'wins {0}'.format(wins)