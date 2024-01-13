def zera_arquivo(nome_arquivo):
    try:
        with open(f'{nome_arquivo}.txt', 'w') as arq:
            arq.write('')
    except FileNotFoundError:
        return 'Arquivo não encontrado'


def escrever(nome_arquivo, conteudo_arquivo):
    try:
        with open(f'{nome_arquivo}.txt', 'a+') as arq:
            arq.writelines(conteudo_arquivo)
    except:
        return 'Error'


def gerar_media(alunos):
    alunos.update(
            {'media': (alunos.get('nota_1') + alunos.get('nota_2')) / 2}
        )