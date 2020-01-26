class Dog:


	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender
		print('(Initialized Dog:{})'.format(self.name))

	def bark(self):
		print('Name:"{}" Age:"{}" Gender:"{}"'.format(self.name,self.age,self.gender),end="")


class Shamoyed(Dog):

	def __init__(self, name, age, gender,child):
		Dog.__init__(self,name,age,gender)
		self.child = child
		print('(Initialized Dog:"{}")'.format(self.name))

	def bark(self):
		Dog.bark(self)
		print('Child:"{:d}"'.format(self.child))

class GoldenRetriver(Dog):

	def __init__(self, name, age, gender,child):
		Dog.__init__(self,name,age,gender)
		self.child = child
		print('(Initialized Dog:"{}")'.format(self.name))

	def bark(self):
		Dog.bark(self)
		print('Child:"{:d}"'.format(self.child))

class Husky(Dog):

	def __init__(self, name, age, gender,child, master):
		Dog.__init__(self,name,age, gender)
		self.child = child
		self.master = master
		print('(Initialized Dog:"{}")'.format(self.name))

	def bark(self):
		Dog.bark(self)
		print('Child:"{}" Master:"{}"'.format(self.child,self.master))


s = Shamoyed('Bo Bo' , 4 ,'Female', 4)
g = GoldenRetriver('Shaung Shaung' , 3,'Male', 1 )
h =	Husky('Ki Ki', 6,'Female', 2 , 2)

print()

dogfamily = [s, g, h]	
for dog in dogfamily:
	dog.bark()