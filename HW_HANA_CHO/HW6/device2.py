import time
import random
import socket

HOST = '127.0.0.1'
PORT = 65432


def collect_device2_data():
    time.sleep(3)
    heartbeat = random.uniform(40, 140)  
    steps = random.uniform(2000, 6000) 
    calories = random.uniform(1000, 4000) 

    if not (40 <= heartbeat <= 140 and 2000 <= steps <= 6000 and 1000 <= calories <= 4000):
        return "Error: Data out of range!"
    
    return f"Heartbeat={heartbeat:.1f}, Steps={steps:.1f}, Cal={calories:.1f}"


def device2_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Device 2 (Heartbeat, Steps, Calories) listening on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Device 2 connected by {addr}")
                data = conn.recv(1024).decode().strip().lower()
                
                if data == "request":
                    result = collect_device2_data()
                    conn.sendall(result.encode())
                elif data == "quit":
                    conn.sendall("Device 2 stopped.".encode())
                    print("Device 2 stopped.")
                    break
                else:
                    conn.sendall("Invalid command.".encode())

if __name__ == "__main__":
    device2_server()