print('importing my_module')

test='test_index'

def find_index(to_search,target):
	'"find value from index"'
	for i,value in enumerate(to_search):
		if value==target:
			return 1
		else:
			return -1