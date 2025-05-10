import socket
import select

HOST = ''
PORT = 3333
BUFSIZE = 1024

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((HOST, PORT))
server_sock.listen(5)
print(f'Server listening on port {PORT}...')

sockets_list = [server_sock]  

while True:
    read_sockets, _, _ = select.select(sockets_list, [], [])
    
    for sock in read_sockets:
        if sock == server_sock:
            client_sock, addr = server_sock.accept()
            sockets_list.append(client_sock)
            print(f'New client connected from {addr}')
        else:
            try:
                data = sock.recv(BUFSIZE)
                if not data:
                    print('Client disconnected')
                    sockets_list.remove(sock)
                    sock.close()
                    continue
                
                msg = data.decode()
                print(f'Received: {msg}')
                
                for client in sockets_list:
                    if client != server_sock and client != sock:
                        client.send(data)
            except:
                sockets_list.remove(sock)
                sock.close()