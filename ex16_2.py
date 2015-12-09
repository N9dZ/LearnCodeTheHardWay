# import a module
from sys import argv
# set two variables
script, filename = argv
# open a file
txt = open(filename)

print "Here's your file %r:" % filename
# use read() to get the content of file
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