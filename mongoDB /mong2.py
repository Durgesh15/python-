from pymongo import MongoClient

conn=MongoClient('localhost',27017)

db=conn.test.book

course=[{'author':'apj abdul kalam','book name':'wings of fire','price':100},{'author':'paulo coleho','book name':'The Alchemist','price':200}]

db.insert(course)

db.update({'book name':'The Alchemist'},{'$set':{'book name':'the first way'}},multi=False)

db.delete({'author':'paulo coleho'})

result1=db.find()
for r in result1:
   print("after change:"+str(r))