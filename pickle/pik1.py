import pickle

website={'name':'google','domain':'.com','study':'KLS'}

with open('website','wb') as f:
	pickle.dump(website,f)

with open('website','rb') as f:
	data=pickle.load(f)
	print(data)