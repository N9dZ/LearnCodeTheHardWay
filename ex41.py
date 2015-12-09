class TheTing(object):
	"""docstring for TheTing"""
	def __init__(self):
		self.number = 0
		
	def some_function(self):
		print "I got called."

	def add_me_up(self, more):
		self.number += more
		return self.number

# two different things
a = TheTing()
b = TheTing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number

# Study this. This is how you pass a variable
# from one class to another. You will need this.
class TheMultiplier(object):
	"""docstring for TheMultiplier"""
	def __init__(self, base):
		self.base = base

	def do_it(self, m):
		return m * self.base
# x is a object, it's a
x = TheMultiplier(a.number)
# run the function "do_it" in class TheMultiplier on object x
print x.do_it(b.number)

stuff = ['Test', 'This', 'Out']
print " ".join(stuff)