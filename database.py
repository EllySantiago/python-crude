import json
import os

def ler_dados(nome_do_arquivo):
    caminho_do_arquivo = f"{os.path.dirname(__file__)}{os.sep}database{os.sep}{nome_do_arquivo}.json"
    with open(caminho_do_arquivo, "r") as arquivo:
        dados = json.load(arquivo)
    return dados

def escrever_dados(dados_para_salvar,nome_do_arquivo):
    caminho_do_arquivo = f"{os.path.dirname(__file__)}{os.sep}database{os.sep}{nome_do_arquivo}.json"

    with open(caminho_do_arquivo, "w") as arquivo:
        json.dump(dados_para_salvar, arquivo)
