import socket  # Importa o módulo socket para comunicação em rede
import time  # Importa o módulo time para manipulação de tempo
import sys  # Importa o módulo sys para acessar argumentos da linha de comando

# Define o endereço IP e a porta a serem utilizados
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024  # Define o tamanho do buffer para transferência de dados
file_name = sys.argv[1]  # Obtém o nome do arquivo a ser enviado da linha de comando

# Cria um socket para comunicação UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envia o nome do arquivo para o destinatário especificado
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print("Sending %s ..." % file_name)

# Abre o arquivo em modo de leitura
f = open(file_name, "r")

# Lê uma quantidade de dados do arquivo e os envia via UDP
data = f.read(buf)
while data:
    # Envia os dados para o destinatário especificado
    if sock.sendto(data, (UDP_IP, UDP_PORT)):
        # Lê a próxima quantidade de dados do arquivo
        data = f.read(buf)
        # Aguarda um curto período de tempo para dar ao receptor um pouco de tempo para salvar os dados
        time.sleep(0.02)

# Fecha o socket
sock.close()
# Fecha o arquivo
f.close()
