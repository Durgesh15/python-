try:
	fob=open("test.log",'r')

	try:
		fob.write("this is not going to print")
		print("It's my test file to verify try-finally in exception handling!!")

	finally:
		print("this block always be executed!!")

except IOError:
	print("this error msg will be printed")

else:
	print("everything going good!!")
