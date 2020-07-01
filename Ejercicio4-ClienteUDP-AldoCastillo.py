import socket as s
import time

class ClienteUDP:
    __cliente: s
    __addr = None
    salir: bool

    def __init__(self):
        self.__cliente = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.salir = False


    def escribirMensaje(self, mensaje: str, direccion):
        self.__addr = direccion
        bytes = mensaje.encode()
        self.__cliente.sendto(bytes, self.__addr)


    def leerMensaje(self):
        data, self.__addr = self.__cliente.recvfrom(1024)
        print(f'Recibido: {data} de {self.__addr}')
        time.sleep(2)


if __name__ == '__main__':
    cudp = ClienteUDP()
    mensaje = 'Mensaje de cliente UDP'
    ip = '127.0.0.1'
    puerto = 12345
    direccion = ip, puerto

    while not cudp.salir:
        cudp.escribirMensaje(mensaje, direccion)
        cudp.leerMensaje()