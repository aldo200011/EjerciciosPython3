import socket as s
import time

class ClienteTCP():
    cliente: s
    salir: bool

    def __init__(self):
        self.cliente = s.socket()
        self.cliente.connect(('127.0.0.1', 35491))
        print(f'Conectado al servidor')
        self.salir = False


    def escribirMensaje(self, mensaje: str):
        bytes = mensaje.encode()
        self.cliente.send(bytes)


    def leerMensaje(self):
        data = self.cliente.recv(1024)
        print(f'Recibido: {data}')
        time.sleep(2)


if __name__ == '__main__':
    ctcp = ClienteTCP()

    while not ctcp.salir:
        ctcp.escribirMensaje('Mensaje de cliente TCP')
        ctcp.leerMensaje()

    ctcp.cliente.close()