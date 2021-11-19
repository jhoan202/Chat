  
import socket   
import threading

host='127.0.0.1'
puerto=5555
my_socket=socket.socket()
my_socket.bind((host,puerto))
my_socket.listen()
print("SERVIDOR EN ESCUCHA EN EL PUERTO 5555")

usuarios_conectados=[]

def recibir(conexion, ip):
	while True:
		try:
			mensaje=conexion.recv(1024).decode('utf-8')
			for i in usuarios_conectados:
				if i != conexion:
					i.send(mensaje.encode('utf-8'))
		except:
			for i in usuarios_conectados:
				if i == conexion:
					usuarios_conectados.remove(i)
					print(f"USUARIO DESCONECTADO {i}")
					i.close()
				if i !=conexion:
					i.send("ADMINISTRADOR: SE DESCONECTO UN USUARIO ANÓNIMO".encode('utf-8'))
			break

while True:
	conexion , ip = my_socket.accept()
	print(f"SE CONECTO EL USUARIO CON IP {ip}")
	usuarios_conectados.append(conexion)
	print(usuarios_conectados)
	thread=threading.Thread(target=recibir, args=(conexion,ip,))
	thread.start()