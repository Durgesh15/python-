class Employee:

	def __init__(self,fname,lname,pay):
		self.fname=fname
		self.lname=lname
		self.pay=pay
		self.email=fname+'.'+lname+'@gmail.com'

	def fullname(self):
		return '{} {}'.format(self.fname,self.lname)
emp_1=Employee('durgesh','gupta',10000)
emp_2=Employee('saurabh','sharma',10000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
#this upper statement transfered in below

print(Employee.fullname(emp_1))