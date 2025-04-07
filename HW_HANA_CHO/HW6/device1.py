import time
import random
import socket

HOST = '127.0.0.1'
PORT = 65431


def collect_device1_data():
    time.sleep(3)  
    temp = random.uniform(0, 40)  
    humid = random.uniform(0, 100)  
    illum = random.uniform(70, 150)  


    if not (0 <= temp <= 40 and 0 <= humid <= 100 and 70 <= illum <= 150):
        return "Error: Data out of range!"
    
    return f"Temp={temp:.1f}, Humid={humid:.1f}, Illum={illum:.1f}"


def device1_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Device 1 (Temperature, Humidity, Illuminance) listening on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Device 1 connected by {addr}")
                data = conn.recv(1024).decode().strip().lower()
                
                if data == "request":
                    result = collect_device1_data()
                    conn.sendall(result.encode())
                elif data == "quit":
                    conn.sendall("Device 1 stopped.".encode())
                    print("Device 1 stopped.")
                    break
                else:
                    conn.sendall("Invalid command.".encode())

if __name__ == "__main__":
    device1_server()