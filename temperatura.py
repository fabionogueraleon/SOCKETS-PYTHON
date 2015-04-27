#################################
#				#
#	MISE - UPM		#
#	LSE - PRACTICA 4	#
#	SOCKETS PYTHON		#
#				#
#	FABIO NOGUERA LEON	#
#	CARLOS ANTONIO ORREGO	#
#				#
#################################
#				#
#	Temperatura [C]		#
#	Rango 0 a 40 [C]	#
#				#
#################################
import socket
import random
import math

HOST = 'localhost'
PORT = 1234             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
tempe=math.floor(20+(random.random()-0.5)*20)
s.sendall(repr(tempe))
data = s.recv(1024)
s.close()
print "Dato Recibido: Temperatura= "+ data +"[C]"


