# define three variables and value them.
people = 30
cars = 40
buses = 15
# if cars are more than people
if cars > people:
	# then print this sentence
	print "We should take the cars."
# if cars are less than people
elif cars < people:
	# print this sentence
	print "We should not take the cars."
# otherwise
else:
	# print this sentence
	print "We can't decide."
# if buses are more than cars
if buses > cars:
	print "Too many buses."
# if buses are less than cars
elif buses < cars:
	print "Maybe we could take the buses."
# if buses are equal to cars
else:
	print "We still can't decide."
# if people are more than buses
if people > buses:
	print "Alright, let's just take the buses."
# if peoply are less than or equal to buses
else:
	print "Fine, let's stay home then."