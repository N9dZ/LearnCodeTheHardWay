# import a mode
from sys import argv
# unpack argv
# and assign the parameters with the left names
script, filename = argv
# Don't write the hardcode
# Use a variable instead of the value directly
txt = open(filename)

print "Here's your file %r:" % filename
# use read() to display the content of file
print txt.read()
# close() to open()
txt.close()

# ask user to input a filename
print "Type the filename again:"
file_again = raw_input(">")
# use the name user just input, open it
txt_again = open(file_again)
# use read() to display the content of file
print txt_again.read()
# close() to open()
txt_again.close()