import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 12345

client.connect((host, port))

message = ''

while (message != 'exit'):
    message = input('Digite a mensagem: ')
    client.send(message.encode('utf-8'))

client.close()
