# define some variables, and assign them values
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
# use '-' for calculating, assign it to cars_not_driven
cars_not_driven = cars - drivers
cars_driven = drivers
# use "*" for calculating, assign it to carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# use "/" for calculating, assign it to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# print sentences with commas through variables
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."