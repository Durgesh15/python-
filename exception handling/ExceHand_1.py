try:
	fob=open("test.log","r")
	fob.write("It's my test file to verify exception handling in Python!!")

except IOError:
	print("Error: can\'t find the file or read data")

else:
	print("Write operation is performed successfully on the file")