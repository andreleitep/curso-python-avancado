# Fazer isso no idle

import os
os.chdir("I:\\Meu Drive\\ADS - FATEC\\Outros Cursos\\python-avancado\\Capitulo_18_py_SQLite3")

import sqlite3
conector = sqlite3.connect('loja.db')
conector.close() # sempre necessário fechar arquivos externos abertos, ou eles podem ficar corrompidos
# um arquivo que não é fechado está pendente no sistema operacional