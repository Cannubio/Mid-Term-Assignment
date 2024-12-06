import socket
import time

def port_scanner(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}")
    open_ports = []  # List to store open ports
    
    for port in range(start_port, end_port + 1):
        print(f"Scanning port {port}...")  # Debugging output
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Timeout for each connection
            result = s.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port}: OPEN")  # Print if port is open
            s.close()
        except Exception as e:
            print(f"Error on port {port}: {e}")
    
    print("\nScan complete.")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    # User inputs for host and port range
    host = input("Enter host to scan (e.g., 127.0.0.1): ")
    
    # Validate the host
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Error: The host '{host}' is unreachable or invalid.")
        exit(1)
    
    try:
        start_port = int(input("Enter start port (e.g., 20): "))
        end_port = int(input("Enter end port (e.g., 80): "))
    except ValueError:
        print("Error: Port numbers must be integers.")
        exit(1)
    
    # Validate port range
    if start_port < 0 or end_port > 65535 or start_port > end_port:
        print("Error: Port numbers must be in the range 0-65535 and start_port <= end_port.")
        exit(1)

    # Measure performance
    start_time = time.time()
    port_scanner(host, start_port, end_port)
    end_time = time.time()
    
    print(f"Time taken to scan ports: {end_time - start_time:.2f} seconds")
