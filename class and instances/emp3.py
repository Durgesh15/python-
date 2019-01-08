class Employee:
	no_of_emp=0
	raise_amount=1.04
	def __init__(self,fname,lname,pay):
		self.fname=fname
		self.lname=lname
		self.pay=pay
		self.email=fname+'.'+lname+'@gmail.com'
		Employee.no_of_emp+=1

	def fullname(self):
		return '{} {}'.format(self.fname,self.lname)

	def apply_raise(self):
		 self.pay=int(self.pay*emp_2.raise_amount)

emp_1=Employee('durgesh','gupta',10000)
emp_2=Employee('saurabh','tiwari',10000)

emp_1.raise_amount=1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_2.pay)
print(Employee.no_of_emp)



