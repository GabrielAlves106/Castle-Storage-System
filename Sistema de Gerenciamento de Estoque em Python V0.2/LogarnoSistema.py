import time
import sqlite3
import sys

banco_clientes = sqlite3.connect("banco_de_dadosclientes.db")

cursor = banco_clientes.cursor()

def menu_de_cadastro():
    print("""
          
        |----------------------------------|                             
        |                                  |                          
        | 1. Logar no Sistema              |     
        |                                  |    
        |----------------------------------|      
             
        """)
    time.sleep(1)
    print("""
          
        |----------------------------------|                             
        |                                  |                          
        | 2. Cadastrar no Sistema          |     
        |                                  |    
        |----------------------------------|      
             
        """)
    time.sleep(1)
    escolha_cadastro = int(input("Escolha Uma Opção: "))
    
    if escolha_cadastro ==1:
        
       Senha = int(input("Digite sua Senha: "))
       login = input("Digite seu Login: ")
       
       resultado_login = logar_sistema(Senha,login)
       if resultado_login=="Login feito com sucesso":
        time.sleep(1)
        print("Você Logou no Sistema!")
       else:
           print("Acesso Negado")
           sys.exit() 
       
    elif escolha_cadastro ==2:
        IDuser = int(input("Digite seu ID: "))
        Senhauser = int(input("Digite sua Senha: "))
        Nomeuser = input("Digite seu Nome: ")
        NomeLogin = input("Digite seu Login: ")
        cadastra_usuario(IDuser,Senhauser,Nomeuser,NomeLogin)
        
        time.sleep(1)
        print("Cadastrando...")
        time.sleep(1)
        print("Usuario Cadastrado com sucesso!")
        menu_de_cadastro()
    
def cadastra_usuario(ID,SENHA,NOME,LOGIN):
    cursor.execute("INSERT INTO users (IDuser, SENHAuser, NOMEuser, NOMElogin) VALUES (?, ?, ?, ?)", (ID, SENHA, NOME, LOGIN))
    banco_clientes.commit()

def logar_sistema(Senha,Login):
    cursor.execute("SELECT * FROM users WHERE NOMElogin = ? AND SENHAuser = ?", (Login, Senha))
    resultado = cursor.fetchone()
    if resultado:
        return "Login feito com sucesso"
    else:
        return "Acesso Negado"
        #sys.exit()
def oi():
    pass

    