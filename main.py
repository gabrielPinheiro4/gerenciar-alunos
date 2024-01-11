from const import constantes


class Aluno:
    for alunos in constantes:
        media = (alunos.get('nota_1') + alunos.get('nota_2')) / 2
        add_media = {'media': media}
        alunos.update(add_media)


    def exemplares(nome_arquivo):
        try:
            with open(nome_arquivo +'.txt', 'w+') as arq:
                for alunos in constantes:
                    if alunos.get('media') > 9.5:
                        arq.write(f'{alunos.get("aluno")} com media: {alunos.get("media")} \n')
                        
            return 'Arquivo criado com sucesso'
        
        except TypeError:
            return 'Digite um nome correto'
        

    def acima_media(nome_arquivo):
        try:
            with open(nome_arquivo +'.txt', 'w+') as arq:
                for alunos in constantes:
                    if 7.5 < alunos.get('media') < 9.5:
                        arq.write(f'{alunos.get("aluno")} com media: {alunos.get("media")} \n')
                        
            return 'Arquivo criado com sucesso'
        
        except TypeError:
            return 'Digite um nome correto'
        
    
    def abaixo_media(nome_arquivo):
        try:
            with open(nome_arquivo +'.txt', 'w+') as arq:
                for alunos in constantes:
                    if alunos.get('media') < 7.5:
                        arq.write(f'{alunos.get("aluno")} com media: {alunos.get("media")} \n')
                        
            return 'Arquivo criado com sucesso'
        
        except TypeError:
            return 'Digite um nome correto'
