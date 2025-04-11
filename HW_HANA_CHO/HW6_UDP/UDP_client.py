import socket
port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input('Enter a message("send mboxId message" or "receive mboxId"): ')
    if msg == 'quit':
        break
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())
sock.close()