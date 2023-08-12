#program of multiple, Multilevel and Hierarchical Inheritances.

# multiple inheritance
# Base class1
class train1:
	train1name = ""

	def train(self):
		print(self.train1name)
# Base class2
class train2:
	train2name = ""

	def train(self):
		print(self.train2name)
# Derived class
class train3(train1, train2):
	def trains(self):
		print("train1 :", self.train1name)
		print("train2 :", self.train2name)
s1 = train3()
s1.train1name = "express"
s1.train2name = "passenger"
s1.trains()


# multilevel inheritance
# Base class
class train1:
	def __init__(self, train1name):
		self.train1name = train1name

# Intermediate class
class train2(train1):
	def __init__(self, train2name, train1name):
		self.train2name = train2name
		train1.__init__(self, train1name)

# Derived class
class train3(train2):
	def __init__(self, train3name, train2name, train1name):
		self.train3name = train3name
		train2.__init__(self, train2name, train1name)
	def print_name(self):
		print('train1 name :', self.train1name)
		print("train2 name :", self.train2name)
		print("train3 name :", self.train3name)
s1 = train3('express', 'passenger', 'bullet')
s1.print_name()


# Hierarchical inheritance
# Base class
class train:
	def fun1(self):
		print("This is parent class.")
# Derived class1
class train1(train):
	def fun2(self):
		print("This is child 1.")
# Derivied class2
class train2(train):
	def fun3(self):
		print("This is child 2.")
obj1 = train1()
obj2 = train2()
obj1.fun1()
obj1.fun2()
obj2.fun1()
obj2.fun3()


""" OUTPUT:
train1 : express
train2 : passenger
train1 name : bullet
train2 name : passenger
train3 name : express
This is parent class.
This is child 1.
This is parent class.
This is child 2. """