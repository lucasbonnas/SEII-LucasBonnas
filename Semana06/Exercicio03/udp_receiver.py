import socket  # Importa o módulo socket para comunicação em rede
import select  # Importa o módulo select para I/O assíncrona

# Define o endereço IP e a porta a serem utilizados
UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3  # Define um tempo limite de espera em segundos

# Cria um socket para comunicação UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Associa o socket ao endereço e porta especificados
sock.bind((UDP_IP, IN_PORT))

while True:
    # Recebe dados do cliente
    data, addr = sock.recvfrom(1024)
    if data:
        print("File name:", data)
        file_name = data.strip()  # Remove possíveis espaços em branco extras

    # Abre o arquivo no modo de escrita binária
    f = open(file_name, 'wb')

    while True:
        # Espera até que haja dados disponíveis para leitura no socket ou até que o tempo limite seja atingido
        ready = select.select([sock], [], [], timeout)
        if ready[0]:  # Se houver dados disponíveis para leitura no socket
            # Recebe os dados do cliente
            data, addr = sock.recvfrom(1024)
            # Escreve os dados recebidos no arquivo
            f.write(data)
        else:  # Se o tempo limite for atingido
            print("%s Finish!" % file_name)  # Indica que a transferência do arquivo foi concluída
            f.close()  # Fecha o arquivo
            break  # Sai do loop interno
