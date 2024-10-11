import sqlite3
import time

banco_clientes = sqlite3.connect("banco_de_dadosclientes.db")

cursor = banco_clientes.cursor()


cursor.close()
banco_clientes.close()
