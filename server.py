import socket
import threading

# Função para lidar com cada cliente
def handle_client(client_socket, client_address):
    print(f"Conexão recebida de {client_address}")
    try:
        while True:
            # Receber a mensagem
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # Finaliza a conexão se o cliente encerrar
                print(f"Cliente {client_address} desconectado.")
                break
            print(f"Mensagem recebida de {client_address}: {message}")
            # Enviar uma resposta ao cliente (opcional)
            client_socket.send("Mensagem recebida!".encode('utf-8'))
    except ConnectionResetError:
        print(f"Cliente {client_address} desconectado abruptamente.")
    finally:
        client_socket.close()

# Criando o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'  # Aceita conexões de qualquer IP
port = 12345
server_socket.bind((host, port))
server_socket.listen(5)  # Até 5 conexões pendentes
print(f"Servidor escutando na porta {port}...")

# Loop principal do servidor
try:
    while True:
        client_socket, client_address = server_socket.accept()
        # Criar uma nova thread para lidar com o cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
except KeyboardInterrupt:
    print("\nServidor encerrado.")
finally:
    server_socket.close()
