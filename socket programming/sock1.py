import socket
import sys

try:
	soc_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

except socket.error as err_msg:
	print("socket is not initalized. error code:"+str(err_msg[0]+',error msg:'+err_msg[1]))
	sys.exit();

print('socket initalized')