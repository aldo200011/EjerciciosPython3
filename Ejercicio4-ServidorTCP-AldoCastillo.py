import socket as s

class ServidorTCP():
    __serverSocket: s
    __ip: str
    __port: int
    salir: bool
    __pktCount: int
    clienteCon: s
    clientAddr: s
    pass

    def __init__(self):
        self.__serverSocket = s.socket()
        print('Se ha creado el socket del servidor')
        self.__ip = ''
        self.__port = 35491
        self.__serverSocket.bind((self.__ip, self.__port))
        print(f'El socket del servidor esta atado a la direccion ip {self.__ip} y el puerto {self.__port}')
        self.__serverSocket.listen()
        self.salir = False
        self.__pktCount = 0
        (self.clienteCon, self.clientAddr) = self.__serverSocket.accept()
        self.__pktCount += 1
        print('Esperando paquetes')


    def escribirMensaje(self, mensaje: str):
        self.clienteCon.send(mensaje.encode())


    def leerMensaje(self):
        data = self.clienteCon.recv(1024)
        self.__pktCount += 1
        print(f'[{self.__pktCount}] Recibi un mensaje: {data} de {self.clientAddr}')


if __name__ == '__main__':
    stcp = ServidorTCP()
    mensaje = 'Mensaje recibido!'

    while not stcp.salir:
        while True:
            stcp.leerMensaje()
            stcp.escribirMensaje(mensaje)

        print('Conexion cerrada')
        stcp.clienteCon.close()
