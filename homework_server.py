import socket
import threading

clients = []

def send_message(from_client, to_client, message):
    to_client.send(message.encode())

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if message:
            print(f"Отримано повідомлення: {message}")

            for client in clients:
                if client != client_socket:
                    send_message(client_socket, client, message)
        else:
            break

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(2)

    print("Сервер запущено. Чекаємо на клієнтів...")

    while len(clients) < 2:
        client_socket, addr = server_socket.accept()
        print(f"Клієнт підключений: {addr}")
        clients.append(client_socket)

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

    server_socket.close()

if __name__ == "__main__":
    main()