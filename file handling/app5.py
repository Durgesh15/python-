with open('app.log','w',encoding='utf-8')as f:
	f.write('something is changing in ths file\n')
	f.write('what it goes changes we will see later\n')

f=open('app.log','r+')
data=f.read(10)
print('read string is:',data)

data2=f.tell()
print('pointer is on:',data2)

position=f.seek(0,0)
data3=f.read(10)
print('now pointer will start reading from:',data3)

f.close()