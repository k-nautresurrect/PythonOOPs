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

