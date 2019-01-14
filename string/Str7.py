def reverse_String(str):
	if len(str)%4==0:
		return ' '.join(reversed(str))
		return str

print(reverse_String('abcd'))
print(reverse_String('python'))