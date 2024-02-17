import socket  # Importa o módulo socket para comunicação em rede

# Define o endereço IP e as portas a serem utilizadas
TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
timeout = 3  # Define um tempo limite de espera em segundos
buf = 1024  # Define o tamanho do buffer para transferência de dados

# Cria um socket para lidar com a transferência do nome do arquivo
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_f.bind((TCP_IP, FILE_PORT))  # Associa o socket ao endereço e porta especificados
sock_f.listen(1)  # Habilita o socket para aceitar conexões, com limite de 1 conexão

# Cria um socket para lidar com a transferência dos dados do arquivo
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT))  # Associa o socket ao endereço e porta especificados
sock_d.listen(1)  # Habilita o socket para aceitar conexões, com limite de 1 conexão

while True:
    # Espera por uma conexão do cliente para transferir o nome do arquivo
    conn, addr = sock_f.accept()
    data = conn.recv(buf)  # Recebe os dados do cliente
    if data:
        print("File name:", data)
        file_name = data.strip()  # Remove possíveis espaços em branco extras

    f = open(file_name, 'wb')  # Abre o arquivo no modo de escrita binária

    # Espera por uma conexão do cliente para transferir os dados do arquivo
    conn, addr = sock_d.accept()
    while True:
        data = conn.recv(buf)  # Recebe os dados do cliente
        if not data:  # Se não houver mais dados a serem recebidos
            break
        f.write(data)  # Escreve os dados recebidos no arquivo

    print("%s Finish!" % file_name)  # Imprime uma mensagem indicando que a transferência do arquivo foi concluída
    f.close()  # Fecha o arquivo
