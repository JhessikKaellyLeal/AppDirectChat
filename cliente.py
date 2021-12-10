import socket   #importação da biblioteca socket
import threading  #importação da biblioteca threading para trabalhar com multitarefas 

# definir o host e a porta
host = "::1"
porta=int(input("Digite a porta:"))

#manda o host e a porta para o server
server = (host,porta)

#defini a codificação
cod = "ascii"

#pede para o usuario digitar o seu apelido (nckname)
nickname = str(input(" Digite um apelido para voce: "))

# Definindo conexao ipv6(AF_INET6) e UDP (SOCK_DGRAM)
conexao= socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)

#faz conexao  com o server
conexao.connect(server)
#codifica o nickname
msg = nickname.encode(cod)
#faz a conexao do envio da mensagem ao server
conexao.sendto(msg,server)

#metodo de receber mensagem
def receber():
    while True:
        print(conexao.recv(1024).decode(cod))
     
# metodo de envio de mensagem   
def enviar():
    while True:
        print("faça da seguinte forma: nome do receptor | mensagem")
        msg = str(input(""))
        conexao.sendto(msg.encode(cod),server)


#criando as threads de receber e enviar as mensagens        
threading.Thread(target=receber).start()
threading.Thread(target=enviar).start()