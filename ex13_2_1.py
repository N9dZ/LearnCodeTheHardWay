# Import a module when you use it,
# Let readers know what modules this program has
# argv means "argument variable"
from sys import argv
# Unpack argv, and assign all the parameters with 
# the names on the left.
filename = argv
# show the filename on screen
print "The filename is called: ", filename
# assign the variables with user's input
name = raw_input("The name is called: ")
no = raw_input("The no is called: ")
age = raw_input("The age is called: ")
sex = raw_input("The sex is called: ")
height = raw_input("The height is called: ")
weight = raw_input("The weight is called: ")
# display some information
print "Your name is", name, "and your student number is", no, "."
print "You're", age, "years old.",
print "You're", sex, "."
print "You're", height, "tall.",
print "You're", weight, "heavy."

#sth = raw_input(
#	"Do you want some Supplementary Specifications?\n")
#print raw_input(
#	"Do you want some Supplementary Specifications?\n")