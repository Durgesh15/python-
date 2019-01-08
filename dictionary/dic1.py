student={'name':'john','age':20,'course':['history','math']}
print(student)
print(student['name'])
student['phone']=555555
student['name']='jane'

student.update({'name':'jia','age':25})

del student['age']
age=student.pop('name')
print(student)
print(age)
	
for key,value in student.items():
	print(key,value)