# import modules
from sys import exit
# room with gold
def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
	# the number inputed should have 0 or 1
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")
	# the number should be less than 50
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
# room with a bear
def bear_room():
	print """
	There's a bear here.
	The bear is in front of another door.
	How are you going to remove the bear?
	"""
	# bear is here at the first
	bear_moved = False
	# always loop
	while True:
		next = raw_input("> ")
		# take honey, go dead
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		# you taunt bear when it's here, move on, next
		elif next =="taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		# you taunt bear when it's not here, go dead
		elif next =="taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		# open door when the bear is away, get into the gold room
		elif next =="open door" and bear_moved:
			gold_room()
		# the machine can't understand you
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insane."
	print "do you 'flee' for your life or eat your 'head'?"

	next = raw_input("> ")
	# be brought to the beginning when you flee your life
	if "flee" in next:
		start()
	# eat head, go dead
	elif "head" in next:
		dead("Well that was tasty!")
	# other answers, move on until one of the two answers above
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)
# the beginning of this game
def start():
	print """
	You're in a dark room.
	There is a door to your 'right' and 'left'.
	which one do you take?
	"""

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()
