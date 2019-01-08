#positional arguments
def student_info(*args,**kwargs):
	print(args)	
	print(kwargs)

courses=['Math','history']
info={'name':'john','age':22}

student_info(*courses,**info)
