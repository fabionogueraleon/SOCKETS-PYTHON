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
#Decibeles [dB]
#Rango 0 a 130 [dB]
#				#
#################################
import socket
import random
import math

HOST = 'localhost'
PORT = 2345             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
decib=math.floor(65+(random.random()-0.5)*65)
s.sendall(repr(decib))
data = s.recv(1024)
s.close()
print "Dato Recibido: Decibeles= "+ data +"[dB]"

