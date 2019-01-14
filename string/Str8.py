def upper_case(str):
	num_upper=0
	for i in str[:4]:
		if i.upper()==i:
			num_upper=num_upper+1
		if num_upper>=2:
			return str.upper()
			return str

print(upper_case('python'))
print(upper_case('PyThon'))