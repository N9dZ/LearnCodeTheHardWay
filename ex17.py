# import two modules
from sys import argv
from os.path import exists
# set three variables
script, from_file, to_file = argv
# print the info for copying
print "Copying from %s to %s..." % (from_file,to_file)

# we could do these two on one line to, how?
#in_file = open(from_file)
#indata = in_file.read()
# Am I right?
#indata = open(from_file).read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exists? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#out_file = open(to_file, 'w')

# =$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=$=
# I can do it in only one line! Perfect! Nice! GJ!
open(to_file, 'w').write(open(from_file).read())

print "All done! Good job!"