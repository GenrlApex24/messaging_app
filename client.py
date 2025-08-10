#!/usr/bin/env python3

import socket
import threading
import tkinter as tk

HOST = "127.0.0.1"
PORT = 65432


def recieve_data():

	while True:

		data = client.recv(1024)
		decoded_data = data.decode("utf-8")

		if decoded_data == "dis123":
			break
			exit()
		else:
			print(decoded_data)
			message_box.insert(1.0, decoded_data)


print("Welcome to my test server")
run = input("Do you want to connect to the server (y/n): ")

if run.lower().strip() == "y":
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))

	usr = input("please enter a username: ")
	client.sendall(f"made their username: {usr}".encode("utf-8"))

	root = tk.Tk()
	root.configure(background="black")	
	root.geometry("500x700")
	root.title("Message +")

	message_box = tk.Text(root, height=30, bg="White")
	message_box.pack(fill="both", padx=5, pady=5, expand=True)

	input_frame = tk.Frame(root)
	input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

	msg = tk.StringVar()
	input_box = tk.Entry(input_frame, textvariable=msg)
	input_box.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=True)

	def clicked():

		data = msg.get()
		print(data)
		client.sendall(f"{usr}: {data}".encode("utf-8"))

	
	send_button = tk.Button(input_frame, text="send", command=clicked)
	send_button.pack(side=tk.RIGHT, padx=5, pady=5)


	recieving_thread = threading.Thread(target=recieve_data)
	recieving_thread.start()


	root.mainloop()

else:
	print("So why did u bother running the client")