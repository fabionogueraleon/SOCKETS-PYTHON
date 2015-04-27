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
#	Liminosidad [lux]	#
#	Rango 0 a 400 lux	#
#				#
#################################
import socket
import random
import math

HOST = 'localhost'
PORT = 3456             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
lumi=math.floor(200+(random.random()-0.5)*200)
s.sendall(repr(lumi))
data = s.recv(1024)
s.close()
print "Dato Recibido: Luminosidad= " + data + " [lux]"

