#!/usr/bin/python3
# ADRIÁN PAYOL MONTERO

import socket

codigos = {'200':'OK', '404':'Not Found'}

c = 0
def contador():
    global c
    if c != 0:
        c = c - 1
    else:
        c = 5
    return c

def respuesta(codigo, body):
    resp = "HTTP/1.1" + str(codigo) + codigos[str(codigo)] + "\r\n\r\n"
    cabez1 = "<html><body><h2>"
    cabez2 = "</h2></body></html>\r\n"
    if body is not None:
        resp = resp + cabez1 + str(c) + cabez2
    return resp

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
    while True:
        print('Esperando peticiones...')
        (recvSocket, address) = mySocket.accept()
        pet = str(recvSocket.recv(2048), 'utf-8')
        rec = pet.split()[1]
        print('Peticion recibida: ' + rec)

        if rec == "/contador":
            c = contador()
            resp = respuesta(200, c)
        else:
            resp = respuesta(404, None)

        recvSocket.send(bytes(resp, "utf-8"))
        recvSocket.close()

except KeyboardInterrupt:
    mySocket.close()

