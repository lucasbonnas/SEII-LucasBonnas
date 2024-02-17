import socket  # Importa o módulo socket para comunicação em rede
import sys  # Importa o módulo sys para acessar argumentos da linha de comando

# Define o endereço IP e as portas a serem utilizadas
TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024  # Define o tamanho do buffer para transferência de dados
file_name = sys.argv[1]  # Obtém o nome do arquivo a ser enviado da linha de comando

try:
    # Cria um objeto de socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Estabelece uma conexão com o servidor na porta FILE_PORT
    sock.connect((TCP_IP, FILE_PORT))
    # Envia o nome do arquivo para o servidor
    sock.send(file_name)
    # Fecha o socket após enviar o nome do arquivo
    sock.close()

    # Imprime uma mensagem indicando que o arquivo está sendo enviado
    print("Sending %s ..." % file_name)

    # Abre o arquivo em modo de leitura binária
    f = open(file_name, "rb")
    # Cria um novo socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Estabelece uma conexão com o servidor na porta DATA_PORT
    sock.connect((TCP_IP, DATA_PORT))
    # Lê todo o conteúdo do arquivo
    data = f.read()
    # Envia os dados do arquivo para o servidor
    sock.send(data)

finally:
    # Fecha o socket
    sock.close()
    # Fecha o arquivo
    f.close()
