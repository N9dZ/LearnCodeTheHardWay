print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# there's variable for a real poem
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# print content of the poem
print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
# a function to make some calculations
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
# some calculations
start_point = 10000
beans, jars, crates = secret_formula(start_point)
# one variable for one value
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10
# use the function's return to value the results directly
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)