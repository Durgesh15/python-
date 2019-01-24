class Employee:
	no_of_emp=0
	raise_amount=1.04

	def __init__(self,fname,lname,pay):
		self.fname=fname
		self.lname=lname
		self.pay=pay
		self.email=fname+'.'+lname+'@gmail.com'
		self.no_of_emp+=1

	def fullname(self):
		return '{} {}'.format(self.fname,self.lname)

	def apply_raise(self):
		self.pay=int(self.pay*self.raise_amount)
		return self.pay

	def __repr__(self):
		return "Employee('{}' '{}' '{}')".format(self.fname,self.lname,self.pay)

	def __add__(self,other):
		return self.pay+other.pay


emp1=Employee('durgesh','gupta',10000)
emp2=Employee('saurabh','tiwari',10000)
emp3=Employee('azmat','ami',10000)

emp1.raise_amount=1.05	

#print(Employee.raise_amount)

#print(emp1.raise_amount)

#print(emp2.raise_amount)

#print(emp3.fullname())

#print(Employee.no_of_emp)

#print(emp2.email)

#print(emp1.apply_raise())

print(repr(emp1))

print(emp1+emp2)