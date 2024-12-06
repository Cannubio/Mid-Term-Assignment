import socket

def start_server():
    host = '127.0.0.1'  # localhost
    port = 12345  # Arbitrary port that matches the client script

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)  # Maximum number of queued connections
        print(f"Server listening on {host}:{port}")

        conn, addr = server_socket.accept()  # Accept client connection
        print(f"Connection from {addr}")

        while True:
            data = conn.recv(1024).decode()  # Receive data from the client
            if not data:
                break  # Break the loop if no data is received
            print(f"Received from client: {data}")
            conn.send("Acknowledged".encode())  # Send response back to the client

        conn.close()  # Close the connection
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()  # Ensure the socket is closed properly

if __name__ == "__main__":
    start_server()
