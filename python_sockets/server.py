import socket

def server():
	port = 5000
	host = socket.gethostname()

	server_socket = socket.socket()
	server_socket.bind((host, port))
	print(host)

	server_socket.listen(3)
	conn, address = server_socket.accept()
	print("Connected from: " + str(address))
	while True:
		data = conn.recv(1024).decode()
		if not data:
			# there is no data
			break
		print("from user:" + str(data))
		data = input("-> ")
		
		# send to the client
		conn.send(data.encode()) 
	conn.close()

if __name__ == "__main__":
	server()