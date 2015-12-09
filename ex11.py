# raise a question
print "How old are you?",
# get the users' answer
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weigh = raw_input()
# print the result in one sentence
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weigh)