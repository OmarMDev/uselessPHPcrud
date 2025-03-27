import socket

def client():
	port = 5000
	host = socket.gethostname()

	client_socket = socket.socket()
	client_socket.connect((host, port))

	message = input("<-")

	# stop connection: bye
	while message.lower().strip() != "bye":
		client_socket.send(message.encode())
		data = client_socket.recv(1024).decode()
		print("received from server:" + str(data))
		message = input("<-")
	
	client_socket.close()

if __name__ == "__main__":
	client()
