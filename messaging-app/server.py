import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


server_socket.bind((IP, PORT))


server_socket.listen()


sockets = [server_socket]


clients = {}

print(f'Listening for connections on {IP}:{PORT}...')


def receive_message(client_socket):
    try:
        message = client_socket.recv(HEADER_LENGTH)

        if not len(message):
            return False

        message_length = int(message.decode('utf-8').strip())

        return {'header': message, 'data': client_socket.recv(message_length)}

    except:
        return False


while True:

    read_sockets, _, exception_sockets = select.select(
        sockets, [], sockets)

    for notified_socket in read_sockets:

        if notified_socket == server_socket:

            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)

            if user is False:
                continue

            sockets.append(client_socket)

            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(
                *client_address, user['data'].decode('utf-8')))

        else:

            message = receive_message(notified_socket)

            if message is False:
                print('Closed connection from: {}'.format(
                    clients[notified_socket]['data'].decode('utf-8')))

                sockets.remove(notified_socket)

                del clients[notified_socket]

                continue

            user = clients[notified_socket]

            print(
                f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            for client_socket in clients:

                if client_socket != notified_socket:

                    client_socket.send(
                        user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:

        sockets.remove(notified_socket)

        del clients[notified_socket]
