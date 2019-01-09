with open('app3.log','w',encoding='utf-8') as f:
	f.write('this is my second program\n')
	f.write('this file contains some data\n')
	f.write('lets see\n')

with open('app3.log','r',encoding='utf-8')as f:
	content=f.read(10)
	content1=f.read(3)
	content2=f.read()

	print(content)
	print(content1)
	print(content2)