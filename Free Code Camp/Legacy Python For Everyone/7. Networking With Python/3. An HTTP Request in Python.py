import socket
# creates a socket but does not associate it
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.1\n\n'.encode()
mysock.send(cmd)

while True:
    # we are going to receive 512 characters at a time
    data = mysock.recv(512)
    # check if we didn't get any data
    if len(data) < 1:
        break
    #print the data that we get
    print(data.decode())
mysock.close()