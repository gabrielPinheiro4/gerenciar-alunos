from const import constantes


def zera_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arq:
            arq.write('')
    except FileNotFoundError:
        return 'Arquivo não encontrado'


def escrever(nome_arquivo, conteudo_arquivo):
    try:
        with open(f'{nome_arquivo}.txt', 'w+') as arq:
            arq.writelines(conteudo_arquivo)
    except:
        return 'Error'


def main():
    for alunos in constantes:
        alunos.update({'media': (alunos.get('nota_1') + alunos.get('nota_2')) / 2})
        
    exemplares = f'{[alunos for alunos in constantes if alunos.get("media") > 9.5]}'
    acima_media = f'{[alunos for alunos in constantes if 7.5 < alunos.get("media") < 9.5]}'
    abaixo_media = f'{[alunos for alunos in constantes if alunos.get("media") < 9.5]}'

    zera_arquivo('sla.txt')

main()