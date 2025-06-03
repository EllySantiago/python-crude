from database import ler_dados, escrever_dados

def criar_usuario(lista_de_usuarios):
    if not (lista_de_usuarios):
        print("Você ainda não tem uma conta. Vamos criar uma! \n")
        nomeUsuario = input("Crie seu nome de usuário: \n")
        dataNascimento = input("Digite sua data de nascimento: \n")
        senhaUsuario = input("Crie uma senha: \n")

        id_usuario = len(lista_de_usuarios) + 1

        usuario = {
            "id": id_usuario,
            "nome": nomeUsuario,
            "nascimento": dataNascimento,
            "senha": senhaUsuario
        }

        lista_de_usuarios.append(usuario)
        escrever_dados(lista_de_usuarios, "usuario")
    else:
        print("Vamos criar uma nova conta!")
        nomeUsuario = input("Crie seu nome de usuário: \n")
        dataNascimento = input("Digite sua data de nascimento: \n")
        senhaUsuario = input("Crie uma senha: \n")
        id_usuario = len(lista_de_usuarios) + 1
        
        usuario = {
            "id": id_usuario,
            "nome": nomeUsuario,
            "nascimento": dataNascimento,
            "senha": senhaUsuario
        }
        
        lista_de_usuarios.append(usuario)
        escrever_dados(lista_de_usuarios, "usuario")
        
def mostrar_meus_dados (usuario):
       
        print(f"Nome: {usuario['nome']}")
        print(f"Data de nascimento: {usuario['nascimento']}")

        opcao = input("Deseja ver sua senha? S/N \n")
        
        if opcao.lower() == 's':
            print(usuario["senha"])
        
        else:
            print("Ok. Vamos proseguir então.")

def login_usuario(lista):
    nome = input("Digite seu nome: \n")
    senha = input("Digite sua senha: \n")

    for usuario in lista:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            print("Login bem-sucedido :D \n")
            print("Bem-vindo", usuario["nome"]) 
            
            print("O que deseja fazer? \n")
            print("1- Ver dados \n")
            print("2- Editar dados \n")
            print("3- Excluir conta \n")
            print("4- Voltar ao menu principal \n")
            opcao = int(input("Escolha a opção desejada: \n"))
            
            if opcao == 1:
                mostrar_meus_dados (usuario)
            
            if opcao == 2:
                alterar_usuario(usuario)
            
            if opcao == 3:
                excluir_usuario(lista_de_usuarios, usuario)
            if opcao == 4:
                sair = True
            
            return
        
        
        
        
    print("Usuário ou senha incorretos. ")
    
    lista_de_usuarios = ler_dados("usuario")

    nomeUsuario = input("Digite o nome do usuário: \n")

def excluir_usuario (lista):
    nome = input("Digite seu nome: \n")
    senha = input("Digite sua senha: \n")

    for usuario in lista:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            lista.remove(usuario)
            escrever_dados(lista, "usuario")
            print("Conta excluída com sucesso! \n \n ")
            return

def alterar_usuario(lista):

    nome= input("Digite seu nome: \n")
    senha = input("Digite sua senha: \n")

    for usuario in lista:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            print("O que deseja alterar? \n")
            print("1 - NOME DE USUÁRIO: ")
            print("2- SENHA")
            print("3- DATA DE NASCIMENTO:")
            opcao = int(input("Digite a opção desejada: \n"))

            if opcao == 1:
                novoNome = input("Qual será seu novo nome de usuário? \n")
                usuario["nome"] = novoNome
                escrever_dados(lista, "usuario")
                print("Nome alterado com sucesso!")
            elif opcao == 2:
                novaSenha = input("Qual será sua nova senha? \n")
                usuario["senha"] = novaSenha

                escrever_dados(lista, "usuario")
                print("Senha alterada com sucesso!")
            elif opcao == 3:
                novaDNascimento = input("Qual sua data de nascimento? \n")

                usuario["nascimento"] = novaDNascimento
                escrever_dados(lista, "usuario")
                print("Data alterada com sucesso! ")
            return
    print("Usuário ou senha incorretos. ")
    
def menu():
    lista_de_usuarios = ler_dados("usuario")
    sair = False
    
    while not sair:
        print("\n--------MENU--------")
        print("1- Criar uma conta \n")
        print("2- Entrar numa conta \n")
        print("3- Sair")
        opcao = input("O que você deseja fazer? \n")
    
    
        if opcao == '1':
            criar_usuario (lista_de_usuarios)
        elif opcao == '2':
            login_usuario (lista_de_usuarios)
        elif opcao == '3':
            break
        else:
            print("opção inválida!")
