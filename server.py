import socket   #importação da biblioteca socket
import threading  #importação da biblioteca threading para trabalhar com multitarefas 

# definindo o host e a porta
host = str(input("Host :"))
porta=int(input("Digite a porta:"))

# adicionando variavel para codificação
cod = "ascii"

# Definindo conexao ipv6(AF_INET6) e UDP (SOCK_DGRAM)
conexao= socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
#iniciando conexão
conexao.bind((host,porta))

#listando clientes e seus apelidos para definir o receptor das mensagens
clientes = []
nickname = []

#metodo para enviar a mensagem
def ms(nick,m,cliente):
    if(nick in nickname):#verifica se o apelido dos clientes esta conectado no momento
        usuario = clientes[nickname.index(nick)]# pega o nickname da lista de clientes
        nome = nickname[clientes.index(cliente)]
        msg = f"{nome} ]===> {m}" # passa no envio o nickname de quem enviou e a mensagem que foi enviada
        conexao.sendto(msg.encode(cod),usuario) #estabelece a conexao para envio da mensagem
    else:# se o cliente não estiver conectado ele informa a mensagem de que o usuario esta off
        msg = f"{nick} esta off"
        conexao.sendto(msg.encode(cod),cliente)# estabelece a conexão para enviar a mensagem

#define a forma como a mensagem deve ser enviada, onde o nickname vem antes , ai vem | e depois a mensagem
def geral(msg,cliente):
    if("|" in msg): #verifica se a mensagem foi enviada no formato correto, estando o nickname antes da | e mensagem depois
        msg = msg.split("|") # estabelece a separação de string usando -> |
        ms(msg[0],msg[1],cliente)
    else: #envia mensagem de erro caso haja problemas no envio
        print("erro 01")
    
# laço de repetição para receber todas as mensagens
while True:
    msg, cliente = conexao.recvfrom(1024) # estabelece a conexão e o tamanho da mensagem
    if(cliente in clientes): #verifica se o usuario é valido
        geral(str(msg.decode(cod)),cliente) #decodifica a mensagem e passa ao cliente
    else: #se não estiver entre os usuarios, vai enviar o nickname
        nick = msg.decode(cod)
        nickname.append(nick)
        clientes.append(cliente)