class Animal:
	def speak(self):
		print("animal is speaking")

class Dog:
	def speak(self):
		print("dog is speaking")

class Cow(Dog,Animal):		#class Cow(Animal,Dog)		#ouput will be cow is howing  
																	#  Animal is speaking
	def bark(self):
		print("cow is howing")
c=Cow()
c.bark()
c.speak()