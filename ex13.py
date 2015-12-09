# Import a module when you use it,
# Let readers know what modules this program has
# argv means "argument variable"
from sys import argv
# Unpack argv, and assign all the parameters with 
# the names on the left.
script, first, second, third = argv

print "The script is called:", script
print "The first is called:", first
print "The second is called:", second
print "The third is called:", third