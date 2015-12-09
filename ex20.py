# import the module
from sys import argv
# define variables and assign them
script, input_file = argv
# read at most size bytes, returned as a string
# f represents filename
def print_all(f):
	print f.read()
# Move to the beginning position, returned none
# f represents filename
def rewind(f):
	f.seek(0)
# returned line number, next line from file as a string
# line_count represents linenumber, f represents filename
def print_a_line(line_count, f):
	print line_count,f.readline(),
# open a the input_file
current_file = open(input_file)
# some tips
print "First let's print the whole file:"
# all content of the file
print_all(current_file)
# some tips
print "Now let's rewind, kind of like a tape."
# move to the beginning position of the file
rewind(current_file)
# some tips
print "Let's print three lines:"
# print the 1st line
current_line = 1
print_a_line(current_line, current_file)
# next line, print the 2nd line
current_line += 1
print_a_line(current_line, current_file)
# next line, print the 3rd line
current_line += 1
print_a_line(current_line, current_file)