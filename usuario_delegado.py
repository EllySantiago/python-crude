from database import ler_dados , escrever_dados

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
        id = int(input("Digite a matrícula do delegado: "))
        usuarios = ler_dados("usuario")
        for usuario in usuarios:
            if id == usuario['id']:
                print("Esse ID já está em uso.")
                break
            else:
                nome = input("Digite o nome do usuário: ")
                usuarios.append({"nome": nome ,"id": id})
                escrever_dados(usuarios, "usuario")
                print(f"Usuário adicionado com sucesso.")
                break

def delegado_excluir():
    id = int(input("Digite a matrícula do delegado a ser excluído: "))
    usuarios = ler_dados("usuario")
    for usuario in usuarios:
        if id == usuario['id']:
            usuarios.remove(usuario)
            escrever_dados(usuarios, "usuario")
            print(f"Usuário removido com sucesso.")
            return
    print(f"Usuário não encontrado.")

def lista_de_delegados():
    usuarios = ler_dados("usuario")
    if usuarios:
        print("\nUsuários cadastrados:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']} - Nome: {usuario['nome']}")
    else:
        print("Nenhum usuário cadastrado.")

def atualizar_delegado():
    usuarios = ler_dados("usuario")
    id = int(input("digite a matricula/id de delegado que deseja atualizar:"))
    for index, usuario in enumerate(usuarios):
        if usuario['id'] == id:
            novo_id = int(input("digite a nova matricula/id para o delegado: "))
            novo_nome = input("digite o novo nome: ")
            usuarios[index] = {"id": novo_id, "nome": novo_nome}
            escrever_dados(usuarios, "usuario")
            print("usuario atualizado com sucesso!")
            return
print("Usuário não encontrado.")



def menu_de_delegados():
    if senha():

        while True:
            print("█" * 50)
            print("█" * 14 + " SISTEMA DE DENÚNCIAS " + "█" * 14)
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
               atualizar_delegado()
            elif escolha == '5':
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")






