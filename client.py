import socket

def client():
    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("'bye'でプログラムが終了します。")
    message = input(" --> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('サーバーからの応答: ' + data)

        message = input(" --> ")

    client_socket.close()

if __name__ == '__main__':
    client()
