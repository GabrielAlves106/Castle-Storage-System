import sqlite3
import time
#from Cadastro import 

def menu_de_deletar():
    time.sleep(1)
    print("""
        |--------------------------------------------------|                             
        |                                                  |                          
        | 1. Deletar Registros de Fornecedores             |     
        |                                                  |    
        |--------------------------------------------------|  
        """)
    time.sleep(1)
    print("""
        |--------------------------------------------------|                             
        |                                                  |                          
        | 2. Deletar Registros de Produtos                 |     
        |                                                  |    
        |--------------------------------------------------|  
          """)
    time.sleep(1)
    
    escolha_de_delete = int(input("Escolha uma opção: "))
    
    if escolha_de_delete ==1:
        seleciona_fornecedor = int(input("Digite o CNPJ do fornecedor que deseja remover: "))
        apagar_registro_clientes(seleciona_fornecedor)
    elif escolha_de_delete ==2:
        seleciona_produto = int(input("Digite o ID do Profuto que você deseja remover: "))
        apagar_registros_produtos(seleciona_produto)
    else:
        print("Opção inválida")

def apagar_registro_clientes(selecionar):
    try:
        banco_clientes = sqlite3.connect("banco_de_dadosclientes.db")

        cursor = banco_clientes.cursor()

        cursor.execute("DELETE from clientes WHERE cnpj = ?", (selecionar,))
        banco_clientes.commit()

        cursor.close()
        banco_clientes.close()
        time.sleep(1)
        print("Removendo fornecedor....")
        time.sleep(1)
        print("Fornecedor Removido.")
        
    except sqlite3.Error as erro:
        print("Erro ao Excluir Dados...",erro)
        

def apagar_registros_produtos(selectprod):
    try:
        banco_clientes = sqlite3.connect("banco_de_dadosclientes.db")

        cursor = banco_clientes.cursor()

        cursor.execute("DELETE from produtos WHERE IDproduto = ?",(selectprod,))
        banco_clientes.commit()

        cursor.close()
        banco_clientes.close()
        time.sleep(1)
        print("Removendo Produto.....")
        time.sleep(1)
        print("Produto Removido.")
        
    except sqlite3.Error as erro:
        print("Erro ao Excluir Dados...",erro)
