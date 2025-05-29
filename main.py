import json
import os

from database import ler_dados, escrever_dados

nomeUsuario = input("Digite o nome do usuário: ")
nascimento = input ("digite a sua data de nascimento: ")
dictUsuario = { "nome": nomeUsuario, "data": nascimento}

lista_de_usuarios = ler_dados("usuario")
lista_de_usuarios.append(dictUsuario)
escrever_dados(lista_de_usuarios,"usuario")

for usuario in lista_de_usuarios:
    print(usuario)
