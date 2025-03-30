import socket
import threading


def handle_client(client_socket, address):
    print(f"Клієнт підключений з адреси {address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Отримано від {address}: {message}")
                broadcast(message, client_socket)
            else:
                print(f"Клієнт {address} відключено.")
                break
        except ConnectionResetError:
            print(f"Клієнт {address} відключився.")
            break
    client_socket.close()


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Не вдалося надіслати повідомлення до клієнта: {e}")


def main():
    global clients
    clients = []

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(5)
    print("Сервер запущено на порті 5000...")

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()


if __name__ == "__main__":
    main()