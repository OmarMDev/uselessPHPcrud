import http.server
import ssl

def main():
	server = http.server.HTTPServer(("localhost", 443), http.server.SimpleHTTPRequestHandler)
	server.socket = ssl.wrap_socket(server.socket, certfile='./cert.pem', keyfile='./key.pem', server_side=True, ssl_version=ssl.PROTOCOL_TLS)
	server.serve_forever()
	
if __name__ == "__main__":
	main()