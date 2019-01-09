class Error1(Exception):
	pass

class InputTooSmallException(Error1)
	pass

class InputTooLargeException(Error1)
	pass

alphabet='m'

while true:

	try:
		alp=raw_input('enter a alphabet here')

		if alp<alphabet:
			raise InputTooSmallException

		elif alp>alphabet:
			raise InputTooLargeException
			break

	except InputTooSmallException:
		print("provided input is too small!!")
		print(' ')
	except InputTooLargeException:
		print("provided input is too large")
		print(' ')

		print('congratulation!you select it perfectly')
