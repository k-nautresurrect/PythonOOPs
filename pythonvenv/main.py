# everything in python is an object
x = 9
print(type(x)) # class int

# there is also an class of object
a = object
print(a)

print(isinstance(x,object)) # everything in python is object

print(isinstance(__name__,object))

# every object has a flag wether the objects are callable or not
# iscallable -> function | execute the code, class | makes an instance 

# only object of instance A
class A:
	pass
a = A
print(a);
print(id(a)); # the id of a
print(hex(id(a))) # the actual adress of the instance

# instance of instance of the object A
b = A()
print(b);
print(id(b));
print(hex(id(b)));


# For any class
class Greetings:
	def say_hi(self):
		print("hey there")

hey = Greetings()
hey.say_hi(); # by default self is passing

'''
	self works to determine the particular instance
	and initialising for that instance only
'''

# python specific
class Specific:
	# attribute can be defined while processing
	'''
		init is not a constructor
		it is somewhat like side effect of the class
	'''
	def __init__(self, name):
		self.name = name
	
	def greet(self):
		print('hey there', self.name)


sp = Specific('kushagra')
sp.greet()

# this is somewhat like static class
Specific('kush').greet()

'''
	init is dunders or magic
	dunders => provides us some hooks or interface 
	to implement the individual functionalities

	lifecycle of object ->
		1. Created
		2. Process
		3. Deleted
	
	python has created list for all the events
	and for every event python has assigned dunders

	every dunder starts with '__' and ends with '__'
	-> __init__(self) => it is called whenever a object has creating event
	-> __del__(self) => called when object is deleted
	-> __add__(self, other) => add the objects of same class
	-> __str__(self) => turns the object to string [str(a) => a.__str__(self)]
'''

# implementing dunders
class Car:
	def __init__(self, model, mileage):
		self.model = model
		self.mileage = mileage

	def __str__(self):
		return "{} {}".format(self.model, self.mileage)

	def __repr__(self):
		return "{}".format(self.model)

	def __eq__(self, other):
		return self.mileage == other.mileage

	def __add__(self, other):
		return self.mileage + other.mileage

toyota = Car('altis', 20)
kia = Car('seltos', 30)

print(kia + toyota)
print(kia==toyota)
print(repr(toyota))
print(str(kia))

# for c++ output --> cout << "string";

class outStream:
	def __lshift__(self, other):
		print(other, end = '')
		return self

cout = outStream()

cout << "hey there" << " " << "this comes from python" << "\n";

# dunders affect not only on classes but whole phython objects

# class variable and instance variable

class Dog:
	breed = 'street' # class variable

	# skills = []
	def __init__(self, name):
		self.name = name
		self.skills = []

	def setSkill(self, skill):
		self.skills.append(skill)


d2 = Dog('jakson')
d2.breed = 'labera' # changing for the instance d2
print(d2.breed)
print(d2.name)
d2.setSkill('barks')
d2.setSkill('catch')
print(d2.skills) # changed for the class variable when self is not given
# and self cannot be used because it is like an instance variable
d = Dog('donald')
print(d.breed)
print(d.name)
print(d.skills)


# inheritance in python

# python only supports overriding 
class SchoolMembers:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print(f"initialized SchoolMember : {self.name}, {self.age}")

	def tell(self):
		print(f"name: {self.name}, age: {self.age}")

def Teacher(SchoolMembers):
	def __init__(self, name, age, salary):
		SchoolMembers.__init__(self, name, age)
		self.salary = salary
		print(f"initialized Teacher : {self.name}")

	def tell(self):
		SchoolMembers.tell(self)
		print(f"salary: {self.salary}")

def Student(SchoolMembers):
	def __init__(self, name, age, marks):
		SchoolMembers.__init__(self, name, age)
		self.marks = marks
		print(f"initialized Student : {self.name}")

	def tell(self):
		SchoolMembers.tell(self)
		print(f"marks: {self.marks}")


t1 = Teacher('rohit', 24, 3000)
s1 = Student('rakesh', 16, 89)
print(type(rohit))
