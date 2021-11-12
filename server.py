import socket, threading

def connect(conn, addr):
	while True:
		try:
			data = conn.recv(1024)
		except (ConnectionResetError, ConnectionAbortedError):
			print(f'Клиент {addr} Разорвал соединение')
			raise
		print(f'Клиент передал сообщение {addr}: {data.decode()}')
		conn.send(data)


sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)

while True:
	conn, addr = sock.accept()
	print(f'connected {addr}')
	threading.Thread(target = connect, args = (conn, addr), daemon = True).start()
