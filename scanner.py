# -*- coding: utf-8 -*-
import socket
from threading import Thread
from progress.bar import IncrementalBar # необходима сторонняя библиотека progress

# процесс сканирования порта
def scan(first, last): # сканируем порты
    for port in range(first,last): # сканирование производиться от первого до последнего порта (first, last)
        sock = socket.socket() # Созданаем сокет
        try:
            scanned.append(port) # Запоминаем просканированный порт и добавляем в список
            sock.connect(('127.0.0.1', port)) # пытаемся присоединиться
            openned.append(port) # если получается, решаем что он открыт
        except:
            continue
        finally:
            sock.close()

# функция печати на экран состояния порта
def printing():
    i = 0
    while i < N: # по очереди проходим все возмодные порты
        if i in scanned:
            bar.next()
            if i in openned: #если просканирован, пишем о его состоянии
                print(f"\nПорт {i} открыт")
            i += 1
        else: # если нет -- ждем сканирования
            continue


N = 2**16 - 1 # кол-во портов
openned = [] # открытые порты
scanned = [] #просканированые порты
bar = IncrementalBar('Progress', max = N)
for i in range(256): # создаем много потоков сканирования
    Thread(target=scan, args=(i*int(N/257), (i+1)*int(N/257))).start()
Thread(target=printing).start() # создаем один поток вывода
