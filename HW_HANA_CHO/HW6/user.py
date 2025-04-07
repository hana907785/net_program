import socket
from datetime import datetime
import os

DEVICE1_HOST = '127.0.0.1'
DEVICE1_PORT = 65431
DEVICE2_HOST = '127.0.0.1'
DEVICE2_PORT = 65432


DATA_FILE = "/Users/chohana/net_program/HW_HANA_CHO/HW6/data.txt" 


data_log = []

def load_data():
    global data_log
    try:
        with open(DATA_FILE, "r") as f:
            data_log = f.readlines()
            data_log = [line.strip() for line in data_log]
    except FileNotFoundError:
        data_log = []


def save_data(device_data, device_type):
    global data_log
    load_data()  

    timestamp = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    data_entry = f"{timestamp}: {device_type}: {device_data}"

  
    device_count = sum(1 for entry in data_log if device_type in entry)

    if device_count < 5: 
        data_log.append(data_entry)
    else:
       
        for i in range(len(data_log)):
            if device_type in data_log[i]:
                data_log.pop(i)
                break
        data_log.append(data_entry)

    
    if len(data_log) > 10:
        data_log.pop(0)

    
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    
    with open(DATA_FILE, "w") as f:
        for entry in data_log:
            f.write(entry + "\n")


def view_data():
    load_data()
    if not data_log:
        print("No data available.")
    else:
        print("\nStored Data:")
        for entry in data_log:
            print(entry)


def send_request(device_host, device_port, command, device_name):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((device_host, device_port))
            s.sendall(command.encode())
            response = s.recv(1024).decode()
            return response
        except ConnectionRefusedError:
            return f"Error: Could not connect to {device_name}. Is the device running?"


def user_main():
    print("User: IoT Device Data Collection")
    print("Current working directory:", os.getcwd())  
    print("Data file path:", DATA_FILE)  

    while True:
        print("\nSelect an option:")
        print("1. Device 1 (Temperature, Humidity, Illuminance)")
        print("2. Device 2 (Heartbeat, Steps, Calories)")
        print("3. View Stored Data")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ").strip()

        if choice == "1":
            device_name = "Device1"
            host, port = DEVICE1_HOST, DEVICE1_PORT
        elif choice == "2":
            device_name = "Device2"
            host, port = DEVICE2_HOST, DEVICE2_PORT
        elif choice == "3":
            view_data() 
            continue
        elif choice == "4":
            print("User program terminated.")
            break
        else:
            print("Invalid choice.")
            continue

        command = input(f"Enter command for {device_name} (Request/Quit): ").strip().lower()
        if command not in ["request", "quit"]:
            print("Invalid command. Use 'Request' or 'Quit'.")
            continue

        response = send_request(host, port, command, device_name)
        print(f"{device_name} Response: {response}")

        if command == "request" and "Error" not in response:
            save_data(response, device_name)
        elif command == "quit":
            print(f"{device_name} has been stopped.")

if __name__ == "__main__":
    user_main()