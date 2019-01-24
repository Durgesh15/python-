import threading
import datetime

exitFlag=0

class myThread(threading.Thread):
	def __init__(self,name,counter):
		threading.Thread.__init__(self)
		self.threadID=counter
		self.counter=counter
		self.name=name

	def run(self):
		print("starting"+self.name)
		#acquiring threadLock
		threadLock.acquire()
		print_date(self.name,self.counter)
		#releasing lock
		threadLock.release()
		print("exiting:"+self.name)

	def print_date(threadName,counter):
		print("program enters in print_date method")
		datefields=[]
		today=datetime.date.today()
		datefields.append(today)
		print("%s[%d] %s"% (threadName,counter,datefields[0]))

threadLock=threading.Lock()
threads=[]

#creating a thread
thread1=myThread("Thread",1)
thread2=myThread("Thread",2)

#starting a thread
thread1.start()
thread2.start()

#adding thread in threads
threads.append(thread1)
threads.append(thread2)

#to join threads
for t in threads:
	t.join()

print("Ending the program")
