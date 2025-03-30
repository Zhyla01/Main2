import socket
import threading

def receive_message(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if message:
            print(f"Нове повідомлення: {message}")
        else:
            break

def main():
    server_address = ('localhost', 12345)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()

    user_name = input("Введіть ваше ім'я: ")

    while True:
        message = input("Ваше повідомлення: ")
        if message == 'exit':
            break
        client_socket.send(f"{user_name}: {message}".encode())

    client_socket.close()

if __name__ == "__main__":
    main()