import socket
import concurrent.futures

network = input("Enter network prefix (e.g. 192.168.1): ")

def scan(ip):
    try:
        socket.create_connection((ip, 80), timeout=0.2)
        return ip
    except:
        return None

with concurrent.futures.ThreadPoolExecutor(50) as executor:
    results = executor.map(
        scan,
        [f"{network}.{i}" for i in range(1, 255)]
    )

for ip in results:
    if ip:
        print("Active:", ip)