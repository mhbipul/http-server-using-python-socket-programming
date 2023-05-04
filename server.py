import socket

HOST = 'localhost'  # Server's host name or IP address
PORT = 8000  # Port number for the server to listen on

def handle_request(client_socket, request):
    """Handles the client's HTTP request and sends a response."""
    # Extract the requested resource from the request (assuming a simple GET request)
    resource = request.split()[1]

    # Generate the HTTP response
    response = f'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World! You requested: {resource}\r\n'

    # Send the response to the client
    client_socket.sendall(response.encode())

    # Close the client connection
    client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f'Server listening on {HOST}:{PORT}')

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f'Client connected: {client_address[0]}:{client_address[1]}')

    # Receive the client's request
    request = client_socket.recv(1024).decode()

    # Handle the request and send a response
    handle_request(client_socket, request)