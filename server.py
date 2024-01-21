import socket
from faker import Faker

def server_program():
    faker = Faker()
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    print("接続待ちです。")
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("接続元: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("ユーザーからのデータ: " + data)
        data = faker.text()
        print("クライアントへ送るデータ: " + data)
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    server_program()
