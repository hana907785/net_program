import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)

print(msg.decode())
# 본인의 이름을 문자열로 전송
name = 'Hana Cho'
sock.send(name.encode())
# 본인의 학번을 수신 후 출력
data = sock.recv(4)
student_id = int.from_bytes(data, 'big')  
print(student_id)

sock.close()