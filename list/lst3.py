def count_list(lst):
	ctr=0

	for i in lst:
		if len(i)>1 and lst[0]==lst[-1]:
			print("print something")
			ctr +=1

		return ctr

code=count_list(['abc', 'xyz', 'aba', '1221'])
print(code) 