#sorting
def sort(*args):
	min=args[0]

for i in args[1:]:
	if i<min:
		min=i
		return min
min=sort(1,12,-1,13,15,-45)
print(min)


