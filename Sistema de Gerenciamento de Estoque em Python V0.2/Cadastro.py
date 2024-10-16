import sqlite3
import time
import sys
from DeletarRegistro import menu_de_deletar
from DeletarRegistro import apagar_registro_clientes
from DeletarRegistro import apagar_registros_produtos
from LogarnoSistema import menu_de_cadastro

banco_clientes = sqlite3.connect("banco_de_dadosclientes.db")

cursor = banco_clientes.cursor()

#cursor.execute("CREATE TABLE produtos (IDproduto integer, NOMEproduto text, VALORproduto integer, QUANTIDADEproduto integer)") 
#cursor.execute("CREATE TABLE clientes (nome text, cnpj integer, email text)")
#cursor.execute("CREATE TABLE users (IDuser interger, SENHAuser integer, NOMEuser text, NOMElogin text )")
    
def registrar_clientes(nome, cnpj, email):
    cursor.execute("INSERT INTO clientes (nome, cnpj, email) VALUES (?, ?, ?)", (nome, cnpj, email))
    banco_clientes.commit()
    
def registrar_produtos(id,nome,valor,quantidade):

    #cursor.execute("CREATE TABLE produtos (IDproduto integer, NOMEproduto texto, VALORproduto integer, QUANTIDADEproduto integer)") 
    cursor.execute("INSERT INTO produtos (IDproduto, NOMEproduto, Valorproduto, Quantidadeproduto) VALUES (?, ?, ?, ?)", (id, nome, valor,quantidade))
    banco_clientes.commit()
    
def menu():
    logo ="""   

CARREGANDO SISTEMA...
                                                               
                            .-'"|                                         
                            |-'"|                                         
                                |   _.-'`.                                
                               _|-"'_.-'|.`.                              
                              |:^.-'_.-'`.;.`.                            
                              | `.'.   ,-'_.-'|                           
                              |   + '-'.-'   J                            
           __.            .d88|    `.-'      |                            
      _.--'_..`.    .d88888888|     |       J'b.                          
   +:" ,--'_.|`.`.d88888888888|-.   |    _-.|888b.                        
   | \ \-'_.--'_.-+888888888+'  _&gt;F F +:'   `88888bo.                     
    L \ +'_.--'   |88888+"'  _.' J J J  `.    +8888888b.                  
    |  `+'        |8+"'  _.-'    | | |    +    `+8888888._-'.             
  .d8L  L         J  _.-'        | | |     `.    `+888+^'.-|.`.           
 d888|  |         J-'            F F F       `.  _.-"_.-'_.+.`.`.         
d88888L  L     _.  L            J J J          `|. +'_.-'    `_+ `;       
888888J  |  +-'  \ L         _.-+.|.+.          F `.`.     .-'_.-"J       
8888888|  L L\    \|     _.-'     '   `.       J    `.`.,-'.-"    |       
8888888PL | | \    `._.-'               `.     |      `..-"      J.b      
8888888 |  L L `.    \     _.-+.          `.   L+`.     |        F88b      CASTLE STORAGE SYSTEM V0.1
8888888  L | |   \   _..--'_.-|.`.          &gt;-'    `., J     |8888b    
8888888  |  L L   +:" _.--'_.-'.`.`.    _.-'     .-' | |       JY88888b   
8888888   L | |   J \ \_.-'     `.`.`.-'     _.-'   J J        F Y88888b  
Y888888    \ L L   L \ `.      _.-'_.-+  _.-'       | |       |   Y88888b 
`888888b    \| |   |  `. \ _.-'_.-'   |-'          J J       J     Y88888b
 Y888888     +'\   J    \ '_.-'       F    ,-T"\   | |    .-'      )888888
  Y88888b.      \   L    +'          J    /  | J  J J  .-'        .d888888
   Y888888b      \  |    |           |    F  '.|.-'+|-'         .d88888888
    Y888888b      \ J    |           F   J    -.              .od88888888P
     Y888888b      \ L   |          J    | .' ` \d8888888888888888888888P 
      Y888888b      \|   |          |  .-'`.  `\ `.88888888888888888888P  
       Y888888b.     J   |          F-'     \\ ` \ \88888888888888888P'   
        Y8888888b     L  |         J       d8`.`\  \`.8888888888888P'     
         Y8888888b    |  |        .+      d8888\  ` .'  `Y888888P'        
         `88888888b   J  |     .-'     .od888888\.-'                      
          Y88888888b   \ |  .-'     d888888888P'                          
          `888888888b   \|-'       d888888888P                            
           `Y88888888b            d8888888P'                              
             Y88888888bo.      .od88888888                                
             `8888888888888888888888888888                                
              Y88888888888888888888888888P                                
               `Y8888888888888888888888P'                                 
                 `Y8888888888888P'                                        
                      `Y88888P'       
                      
                      
                                    SISTEMA CARREGADO, INICIANDO...                                                 
        
    """
    for linha in logo.splitlines():
        time.sleep(0.07)
        print(linha)
    print("""
          
                                    |----------------------------------------------|                
                                    |                                              |      
                                    | BEM VINDO AO SISTEMA DE GERENCIAMENTO CASTLE |    
                                    |                                              |       
                                    |----------------------------------------------|                                             
    """)
    time.sleep(2)
    print("""
          
        |----------------------------------|                             
        |                                  |                          
        | 1. Registrar Fornecedor          |     
        |                                  |    
        |----------------------------------|      
             
        """)
    print("""
          
        |----------------------------------|                             
        |                                  |                          
        | 2. Cadastrar Produtos            |     
        |                                  |    
        |----------------------------------|  
         
          """)
    print("""
          
        |----------------------------------|                             
        |                                  |                          
        | 3. Deletar Registros             |     
        |                                  |    
        |----------------------------------|  

          """)
    escolha = int(input("ESCOLHA UMA OPÇÃO: "))
    
    
    if escolha ==1:
        
        nome = str(input("Registre o nome do fornecedor: "))
        cnpj = int(input("Registre o CNPJ do fornecedor: "))
        email = str(input("Registre emai do fornecedor:  "))
        registrar_clientes(nome,cnpj,email)
        print("Registrando cliente...")
        time.sleep(2)
        print("CLIENTE REGISTRADO COM SUCESSO!!")
        
        
    elif escolha ==2:
        
        id_produto = int(input("Digite o CÓDIGO do produto: "))
        nome_produto = str(input("Digite o NOME do produto: "))
        valor_produto = int(input("Digite o Valor do produto: "))
        quantidade_produto = int(input("Digite a QUANTIDADE do produto: "))
        registrar_produtos(id_produto, nome_produto, valor_produto, quantidade_produto)
        print("Registrando Produto no BANCO DE DADOS...")
        time.sleep(2)
        print("PRODUTO REGISTRADO COM SUCESSO!!")        
    
    elif escolha ==3:
        menu_de_deletar()
        
    elif escolha==4:
        print("Saindo do Sistema...")
        time.sleep(1)
        sys.exit()
    else:
        print("OPÇÃO INVÁLIDA!!")
        
menu_de_cadastro()    
menu()
 

cursor.close()
banco_clientes.close()
