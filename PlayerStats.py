"""

Written by: Viktor Dominguez (with some help from Python.org, OverStack, and W3)
Debugged/tested (painstakenly) by: Viktor Dominguez
Date Started: 12/03/2022 (mm/dd/yyyy)
Last update: 04/18/2025 (mm/dd/yyyy)
Editor: Sublime Text

------------
DESCRIPTION
------------
A simulation of my DnD group's current campaign setup. Also was a way for me to practice OOP and Classes in Python. Enjoy messing with it.
Obviously there's other stuff that can be done. I didn't want to do it though :P I just wanted to get names, stats, and dice rolling done.
There's health and armour in case I ever decide to change it to allow for simulated battles...maybe some other day.

This program is written as a script to run in a terminal. If you want to run it in a console, you might have to change the clear() function.

--------
LICENSE
--------
None, but some credit is always appreciated :)

"""

from random import randint
import sys
from time import sleep
import os


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


# Delayed Text Output Function
def delay_readout(string):
	for char in string:
		sys.stdout.write(char)
		sys.stdout.flush()
		sleep(0.05)

# Main class to build characters
class Player:
	def __init__(self, name, health, armour, STR, DEX, CONS, INT, WIS, CHR, prof):
		self.name = name
		self.health = health
		self.armour = armour
		self.STR = STR
		self.DEX = DEX
		self.CONS = CONS
		self.INT = INT
		self.WIS = WIS
		self.CHR = CHR
		self.prof = prof
		# self.money = money

	# potential Greetings Screen when program is started
	def greetings(self):
		print(f"\nGreetings, {self.name}! Here is your status:\n")
		print(f"\n{self.health}\n{self.armour}\n\n")


	# Normal Dice Roll Function with error checks
	def diceRoll(self, stat, statName):
		"""

		stats:

		2-3 = -4
		4-5 = -3
		6-7 = -2
		8-9 = -1
		10-11 = 0
		12-13 = +1
		14-15 = +2
		16-17 = +3
		>18 = +4

		"""
		if stat in range(4):
			bonus = -4
		elif stat in range(4, 6):
			bonus = -3
		elif stat in range(6, 8):
			bonus = -2
		elif stat in range(8, 10):
			bonus = -1
		elif stat in range(10, 12):
			bonus = 0
		elif stat in range(12, 14):
			bonus = 1
		elif stat in range(14, 16):
			bonus = 2
		elif stat in range(16, 18):
			bonus = 3
		else:
			bonus = 4
		
		total = 0

		while True:
			clear()
			delay_readout(f"\nNow how many SIDES will your die have, Master {self.name} (6-20 or 0 for random): ")
			try:
				n = int(input())
			except ValueError:
				delay_readout("\nYou have somehow entered something that is not possible, Sire. Are you perhaps having one of those stroke thingies I have heard so much about? (y/n): ")
				sleep(1.5)
				delay_readout("n")
				sleep(2.0)
				delay_readout("ads;fajf;sdlfkjsfd\n")
				sleep(1.0)
				delay_readout("\nI see, well Sire I'm willing to give you one more chance so if you can, please select a number from 6 to 20.\n")
				sleep(1.5)
				delay_readout("Or you can pick 0 and have me pick for you.\n\nThank the gods for magic or some of these die would be impossible to manufacture...\n")
				delay_readout("I mean, have you ever seen a 13 sided die in the natural world? Yeah, I didn't think so")
				sleep(2.5)
				continue
			if n == 0:
				n = randint(6,20)
				delay_readout("\n...")
				sleep(2.0)
				delay_readout("\n*CLINK*")
				sleep(1.0)
				delay_readout("\n*CLANK*")
				sleep(1.0)
				delay_readout("\n...")
				sleep(2.5)
				delay_readout(f"\n\nI'm back from slaving away making that {n}-sided die you wanted.")
				sleep(2.0)
				delay_readout(" ...\n")
				sleep(2.5)
				delay_readout("You didn't ask for this? You just chose random and then I walked away?...")
				sleep(2.0)
				delay_readout("Fuck.\n")
				sleep(1.0)
				delay_readout("\nWell let's roll this fucker I guess...")
				sleep(1.5)
				delay_readout("Sire.")
				sleep(1.5)
				break
			elif n in range(6,21):
				break
			else:
				delay_readout("\nSire, you have quite the imagination. But that is an invalid number. Please pick a number from 6 to 20 or the number 0 if you want me to pick for you.\n")
				sleep(1.5)

		while True:
			clear()
			delay_readout(f"\nNow please enter how many ROLLS you will make, Master {self.name} (1-please nothing bigger than 6; 0 for random): ")
			try:
				rolls = int(input())
			except ValueError:
				delay_readout("\nSire has a big, smooth brain, don't you? Please select a number this time... Any number above 0 will do. Hell, even 0 works too.\n")
				sleep(1.5)
				continue
			if rolls == 0:
				rolls = randint(1, 10)
				if rolls == 1:
					delay_readout("\nOnce should do, I don't want to throw out my shoulder or anything.\n")
					sleep(1.5)
					break
				else:
					delay_readout(f"\nI shall roll {rolls} times...or will I?")
					sleep(1.5)
					delay_readout(" Yeah, I will...")
					sleep(1.0)
					delay_readout("or will I...")
					sleep(2.0)
					delay_readout("I will, I will! No SONKS.")
					sleep(1.5)
					delay_readout(".")
					sleep(1.0)
					delay_readout(".")
					sleep(1.5)
					delay_readout("No SONKS\n")
					sleep(1.0)
					break
			elif rolls in range(21):
				break
			elif rolls > 20:
				delay_readout(f"\n...really? You want me to sit here and roll this fucker {rolls} times?")
				delay_readout("\nYou know I've got other things to do today. Please pick something a little more reasonable, Sire.\n")
				sleep(2.5)
			else:
				delay_readout("\n...You have to roll at least once, Sire. How does one roll that many times anyways?\n")
				sleep(1.5)

		for i in range(1,rolls+1):
			value = randint(1,n)
			total += value
			delay_readout("\nRolling...")
			sleep(2.0)
			delay_readout("\nRolling...")
			sleep(1.5)
			delay_readout(f"{value}!!\n")
			if value == n:
				delay_readout(f"NAT {n}!!\n")
				sleep(1.0)
			elif value == 1:
				delay_readout("Oof...That's rough buddy.\n")
				sleep(1.0)
			delay_readout(f"\nRolls left: {rolls - i}\n")
			sleep(0.5)
			if i == rolls:
				delay_readout(f"\nSire's total after all those rolls: {total} // Out of a possible {n*rolls}")
				delay_readout(f"\nAdding your ability score of {bonus}, your actual total is {total + bonus}.\n\n")
				sleep(1.5)
				if self.prof == statName:
					delay_readout(f"\nOh-ho, I almost forgot about Sire's proficiency bonus, which makes the actual for-realsies total {total + bonus + 2}!\n\n")
					sleep(2.5)
		return

	def dropLowestRoll(self, stat, statName):
		"""

		stats:

		2-3 = -4
		4-5 = -3
		6-7 = -2
		8-9 = -1
		10-11 = 0
		12-13 = +1
		14-15 = +2
		16-17 = +3
		>18 = +4

		"""
		if stat in range(4):
			bonus = -4
		elif stat in range(4, 6):
			bonus = -3
		elif stat in range(6, 8):
			bonus = -2
		elif stat in range(8, 10):
			bonus = -1
		elif stat in range(10, 12):
			bonus = 0
		elif stat in range(12, 14):
			bonus = 1
		elif stat in range(14, 16):
			bonus = 2
		elif stat in range(16, 18):
			bonus = 3
		else:
			bonus = 4

		values = []
		while True:
			clear()
			delay_readout(f"\nNow how many SIDES will your die have, Master {self.name} (6-20 or 0 for random): ")
			try:
				n = int(input())
			except ValueError:
				delay_readout("\nThat...that's not even possible, Sire.\nThis task is so easy, a caveman's toddler could do it. Select an integer from 6 to 20.")
				delay_readout("\n\nIf you really can't decide, choose 0 and let me pick for you, Master.\n")
				sleep(2.5)
				continue
			if n == 0:
				n = randint(6, 20)
				delay_readout(f"\nI finished making that {n}-sided die, time to decided how many tosses to give this bad boy.")
				sleep(1.5)
				break
			elif n in range(6,21):
				break
			else:
				delay_readout("\nYour creativity knows no bounds, Sire. But I do require a number; either from 6 to 20 or a plain ol' 0.\n")
				sleep(1.5)

		while True:
			clear()
			delay_readout(f"\nNow please enter how many ROLLS you will make, Master {self.name} (2-please nothing bigger than 6; 0 for random): ")
			try:
				rolls = int(input())
			except ValueError:
				delay_readout("\nYour friends must love your big, smooth-brain energy, huh? Please select a number this time... Any number above 1 will do.\n")
				sleep(1.5)
				continue
			if rolls == 0:
				rolls = randint(2,11)
				delay_readout(f"\nI guess I'll roll this thing...I don't know maybe like {rolls} times? That should be plenty of rolls, can't be rolling all day now can we?")
				sleep(1.5)
				clear()
				break
			elif rolls > 1 and rolls < 22:
				sleep(1.5)
				clear()
				break
			elif rolls > 21:
				delay_readout(f"\n...I know I didn't say this, but no. No way we're going to sit here and roll this die {rolls} times! The most I'll do is 21\n\n")
				sleep(1.5)
				delay_readout("......\n")
				sleep(1.5)
				delay_readout("\nYou better not...")
				sleep(2.5)
				delay_readout("Please don't, I have a family...")
				sleep(2.0)
				delay_readout("Fuck :'( Tell my wife I loved her\n")
				sleep(2.0)
				clear()
				rolls = 21
				delay_readout(f"\nNow please enter how many ROLLS you will make, Master {self.name} (2-please nothing bigger than 6; 0 for random): ")
				sleep(1.5)
				delay_readout("2")
				sleep(1.5)
				delay_readout("1")
				sleep(2.5)
				delay_readout("\n\nYou  motherfu")
				clear()
				break
			else:
				delay_readout("\n*Sigh*")
				sleep(1.0)
				delay_readout("\n...Sire, you have to roll at least twice.\n")
				sleep(1.0)

		for i in range(1,rolls+1):
			rollValue = randint(1,n)
			values.append(rollValue)
			values.sort()
			delay_readout("\nRolling...")
			sleep(2.0)
			delay_readout("\nRolling...")
			sleep(1.5)
			delay_readout(f"{rollValue}!!\n")
			if rollValue == n:
				delay_readout(f"NAT {n}!!\n")
			elif rollValue == 1:
				delay_readout("Oof...That's rough buddy.\n")
			delay_readout(f"\nRolls left: {rolls - i}\n")
			sleep(1.0)
			if i == rolls:
				delay_readout(f"\nI will now drop that hideous {values[0]} you rolled earlier, Sire...\n")
				sleep(0.5)
				values.pop(0)
				total = sum(values)
				delay_readout(f"\nAnd with that abomination gone, here is Sire's total after all those rolls: {total} // Out of a possible {n*(rolls-1)}")
				delay_readout(f"\nAdding your ability score of {bonus}, your actual total is {total + bonus}.\n\n")
				sleep(1.5)
				if self.prof == statName:
					delay_readout(f"\nOh-ho, I almost forgot about Sire's proficiency bonus! Here is your for-realsies total: {total + bonus + 2}!\n\n")
					sleep(2.5)
		return


if __name__ == '__main__':

	# Function to choose Player 1's Stats
	def chooseStats(name):
		allowance = 20
		statOptions = ["STR", "DEX", "CONS", "INT", "WIS", "CHR"]
		stats = {'STR': 8, 'DEX': 8, 'CONS': 8, 'INT': 8, 'WIS': 8, 'CHR': 8, 'prof': ''}

		delay_readout("\nYou have been graced by the gods, Sire. They have given you some 'points' to change your personality characteristics.\n")
		sleep(1.0)
		delay_readout("Wish they would do something about the famines and wars and plagues, but I'm sure they've got other things to worry about...")
		sleep(2.0)

		# Menu for choosing stats (Selection While Loop)
		while True:
			clear()
			delay_readout(f"Your current allowance: {allowance}")
			# List the options for stats (and exit option)
			for i, (k,v) in enumerate(stats.items(), start = 1):
				if i == len(stats):
					delay_readout("\nQ) All Done")
					continue
				delay_readout(f"\n{i}) {k}: {v}")
			
			# Choosing which stat to edit
			delay_readout(f"\n\nNow choose which stat you would like to change (1-{len(statOptions)} or 'Q'): ")
			statIndex = input()

			# If they choose something longer than 1 character:
			if len(statIndex) != 1:
				delay_readout(f"\n\nSire I require one character: a number from 1 to {len(statOptions)} or a 'Q'.\n\n")
				sleep(2.0)
				continue
			
			# If they only enter in 1 character:
			else:
				# If Q is selected, have to make sure the allowance is 0
				if statIndex.lower() == 'q' and allowance == 0:
					
					# Loop until a proficiency is chosen (Proficiency While Loop)
					while True:
						delay_readout(f"\nNow just select the stat you wish to be proficienct in (1-{len(statOptions)} or 0 for random): ")
						try:
							prof = int(input())

						# If they don't choose a number:
						except ValueError:
							delay_readout("\nSire, only a number will do here. Please stop dragging this out, I have a family you know.\n")
							sleep(2.0)
							continue

						# if the number is 0, a random stat will be chosen
						if prof == 0:
							stats['prof'] = statOptions[randint(0, len(statOptions)-1)]
							delay_readout(f"\nSince you chose 0, Master {name} I picked a stat at random for you. How does {stats['prof']} sound as a proficiency (y/n)?: ")
							answerProf = input()

							# REPEATED/COPIED CODE INSERTED HERE - This code was originally written first at line 440 (36 lines down) and was reused here
							# If they type too many characters:
							if len(answerProf) != 1:
								delay_readout(f"\nMaster {name}, you really can't read, can you?\nThis has to be the 4th time you've come across a (y/n) prompt...\n")
								sleep(2.0)
								delay_readout("*SIGH*...Guess we'll try this again. Might as well let you rethink your proficiency choice as well, you may have selected it by mistake.\n")
								sleep(2.0)
								# "continue" from here should loop back to the top of the Proficiency While Loop
								continue
							
							# If they confirm their choice of proficiency
							else:
								if answerProf.lower() == 'y':
									delay_readout(f"\nLooks like you're all done here, Master {name}.")
									sleep(1.5)
									# break will exit out of Proficiency While Loop. Will need another break to exit Selection While Loop
									break

								# If anything besides 'y' is typed, it will be taken as a 'n'
								else:
									delay_readout("\nYou're right, that won't do. Let's try picking another stat for your proficiency bonus, Sire.\n")
									sleep(1.5)
									continue

						# If a number is chosen, but it's outside the range of the options:
						elif prof not in range(1, len(statOptions)+1):
							delay_readout(f"\nYou must choose a number from 1 to {len(statOptions)} Sire. There are no stat options for {prof}...\n")
							sleep(2.0)
							continue
						
						# If they choose a correct number corresponding to a stat:
						else:
							stats['prof'] = statOptions[prof-1]
							delay_readout(f"\nYou have selected the {statOptions[prof-1]} proficiency. Is this alright, Sire? (y/n): ")
							answerProf = input()
							
							# If they type too many characters:
							if len(answerProf) != 1:
								delay_readout(f"\nMaster {name}, you really can't read, can you?\nThis has to be the 4th time you've come across a (y/n) prompt...\n")
								sleep(2.0)
								delay_readout("*SIGH*...Guess we'll try this again. Might as well let you rethink your proficiency choice as well, you may have selected it by mistake.\n")
								sleep(2.0)
								# "continue" from here should loop back to the top of the Proficiency While Loop
								continue
							
							# If they confirm their choice of proficiency
							else:
								if answerProf.lower() == 'y':
									delay_readout(f"\nLooks like you're all done here, Master {name}.")
									sleep(1.5)
									# break will exit out of Proficiency While Loop. Will need another break to exit Selection While Loop
									break

								# If anything besides 'y' is typed, it will be taken as a 'n'
								else:
									delay_readout("\nYou're right, that won't do. Let's try picking another stat for your proficiency bonus, Sire.\n")
									sleep(1.5)
									continue

				# If Q is selected but there's still points unspent:
				elif statIndex.lower() == 'q' and allowance > 0:
					delay_readout(f"\nMaster {name}, these points were given to you by the gods. Please don't make them angry by wasting them.")
					sleep(2.0)
					continue

				# Added to avoid getting a ValueError for statIndex
				if statIndex.lower() == 'q' and allowance == 0:
					break
				# Try to convert statIndex to an int before it is used in the following elif statement
				try:
					statIndex = int(statIndex)
				except ValueError:
					delay_readout(f"\nMaster {name}, please just stick to a number from 1 to {len(statOptions)} or a 'Q'. All other characters are invalid.")
					sleep(1.5)
					continue
				#	When Q is not chosen: 
				# If the choice is not between 1 and 6:
				if statIndex not in range(1,len(statOptions)+1):
					delay_readout("\nSire, do you know how values and numbers work? I have my doubts...\nLet's take it from the top then.")
					sleep(2.0)
					continue
				else:

					# Increase/Decrease Stats While Loop
					while True:
						delay_readout(f"\n\n{statOptions[statIndex-1]} -\tHow much will you increase/decrease it by?: ")
						try:
							value = int(input())
						except ValueError:
							delay_readout(f"\nMaster {name}, I require a BLOODY INTEGER!! How does one increase or decrease a stat by that anyway?")
							sleep(2.0)
							continue

						score = stats[statOptions[statIndex-1]]
						if score + value < 1 or score + value > 20:
							delay_readout(f"\nSire, the values for stats can only be from 1 to 20.")
							sleep(2.0)
							continue
						if value > allowance:
							delay_readout("\nSire, the gods only gave you so many points. Please don't be greedy.")
							sleep(2.0)
							continue

						# Update the allowance variable
						allowance -= value
						# Update the stats values
						stats[statOptions[statIndex-1]] += value
						delay_readout("\nUpdating...\n")
						sleep(1.5)
						delay_readout("Updating...")
						sleep(1.5)
						delay_readout("Done!\n")
						sleep(1.5)
						break
			try:
				if answerProf.lower() == 'y':
					break
			except:
				continue
		return stats


	# Types of Stats
	statOptions = ["STR", "DEX", "CONS", "INT", "WIS", "CHR"]

	
	playerChoices = []

	# Player 1 Name Loop
	while True:
		clear()
		delay_readout("\nPlease enter your name, Sire: ")
		name = input()

		# Player 1 Name Confirmation Loop
		while True:
			delay_readout("\nSo...you wish to be called " + name + "? (y/n): ")
			answerNameOne = input()
			if len(answerNameOne) != 1:
				delay_readout("\nSire, type just a single character.\n\n'Y' will allow us to continue, any other character will make me think you had a stroke looking for the 'N'\n")
				sleep(3.0)
				clear()
				continue
			else:
				if answerNameOne.lower() == 'y':
					delay_readout(f"\nMaster {name}. A perfectly normal name for a medieval person such as yourself...\n")
					sleep(1.5)
					break
				else:
					delay_readout("\nOh...alright, let's try that again.")
					sleep(1.5)
					break
		# redundant check to break out of the main While Loop (caused by having 2 different conditions break out of the same While Loop)
		if answerNameOne.lower() == 'y':
			break

	sleep(0.5)

	# Stats for Player 1 - Choice to customize or to get default stats & proficiency
	while True:
		clear()
		delay_readout(f"Master {name}, this would be an excellent opportunity to choose some stats of your own, wouldn't you agree? (y/n): ")
		answerStats = input()
		if len(answerStats) != 1:
			delay_readout("\nI know you're excited, but please just stick to 'y' or 'n', Sire.\n")
			sleep(1.5)
			continue
		else:
			if answerStats.lower() == 'y':
				sleep(0.5)
				clear()
				statsPlayerOne = chooseStats(name)
				playerOne = Player(name, 50, 6, statsPlayerOne['STR'], statsPlayerOne['DEX'], statsPlayerOne['CONS'], statsPlayerOne['INT'], statsPlayerOne['WIS'], statsPlayerOne['CHR'], statsPlayerOne['prof'])
				playerChoices.append(playerOne)
				break
			else:
				# variable for random proficiency
				randomProf = randint(0, len(statOptions)-1)
				delay_readout(f"\nI will just go ahead and give you some default stats, Sire. How does a proficiency in {statOptions[randomProf]} sound?\n")
				sleep(1.0)
				delay_readout("Well you're stuck with it whether you like it or not :/ #SowwieeeNotSowwieee\n")
				sleep(2.0)
				playerOne = Player(name, 50, 6, 12, 12, 6, 12, 20, 6, statOptions[randomProf])
				playerChoices.append(playerOne)
				break
		break

	# Player 2 Name While Loop - Stats will be automatically assigned to Player 2 --> Might update in future version
	while True:
		clear()
		delay_readout("\n\nYour friend there...")
		sleep(1.0)
		delay_readout("they are your friend, correct?\n\nWhat do they wish to be called?: ")
		nameTwo = input()
		delay_readout(f"\nSo they're named...{nameTwo}? (y/n): ")
		answerNameTwo = input()
		if len(answerNameTwo) == 1:
			if answerNameTwo.lower() == 'y':
				delay_readout("\nAh, I see...Another perfectly normal name for a medieval person...")
				sleep(2.0)
				break
			else:
				delay_readout("\nHmmm....")
				sleep(3.0)
				continue
		else:
			delay_readout("\nPlease just use a single character for your answer Sire. Anything other than 'y' will be deemed as an 'n'.\n")
			sleep(1.5)
			continue
		break
		# if answerNameTwo.lower() == 'y':
		# 	break

	# Player 2 Stats
	# variable for random proficiency
	randomProf2 = randint(0, len(statOptions)-1)
	playerTwo = Player(nameTwo, 50, 6, 10, 12, 8, 6, 12, 20, statOptions[randomProf2])
	playerChoices.append(playerTwo)

	playerNames = [name, nameTwo]

	# Game will loop from here. Stats are locked in
	while True:
		# Player Choice While Loop
		while True:
			clear()
			for i, x in enumerate(playerNames, start = 1):
				delay_readout(f"\n{i}. {x}")

			delay_readout(f"\n\nChoose your player (1-{len(playerNames)}; 0 for random): ")
			try:
				playerIndex = int(input())
			except ValueError:
				delay_readout(f"\nYou have made a mistake, Sire. I will not be accepting anything that is not a number from 0 to {len(playerNames)}")
				sleep(1.5)
				continue
			if playerIndex == 0:
				playerIndex = randint(1,len(playerNames))
				delay_readout(f"\nSince you couldn't decide, Sire, I just went with {playerNames[playerIndex-1]}.")
				sleep(1.0)
				break
			elif playerIndex in range(1, len(playerNames) + 1):
				delay_readout(f"\n\nLooks like it'll be Master {playerNames[playerIndex-1]}!\n")
				sleep(1.0)
				break
			else:
				delay_readout(f"\n...Sire, it's clear to me that reading is not your strongest ability. Please select a number from 0 to {len(playerNames)}.\n")
				sleep(1.5)

		player = playerChoices[playerIndex-1]

		
		# Stat Choice While Loop
		while True:
			clear()
			for i, x in enumerate(statOptions, start = 1):
				delay_readout(f"\n{i}. {x}")

			delay_readout(f"\n\nPlease choose which stat you will roll for, Sire (1-{len(statOptions)}; 0 for random): ")
			try:
				statRoll = int(input())
			except ValueError:
				delay_readout(f"\nSire, only INTEGERS from 0 to {len(statOptions)} will be accepted...")
				sleep(1.5)
				delay_readout("INTEGERS!!!!")
				sleep(2.5)
				delay_readout("...Sorry about all that. Let's try that again.\n")
				sleep(1.5)
				continue
			# If 0 is input, a random stat will be chosen
			if statRoll == 0:
				statChosen = statOptions[randint(0,len(statOptions)-1)]
				delay_readout(f"\n\nThe random stat chosen for you is {statChosen}. Best of luck, Sire.")
				sleep(1.5)
				break
			elif statRoll in range(1, len(statOptions) + 1):
				delay_readout("\n\nHomestretch now, Sire...\n")
				sleep(1.0)
				break
			else:
				delay_readout(f"\nSire, you must pick a number from 0 to {len(statOptions)}")
				sleep(1.0)

		statChosen = statOptions[statRoll-1]

		# Types of Dice Rolls
		rollChoices = ["Normal roll", "Roll with advantage"]

		# Roll Choice While Loop
		while True:
			clear()
			for i, x in enumerate(rollChoices, start = 1):
				delay_readout(f"\n{i}. {x}")

			delay_readout(f"\n\nPlease choose what type of roll you want to use (1-{len(rollChoices)}; 0 for random): ")
			try:
				rollIndex = int(input())
			except ValueError:
				delay_readout("...Seriously?")
				sleep(2.0)
				continue
			# User chose a valid option:
			if rollIndex in range(1, len(rollChoices) + 1):
				# Class Player() method call for one of the Dice Roll Functions
				if rollIndex == 1:
					# getattr(Obj, Attr) will return the value of Attr found stored within the Obj. EX) Obj(Attr = 4, otherAttr = '0') --> getattr(Obj, otherAttr) would return '0'
					# diceRoll takes an int and a str as arguments. We need the int associated with the stat in our player object.
					# Since we named the variables of the player object the same as the stats options, we can use statChosen for both:
					player.diceRoll(getattr(player, statChosen), statChosen)
				else:
					player.dropLowestRoll(getattr(player, statChosen), statChosen)
				break
			# User chose Random:
			elif rollIndex == 0:
				randomRoll = randint(0,1)
				delay_readout(f"\nSince you don't like making your own decisions, I chose: {rollChoices[randomRoll]}.\n\nHeavens forbid someone asks you what you want to eat for dinner.\n")
				sleep(1.5)
				if randomRoll == 0:
					player.diceRoll(getattr(player, statChosen), statChosen)
				else:
					player.dropLowestRoll(getattr(player, statChosen), statChosen)
				break
			# User input some bogus value that was a number (negative, decimal, etc)
			else:
				delay_readout("\n*Sigh*...")
				sleep(1.5)
				delay_readout(f"\nPlease enter a valid choice, Master {player.name}")
				sleep(1.5)


		delay_readout("\nThat was fun!\n\n")

		while True:
			delay_readout("Want to play again? You can even pick another player or stat this time (y/n): ")
			answerPlayAgain = input()
			if len(answerPlayAgain) > 1:
				delay_readout("\n\nI thought we were past this? You know what to do by this point.\n\n")
				sleep(2.0)
				continue
			elif len(answerPlayAgain) < 1:
				delay_readout("\n\nPlease enter something, I can't decide based on that answer.\n\n")
				sleep(1.5)
				continue
			else:
				if answerPlayAgain.lower() == 'y':
					break
				else:
					delay_readout("\n\nGoodbye, come play again!\n\n")
					sleep(2.5)
					sys.exit()
