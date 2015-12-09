## Animal is a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## ??
class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name):
		## ??
		self.name = name

class Cat(Animal):
	"""docstring for Cat"""
	def __init__(self, name):
		## ??
		self.name = name

class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		## ??
		self.name = name
		## Person has a pet of some kind
		self.pet = None

## ??
class Employee(Person):
	"""docstring for Employee"""
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## object is-a Fish
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Salmon
class Halibut(Salmon):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee, named Frank, salary 120000
frank = Employee("Frank", 120000)

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()