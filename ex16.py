# import the module
from sys import argv
# define a variable, and assign it
script, filename = argv
# some prompt messages
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# get the response from user
raw_input("?")

print "Opening the file..."
# return a file object with mode Write
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# Delete the content of the file
target.truncate()

print "Now I'm going to ask you for three lines."
# receive the user's input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# write content into the corresponding file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()