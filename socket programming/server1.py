import socket
import time

def main():
	host="127.0.0.1"
	port=5001

	mySocket=socket.socket()
	mySocket.bind((host,port))
	mySocket.listen(1)

	conn,adr=mySocket.accept()
	print("connection is done on"+str(adr))

	while True:
		data=conn.recv(1024).decode()
		if not data:
			break
		print("from connect to user:"+str(data))
			

		data=str(data).upper()
		print("recieve from user:"+str(data))

		data=input("?")
		conn.send(data.encode())

	conn.close()

if __name__=='__main__':
	main()

