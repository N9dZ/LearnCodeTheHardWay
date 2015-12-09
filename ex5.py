# define some variables, and assign them values
my_name = 'Ned Zhang'
my_age = 25
my_height = 192
my_weight = 89.1
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'
# print with "%s", "%d" and variables
print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)