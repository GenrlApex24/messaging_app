#!/usr/bin/env python3

import socket
import threading

HOST = "127.0.0.1"
PORT = 65432


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

				conn.sendall(decoded_data.encode("utf-8"))
				
				if decoded_data.lower().strip() == "exit":
					conn.sendall("dis123".encode("utf-8"))
					break

				print(f"{addr}{decoded_data}")
				conn.sendall(decoded_data.encode("utf-8"))
		except ConnectionResetError:
			print("client unexpecedly dissconected!")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Server listening on {HOST}:{PORT}")

while True:
	conn, addr = server.accept()
	client_thread = threading.Thread(target=client_handler, args=(conn, addr))
	client_thread.start()