import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))

    name = input("Введіть ваше ім'я: ")

    while True:
        message = input(" - > ")
        if message.lower() == 'bye':
            break
        full_message = f"{name}: {message}"
        client_socket.send(full_message.encode('utf-8'))

    client_socket.close()


if __name__ == "__main__":
    main()