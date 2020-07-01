import socket as s

class ServidorUDP:
    __socketServidor: s
    __ip: str
    __port: int
    __addr = None
    salir: bool
    __pktCount: int

    def __init__(self):
        self.__socketServidor = s.socket(s.AF_INET, s.SOCK_DGRAM)
        print('Se ha creado el socket del servidor')
        self.__ip = ''
        self.__port = 12345
        self.__socketServidor.bind((self.__ip, self.__port))
        print(f'El socket del servidor esta atado a la direccion ip {self.__ip} y el puerto {self.__port}')
        self.salir = False
        self.__pktCount = 0
        print('Esperando paquetes')


    def escribirMensaje(self, mensaje: str, direccion):
        direccion = self.__addr
        self.__socketServidor.sendto(mensaje.encode(), direccion)


    def leerMensaje(self):
        data, self.__addr = self.__socketServidor.recvfrom(1024)
        self.__pktCount += 1
        print(f'[{self.__pktCount}] Recibi un mensaje: {data} de {self.__addr}')


if __name__ == '__main__':
    sudp = ServidorUDP()
    mensaje = 'Mensaje recibido!'
    ip = '127.0.0.1'
    puerto = 12345
    direccion = ip, puerto

    while not sudp.salir:
        sudp.leerMensaje()
        sudp.escribirMensaje(mensaje, direccion)