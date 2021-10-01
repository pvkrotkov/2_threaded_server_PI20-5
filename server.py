# -*- coding: utf-8 -*-
import socket, threading


def work_with_client(conn):
    while True:
        msg = ''
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
        conn.send(data)
    conn.close()


sock = socket.socket()
sock.bind(('127.0.0.1', 9091))
sock.listen(0)

while True:
    try:
        conn, addr = sock.accept()
    except:
        continue
    else:
        Thread(target=work_with_client, args=conn)
