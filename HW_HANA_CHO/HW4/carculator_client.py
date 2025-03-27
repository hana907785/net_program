from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('Enter expression (e.g., 20 + 17), or "q" to quit: ')
    if msg.lower() == 'q':
        break
    s.send(msg.encode())
    data = s.recv(1024)
    print('Result from server:', data.decode())

s.close()
