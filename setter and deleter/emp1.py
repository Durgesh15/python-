class Employee:
	def __init__(self,fname,lname,pay):
		self.fname=fname
		self.lname=lname
		self.pay=pay

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.fname,self.lname)

	#@property
	#def fullname(self):
	#	return '{} {}'.format(self.fname,self.lname)

	@fullname.setter
	def fullname(self,name):
		fname, lname=name.split(' ')
		self.fname=fname
		self.lname=lname


emp1=Employee('durgesh','gupta',10000)

emp1.fullname='saurabh tiwari'

print(emp1.fname)
print(emp1.email)

print(emp1.fullname)