import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    
    client.send(b'Hello ' + addr[0].encode())
    # 학생의 이름을 수신한 후 출력
    name = client.recv(1024).decode()
    print(name)

    # 학생의 학번을 전송
    student_id = 20221337
    data = student_id.to_bytes(4, 'big') 
    client.send(data)

    client.close()