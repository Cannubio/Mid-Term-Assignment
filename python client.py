import socket

def start_client():
    host = '127.0.0.1'
    port = 12345

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Connected to the server")

        message = "Hello, Server!"
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Response from server: {response}")
        
        client_socket.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_client()
