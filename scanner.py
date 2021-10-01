# -*- coding: utf-8 -*-
import socket
from threading import Thread





def scan(first, last):
    for port in range(first,last):
        sock = socket.socket()
        try:
            print(port)
            sock.connect(('127.0.0.1', port))
            print("Порт", i, "открыт")
        except:
            continue
        finally:
            scanned.append(port)
            sock.close()
        
N = 2**16 - 1
unscanned = [i for i in range(1, N+1)]
scanned = []

for i in range(256):
    Thread(target=scan, args=(i*int(N/257), (i+1)*int(N/257))).start()
