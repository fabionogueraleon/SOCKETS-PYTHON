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
#	     SERVIDOR	 	#
#				#
#################################

import socket,select,time
from os import curdir, sep

try:
	HOST1 = ''                
	PORT1 = 1234              
	tempe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tempe.bind((HOST1, PORT1))
	tempe.listen(1)

	HOST2 = ''                
	PORT2 = 2345              
	decib = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	decib.bind((HOST2, PORT2))
	decib.listen(1)

	HOST3 = ''                
	PORT3 = 3456              
	lumi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	lumi.bind((HOST3, PORT3))
	lumi.listen(1)


	HOST4 = '127.0.0.1'                
	PORT4 = 8080
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.bind((HOST4, PORT4))
	serverSocket.listen(1);
	
	inputs =[tempe,decib,lumi,serverSocket]
	
	temperatura = 0
	decibeles = 0
	luminosidad = 0

	while True:
		(read, write, exc) =  select.select(inputs,[],[])
		for s in read:
			if s == tempe:
				conn, addr = s.accept()
				temperatura = conn.recv(1024)
				print "Dato recibido del sensor de Tempertura = "+temperatura+" [C]"
				conn.sendall(temperatura)
			elif s == decib:
				conn, addr = s.accept()
				decibeles = conn.recv(1024)
				print "Dato recibido del sensor de Intensidad Sonora =  "+decibeles+" [dB]"
				conn.sendall(decibeles)
			elif s == lumi:
				conn, addr = s.accept()
				luminosidad = conn.recv(1024)
				print "Dato recibido del sensor de Luminosidad = "+luminosidad+" [lux]"
				conn.sendall(luminosidad)
			elif s == serverSocket:
					print 'Servidor en linea, Ctrl+C para salir'
					connectionSocket, addr = serverSocket.accept()
					try:	
						path = "index.html"
						f = open(curdir + sep + path)
	    					outputdata = f.read()
						date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
						connectionSocket.send(outputdata.replace("temperatura","%s [&degC]"%(temperatura)).replace("decibeles","%s [dB]"%(decibeles)).replace("luminosidad","%s [lux]"%(luminosidad)).replace("fecha","%s"%(date)))
						connectionSocket.close()
					except IOError:
						connectionSocket.send('ERROR - 404 File not found\n') 
						connectionSocket.shutdown(1)						
						connectionSocket.close()
			else: 
				print "Servidor no detectado"
				continue
except (KeyboardInterrupt, SystemExit):
	print '  Ctrl+C recibido, apagando servidor'	
	serverSocket.shutdown(1)
	serverSocket.close()
