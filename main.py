import json
import os

from database import ler_dados , escrever_dados



usuarios = {}
senha_geral = "1234"


def senha():
    tentativas = 3
    while tentativas > 0:
        senha = input("Digite a senha para acessar o sistema: ")
        if senha == senha_geral:
            print("Acesso liberado.\n")
            return True
        else:
            tentativas -= 1
            print(f"Senha incorreta. Tentativas restantes: {tentativas}")
    print("Acesso negado. Encerrando o programa.")
    return False

def delegado_adicionar():
    try:
        id = int(input("Digite o ID do usuário: "))
        if id in usuarios:
            print("Esse ID já está em uso.")
        else:
            nome = input("Digite o nome do usuário: ")
            usuarios[id] = nome
            print(f"Usuário '{nome}' adicionado com sucesso.")
    except ValueError:
        print("ID inválido. Use apenas números.")

def delegado_excluir():
    try:
        id = int(input("Digite o ID do usuário a ser excluído: "))
        if id in usuarios:
            nome = usuarios.pop(id)
            print(f"Usuário '{nome}' removido com sucesso.")
        else:
            print("Usuário não encontrado.")
    except ValueError:
        print("ID inválido. Use apenas números.")

def lista_de_delegados():
    if usuarios:
        print("\nUsuários cadastrados:")
        for id, nome in usuarios.items():
            print(f"ID: {id} - Nome: {nome}")
    else:
        print("Nenhum usuário cadastrado.")

def atualizar_delegado():
    id = input("digite o id de delegado que deseja atualizar:").strip()
    if id in usuarios:
        print(f'usuario atual:{usuarios[id]}')
        novo_nome=input("digite o novo nome de usuario(aperte enter para manter):").strip()
        if novo_nome:
            usuarios[id]= novo_nome
            escrever_dados(usuarios, nome_do_arquivo)
            print("usuario atualizado com sucesso")
        else:
            print("nenhuma alteraçao feita.")
    else:
        print("usuario nao encontrado.")

def menu():
    while True:
        print("█" * 50)
        print("█" * 14 + " SISTEMA DE DENÚNCIAS " + "█" * 14)
        print("█" * 50)
        print("1. Adicionar Delegado")
        print("2. Excluir Delegado")
        print("3. Listar Delegados")
        print("4. atualizar delegado")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            delegado_adicionar()
        elif escolha == '2':
            delegado_excluir()
        elif escolha == '3':
            lista_de_delegados()
        elif escolha == '4':
            lista_de_delegados()
        elif escolha == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if senha():
    menu()






