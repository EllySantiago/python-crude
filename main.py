from feedbacks import menu_feedback
from usuario_delegado import menu_de_delegados
from denuncias import menu_denuncias


def menu():
    while True:
        print("█" * 50)
        print("█" * 14 + " SISTEMA DE DENÚNCIAS " + "█" * 14)
        print("1. Administrar delegados 1234")
        print("2. Fazer uma denúncia")
        print("3. gostaria de dar um feedback :) ?")
        print("4. sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_de_delegados()
        elif escolha == '2':
            menu_denuncias()
        elif escolha == '3':
           menu_feedback()
        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
