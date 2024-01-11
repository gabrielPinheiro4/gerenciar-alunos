from const import constantes


def main(nome_arquivo, opcao):
    try:
        for aluno in constantes:
            media = (aluno.get('nota_1') + aluno.get('nota_2')) / 2
            adicionar_media = {'media': media}
            aluno.update(adicionar_media)
                        
        with open(f'{nome_arquivo}.txt', 'w+') as arq:
            if opcao == 'exemplares':
                arq.writelines(f'{[aluno for aluno in constantes if aluno.get("media") > 9.5]}')
                
            if opcao == 'acima_media':
                arq.writelines(f'{[aluno for aluno in constantes if 7.5 < aluno.get("media") < 9.5]}')
                
            if opcao == 'abaixo_media':
                arq.writelines(f'{[aluno for aluno in constantes if 7.5 > aluno.get("media")]}')
            
    except: 
        return 'Erro'
