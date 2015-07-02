import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 80                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   msg = c.recv(1024)
   
   
   startI = msg.find("%3A")
   #print startI
   msg = msg[startI+3:startI+50]
   endI = msg.find("%3A")
   #print startI
   #print endI
   print msg[0:endI].replace("%2C",", ")
   
#GET /cc?a=dir_bic.directionbg&r=&i=&bw=1153&px=229&py=443&sx=229&sy=443&m=0&nsc=map.route&g=02360108%3A37.6628154%2C127.0424377%3AZ12%3A0.0087137%2C0.0046892&u=about%3Ablank&time=1431679993176 HTTP/1.1
   #print 'Got connection from', addr
   #c.send('Thank you for connecting')
   #c.close()                # Close the connection