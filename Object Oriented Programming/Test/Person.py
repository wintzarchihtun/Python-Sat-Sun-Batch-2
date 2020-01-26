class Person:
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def say_name(self):
		print('Hello,my name is ', self.name)


	def say_age(self):
		print('I\'m ', self.age,'years old.')	

	def say_gender(self):
		print('I\'m a ',self.gender)	

p = Person('Swaroop',16,'boy')
p.say_name()
p.say_age()
p.say_gender()




(name -, age -, gender - )