import socket
import threading

HOST = 'localhost'
PORT = 3333
BUFSIZE = 1024

def receive(sock):
    while True:
        try:
            data = sock.recv(BUFSIZE)
            if data:
                print('\n' + data.decode())
            else:
                break
        except:
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

recv_thread = threading.Thread(target=receive, args=(sock,))
recv_thread.daemon = True
recv_thread.start()

my_id = input('ID를 입력하세요: ')
sock.send(f'[{my_id}] 입장했습니다.'.encode())

while True:
    msg = input()
    if msg == 'quit':
        sock.send(f'[{my_id}] 퇴장합니다.'.encode())
        sock.close()
        break
    sock.send(f'[{my_id}] {msg}'.encode())
