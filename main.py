import json
import os

arquivo = 'denuncias.json'

def ler_dados():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f)
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_dados(dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=2)

def criar_denuncia():
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data = input("Data: ")
    local = input("Local: ")
    denuncias = ler_dados()
    nova = {
        "id": str(len(denuncias) + 1),
        "titulo": titulo,
        "descricao": descricao,
        "data": data,
        "local": local,
        "status": "aberta"
    }
    denuncias.append(nova)
    salvar_dados(denuncias)
    print("Denúncia criada")

def lista_denuncias():
    denuncias = ler_dados()
    if not denuncias:
        print("Nenhuma denúncia registrada")
        return
    for d in denuncias:
        print(f"[{d['id']}] {d['titulo']} - {d['status']}")

def ver_denuncia():
    id = input("ID da denúncia: ")
    denuncias = ler_dados()
    for d in denuncias:
        if d["id"] == id:
            print(json.dumps(d, indent=2))
            return
    print("Denúncia não encontrada")

def atualizar_denuncia():
    id = input("ID da denúncia a atualizar: ")
    denuncias = ler_dados()
    for i, d in enumerate(denuncias):
        if d["id"] == id:
            d["titulo"] = input(f"Novo título({d['titulo']}): ") or d["titulo"]
            d["descricao"] = input(f"Nova descrição({d['descricao']}): ") or d["descricao"]
            d["data"] = input(f"Nova data({d['data']}): ") or d["data"]
            d["local"] = input(f"Novo local({d['local']}): ") or d["local"]
            d["status"] = input(f"Novo status({d['status']}): ") or d["status"]
            salvar_dados(denuncias)
            print("Denúncia atualizada")
            return
    print("Denúncia não encontrada")

def excluir_denuncia():
    id = input("ID da denúncia a excluir: ")
    denuncias = ler_dados()
    novas = [d for d in denuncias if d["id"] != id]
    if len(novas) == len(denuncias):
        print("Denúncia não encontrada")
    else:
        salvar_dados(novas)
        print("Denúncia excluída")

def menu():
    while True:
        print("\nMenu de denúncias")
        print("1. Criar denúncia")
        print("2. Listar denúncias")
        print("3. Ver denúncia")
        print("4. Atualizar denúncia")
        print("5. Excluir denúncia")
        print("6. Sair")
        opcao = input("Escolha opção: ")
        match opcao:
            case '1':
                criar_denuncia()
            case '2':
                lista_denuncias()
            case '3':
                ver_denuncia()
            case '4':
                atualizar_denuncia()
            case '5':
                excluir_denuncia()
            case '6':
                print("Saindo do sistema")
                break
            case _:
                print("Opção inválida")

if __name__ == '__main__':
    menu()

