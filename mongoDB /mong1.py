from pymongo import MongoClient
#connect to mongoDb
conn=MongoClient('localhost',27017)

#acces  the testdb database and the emp collection
db=conn.testdb.emp

#create dictionary
emp_rec={}

#set flag variable
flag=True

#loop for data input
while(flag):
	#ask for input
	emp_name,emp_addr,emp_id=input("enter emp_name,address and id:").split()

	#place value in dictionary
	emp_rec={'name':emp_name,'address':emp_addr,'id':emp_id}

	#insert the record
	db.insert(emp_rec)
	print('one record is inserted!!!!!!!!!')

	#ask from user if he wants to continue to insert
	flag=input('Enter another record?')
	if(flag[0].upper()=='N'):
		flag==False

	#find all documents
	ret=db.find()

	print()
	print('+++++++++++++++')

	#display documents from collections
for rec in ret:
	print('program in for loop')
	print(rec['name']+','+rec['address']+','+rec[id])

print('program is done!!!!!')

#close the conn to MongoDB
conn.close()