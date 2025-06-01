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