import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

// seu ip
host = ''
port = 12345

client.connect((host, port))

message = ''

while message.lower() != 'exit':
    message = input('Digite a mensagem: ')
    client.send(message.encode('utf-8'))
    
    response = client.recv(1024)
    print('Resposta do servidor:', response.decode('utf-8'))

client.close()
def receive_messages():
    while True:
        try:
            response = client.recv(1024)
            if not response:
                break
            print('\nMensagem recebida:', response.decode('utf-8'))
        except:
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()
