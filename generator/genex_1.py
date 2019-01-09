#this program doesnt finding mem_profile package
import mem_profile
import random
import time

names=['durgesh','saurabh','aditya','shyam','azmat','riyaz']
major=['developer','developer','sen_developer','sen_developer','developer','developer']

print('Memory(before):{}Mb'.format(mem_profile.memory_usage_resource()))

def people_list(num_people):
	result=[]
	for i in range(num_people):
		person={'id':i,'name':random.choice(names),'major':random.choice(major)}
		result.append(person)
	return result

def people_generator(num_people):
	for i in range(num_people):
		person={'id':i,'name':random.choice(names),'major':random.choice(major)}
		yield person
t1=time.clock()
people=people_list(100000)
t2=time.clock()

#t1=time.clock()
#people=people_generator(100000)
#t2=time.clock()

print('Memory(after):{}Mb'.format(mem_profile.memory_usage_resource()))
print('Took {} seconds'.format(t2-t1))