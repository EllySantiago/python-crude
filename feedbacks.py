import json
import os

ARQUIVO_FEEDBACK = 'feedbacks.json'

def ler_feedbacks():
    if not os.path.exists(ARQUIVO_FEEDBACK):
        with open(ARQUIVO_FEEDBACK, 'w') as f:
            json.dump([], f)
    with open(ARQUIVO_FEEDBACK, 'r') as f:
        return json.load(f)

def salvar_feedbacks(feedbacks):
    with open(ARQUIVO_FEEDBACK, 'w') as f:
        json.dump(feedbacks, f, indent=2)

def criar_feedback():
    denuncia_id = input("ID da denúncia: ")
    agente_nome = input("Nome do agente: ")
    mensagem = input("Mensagem do feedback: ")
    data = input("Data (ex: 2025-05-23): ")

    feedbacks = ler_feedbacks()

    novo_feedback = {
        "id": str(len(feedbacks) + 1),
        "denuncia_id": denuncia_id,
        "agente_nome": agente_nome,
        "mensagem": mensagem,
        "data": data
    }

    feedbacks.append(novo_feedback)
    salvar_feedbacks(feedbacks)

    print("✅ Feedback criado com sucesso!")

def listar_feedbacks():
    feedbacks = ler_feedbacks()
    if not feedbacks:
        print("Nenhum feedback registrado.")
        return
    print("\nLista de feedbacks:")
    for f in feedbacks:
        print(f"[{f['id']}] Denúncia ID: {f['denuncia_id']}, Agente: {f['agente_nome']}, Feedback: {f['mensagem']}, Data: {f['data']}")

def atualizar_feedback():
    id = input("ID do feedback a atualizar: ")
    feedbacks = ler_feedbacks()

    for i, f in enumerate(feedbacks):
        if f["id"] == id:
            while True:
                print("\nO que você quer atualizar?")
                print("1. Denúncia ID")
                print("2. Nome do agente")
                print("3. Mensagem")
                print("4. Data")
                print("5. Sair")

                opcao = input("Escolha uma opção: ")

                if opcao == '1':
                    novo = input(f"Novo Denúncia ID (atual: {f['denuncia_id']}): ")
                    if novo:
                        f['denuncia_id'] = novo
                elif opcao == '2':
                    novo = input(f"Novo nome do agente (atual: {f['agente_nome']}): ")
                    if novo:
                        f['agente_nome'] = novo
                elif opcao == '3':
                    novo = input(f"Nova mensagem (atual: {f['mensagem']}): ")
                    if novo:
                        f['mensagem'] = novo
                elif opcao == '4':
                    novo = input(f"Nova data (atual: {f['data']}): ")
                    if novo:
                        f['data'] = novo
                elif opcao == '5':
                    salvar_feedbacks(feedbacks)
                    print("✅ Feedback atualizado com sucesso!")
                    return
                else:
                    print("Opção inválida, tente novamente.")

    print("⚠️ Feedback não encontrado.")

def excluir_feedback():
    id = input("ID do feedback a excluir: ")
    feedbacks = ler_feedbacks()
    novas = [f for f in feedbacks if f["id"] != id]
    if len(novas) == len(feedbacks):
        print("⚠️ Feedback não encontrado.")
    else:
        salvar_feedbacks(novas)
        print("✅ Feedback excluído com sucesso!")

def menu_feedback():
    while True:
        print("\nMenu de Feedbacks")
        print("1. Criar feedback")
        print("2. Listar feedbacks")
        print("3. Atualizar feedback")
        print("4. Excluir feedback")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_feedback()
        elif opcao == '2':
            listar_feedbacks()
        elif opcao == '3':
            atualizar_feedback()
        elif opcao == '4':
            excluir_feedback()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    menu_feedback()
