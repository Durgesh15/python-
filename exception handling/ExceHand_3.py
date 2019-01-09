try:
	a=int(input('enter a +ve no'))

	if a<=0:
		raise ValueError('this is not a +ve no')
except ValueError as ve:
	print(ve)