from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('Waiting for connection...')

while True:
    client, addr = s.accept()
    print('Connection from', addr)
    
    while True:
        data = client.recv(1024)
        if not data:
            break
        
        try:
            expr = data.decode().replace(' ', '')  
            if '+' in expr:
                a, b = expr.split('+')
                result = int(a) + int(b)
            elif '-' in expr:
                a, b = expr.split('-')
                result = int(a) - int(b)
            elif '*' in expr:
                a, b = expr.split('*')
                result = int(a) * int(b)
            elif '/' in expr:
                a, b = expr.split('/')
                result = round(int(a) / int(b), 1)
            else:
                raise ValueError
            client.send(str(result).encode())
        except:
            client.send(b'Error: Invalid Expression')
