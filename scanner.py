# -*- coding: utf-8 -*-
import socket
from threading import Thread


def scan(first, last): # сканируем порты
    for port in range(first,last): # по очереди
        sock = socket.socket() # сокет создаем
        try:
            scanned.append(port) # запоминаем, что мы просканировали порт
            sock.connect(('127.0.0.1', port)) # пытаемся присоединиться
            openned.append(port) # если получается, решаем что он открыт
        except:
            continue
        finally:
            sock.close()


def printing():
    i = 0
    while i < 65535: # по очереди проходим все возмодные порты
        if i in scanned: 
            if i in openned: #если просканирован, пишем о его состоянии
                print(f"Порт {i} открыт")
            else:
                print(f"Порт {i} закрыт")
            i += 1
        else: # если нет -- ждем сканирования
            continue


N = 2**16 - 1 # кол-во портов
openned = [] # открытые порты
scanned = [] #просканированые порты
for i in range(256): # создаем много потоков сканирования
    Thread(target=scan, args=(i*int(N/257), (i+1)*int(N/257))).start() 
Thread(target=printing).start() # создаем один поток вывода
