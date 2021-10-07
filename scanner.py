# -*- coding: utf-8 -*-
import socket
from threading import Thread


def scan(first, last):
    for port in range(first,last):
        sock = socket.socket()
        try:
            scanned.append(port)
            sock.connect(('127.0.0.1', port))
            openned.append(port)
        except:
            continue
        finally:
            sock.close()


def printing():
    i = 0
    while i < 65535:
        if i in scanned:
            i += 1
            if i in openned:
                print(f"Порт {i} открыт")
            else:
                print(f"Порт {i} закрыт")
        else:
            continue


N = 2**16 - 1
openned = []
scanned = []
for i in range(256):
    Thread(target=scan, args=(i*int(N/257), (i+1)*int(N/257))).start()
Thread(target=printing).start()