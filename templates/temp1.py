from string import Template
student=[('ram',90),('shyam',100),('mohan',110)]
t=Template('hey $name, u have got $marks marks')
for i in student:
	print(t.substitute(name=i[0],marks=i[1]))
