def get_great(lst):
	max=lst[0]
	for i in lst:
		if i>max:
			max=i
			return max

code=get_great(lst=[1,2,-4,6,8])
print(code)