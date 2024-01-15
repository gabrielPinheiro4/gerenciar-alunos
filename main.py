import json
from const import constantes
from utils import escrever, zera_arquivo, gerar_media


def main(nome_arquivo):
    zera_arquivo(nome_arquivo)

    for alunos in constantes:
        gerar_media(alunos)

    exemplares = [
        alunos for alunos in constantes if alunos.get('media') > 9.5
        ]
    
    acima_media = [
        alunos for alunos in constantes if 7.5 < alunos.get('media') < 9.5
        ]
    
    abaixo_media = [
        alunos for alunos in constantes if alunos.get('media') < 7.5
        ]
    
    alunos_dicionario = [
            {'exemplares': exemplares}, 
            {'acima_media': acima_media}, 
            {'abaixo_media': abaixo_media}
        ]
    
    for lista in alunos_dicionario:
        escrever(nome_arquivo, json.dumps(lista, indent=4))


main('arquivo')
