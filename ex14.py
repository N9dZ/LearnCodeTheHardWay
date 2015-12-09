# import a module for variables
from sys import argv
# define two variables
script, user_name = argv
# define and assign a variable
prompt = '> '
# use '"%s" % var_name' to output the value of variables
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
# get a value from user's input
likes = raw_input(prompt)
# ask a question
print "Where do you live %s?" % user_name
# get a value from user's input
lives = raw_input(prompt)
# questioning
print "What kind of computer do you have?"
# get the input value
computer = raw_input(prompt)
'''
Three double quotation marks makes input freely
not like line 8th, using '"%r %r" % (var_name1, var_name2)'
the number of "%r" on the left should be the same 
as var_name in the parenthesis
'''
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)