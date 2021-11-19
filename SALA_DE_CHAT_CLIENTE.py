import socket   
import threading
my_socket= socket.socket()
my_socket.connect(('127.0.0.1',5555))
print("BIENVENIDOS AL CHAT ANÓNIMO DE LA UNIPAMPLONA")

def recibir_mensajes():
	while True:
		
		mensaje1=my_socket.recv(1024).decode('utf-8')
		print(mensaje1)
def enviar_mensajes():
	while True:
		
		mensaje=input()
		my_socket.send(f"-user_anonimo: {mensaje}".encode('utf-8'))

thread_recibir_mensajes=threading.Thread(target=recibir_mensajes)
thread_recibir_mensajes.start()
thread_enviar_mensajes=threading.Thread(target=enviar_mensajes)
thread_enviar_mensajes.start()