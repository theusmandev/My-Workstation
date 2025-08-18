import sys
import socket
import time
from datetime import datetime

# Get current time for logging
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Create a UDP socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as e:
    print(f"Error creating socket: {e}")
    sys.exit(1)

# User input for target IP and port
try:
    ip = input("Enter Target IP: ")
    port = int(input("Enter Port: "))
except ValueError:
    print("Invalid port number. Please enter a valid integer.")
    sys.exit(1)

# Validate IP address
try:
    socket.inet_aton(ip)
except socket.error:
    print("Invalid IP address.")
    sys.exit(1)

# Data to send (1490 bytes of 'A' characters for demonstration)
data = b'A' * 1490

# Clear screen and display start message (platform-independent)
print("\033[H\033[J", end="")  # ANSI clear screen
print("UDP Packet Sender Starting")
print("Author: HA-MRX")
print("GitHub: https://github.com/Ha3MrX")
print()

# Simulate progress bar
progress = ["[                    ] 0%", 
            "[=====               ] 25%", 
            "[==========          ] 50%", 
            "[===============     ] 75%", 
            "[====================] 100%"]
for step in progress:
    print(step)
    time.sleep(1)

# Send a limited number of packets (e.g., 10) for demonstration
sent = 0
max_packets = 700
print(f"\nSending {max_packets} packets to {ip}:{port}...")
try:
    for i in range(max_packets):
        sock.sendto(data, (ip, port))
        sent += 1
        print(f"Sent packet {sent} to {ip}:{port}")
        time.sleep(0.1)  # Small delay to avoid overwhelming the network
except socket.error as e:
    print(f"Error sending packet: {e}")
finally:
    sock.close()
    print("Socket closed. Transmission complete.")