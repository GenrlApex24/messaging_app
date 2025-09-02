#!/usr/bin/env python3

import socket
import threading

HOST = "127.0.0.1"
PORT = 65432

conns = []

with open("log.txt", "a") as f:
	f.write(f"\n\nNew Session\n")

def client_handler(conn, addr):
	with conn:
		print(f"Connected to by {addr}")

		try:
			while True:
				data = conn.recv(1024)
				decoded_data = data.decode("utf-8")

				if not data:
					break

				with open("log.txt", "a") as f:
					f.write(f"{decoded_data}\n")
				
				if decoded_data == "exit":
					conn.sendall("dis123".encode("utf-8"))
					break

				print(f"{addr}{decoded_data}")

				for c in conns:
					try:
						c.sendall(decoded_data.encode("utf-8"))
					except:
						conns.remove(c)

		except ConnectionResetError:
			print("client unexpectedly dissconected!")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Server listening on {HOST}:{PORT}")

while True:
	conn, addr = server.accept()
	conns.append(conn)
	print(conns)
	client_thread = threading.Thread(target=client_handler, args=(conn, addr))
	client_thread.start()