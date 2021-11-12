import socket
import re
from threading import Thread, Lock
from queue import Queue


def getIP():
    while True:
        host = input('Введите ip который будем сканировать: ')
        if re.match(r'^(\d{1,3}\.){3}\d{1,3}$', host):
            return host
        else:
            print('Вы ввели некорректный адрес')



def scanner(port, host):
    global LOCK, open_ports
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except:
        pass
    else:
        with LOCK:
            available.append(port)
    finally:
        sock.close()


def scan_thread(host):
    global portQueue
    while True:
        port = portQueue.get()
        scanner(port, host)
        portQueue.task_done()


def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()


def prbar():
    global all_ports, start, portQueue
    while True:
        all_cnt = all_ports-start
        items = portQueue.qsize()
        in_scan = all_cnt - items
        printProgressBar(in_scan, all_cnt, ' Сканируется:', length = 50)
        if not items:
            break
    

def main(host, ports):
    global portQueue, treads_count
    for port_number in ports:
        portQueue.put(port_number)
    Thread(target=prbar, daemon = True).start()
    for _ in range(treads_count):
        Thread(target=scan_thread, args = [host], daemon = True).start()
    portQueue.join()   



host = getIP()
all_ports = 2**16
start = 1
treads_count = 5000
portQueue = Queue()
LOCK = Lock()
ports_list = [i for i in range(start,all_ports)]
available = []



main(host, ports_list)
available.sort()
print('Открытые порты:', '; '.join([str(i) for i in available]))