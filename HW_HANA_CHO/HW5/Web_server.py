from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept() 
    
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n') #'GET /index.html HTTP/1.1', '...', '...'

    filename = req[0].split() #'GET', '/index.html', 'HTTP/1.1'
    filename = filename[1]  #'/index.html'
    filename = filename.strip('/') #'index.html'

    try:
        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html'
        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
    
        response_msg = 'HTTP/1.1 200 OK\r\nContent-Type: ' + mimeType + '\r\n\r\n'
        c.send(response_msg.encode())

        if 'text' in mimeType:
            data = f.read()
            c.send(data.encode('euc-kr'))  #euc-kr 이거로 하면 깨짐
        else:
            data = f.read()
            c.send(data)

    except: #예외처리
        response_msg = 'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        c.send(response_msg.encode())
    
    c.close()