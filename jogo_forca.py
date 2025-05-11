# Jogo da Forca. By: Alex Lopes

from random import choice


def achar_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
        return True

    except FileNotFoundError:
        a = open(nomeArquivo, 'wt+')
        a.close()
        return False


def colocar_palavras(nomeArquivo):
    a = open(nomeArquivo, 'at')
    a.write('lua\nsol\ngarfo\nfaca\ncolher\nmulher\nhomem\nastronauta\nadvogado\nalquimia\nafta\ncacto\niogurte\ntravesseiro\nventilador\ncopo\ntv\ncassetete\ncoxinha\nArthur\nAlex\nIsabella\nKaylan\nLiandra\nMaria\nJose\nNathalia\nEllen\nSarah\nDuda\n')
    a.close()


def carregar_palavra(nomeArquivo):
    global arquivo, score
    try:
        a = open(nomeArquivo, 'rt')
        if nomeArquivo == score:
            palavra = a.read()
            a.close()

        else:
            palavra = a.readlines()
            palavra = choice(palavra).strip()
            a.close()

        return palavra

    except FileNotFoundError:
        print('Error')


def scoreUpdate(nomeArquivo, score, nome, palavra, tentativas):
    try:
        a = open(nomeArquivo, 'at')
        a.write(f'Nome: {nome}  |  Score: {score:.2f}  |  Palavra: {palavra}  |  Tentativas: {tentativas}\n')
        a.close()
    except:
        print(f'Erro ao gravar Score no arquivo {nomeArquivo}!')


# PROGRAMA PRINCIPAL:
arquivo = 'pal.txt'
score = 'score.txt'
status = False
tentativas = 0

print('Bem-vindo ao Jogo da forca!')

if achar_arquivo(arquivo):
    print(f'\nArquivo encontrado!\n')
else:
    print(f'\nArquivo {arquivo} criado com sucesso!\n')

if achar_arquivo(score) is not True:
    print(f'\nArquivo {score} criado com sucesso!\n')

colocar_palavras(arquivo)


# LOOP PRINCIPAL:
while True:
    opt = int(input('1 | Jogar\n2 | Score\n3 | Sair\nDigite a opção desejada: '))
    match opt:
        case 1:  # Jogar
            if achar_arquivo(arquivo):
                palavra = carregar_palavra(arquivo).lower()
                nome = input('Digite seu nome: ')
                letras = []

                print('\nDigite "3" para desistir!\n')
                print(f'A palavra tem {len(palavra)} letras!\n')
                print('_' * len(palavra), end=' | ')

                while True:

                    quant_score = 100 * len(palavra)

                    letra = input('Digite a letra: ').lower()
                    tentativas += 1

                    for i in range(len(letras)):
                        if letras[i] == letra:
                            del letras[i]
                            break

                    letras.append(letra)

                    if letra == '3':
                        print(f'Mais sorte na próxima! A palavra era {palavra}!')

                        tentativas = 0
                        del letras
                        quant_score = 0

                        break

                    if letra in palavra:
                        print(f'A palavra tem a letra {letra}\n')

                    for i in range(len(palavra)):
                        status = False
                        for b in range(len(letras)):
                            if palavra[i] == letras[b]:
                                print(letras[b], end='')
                                status = True

                        if not status:
                            print('_', end='')

                    print(' | ', end='')

                    stop = True

                    for i in range(len(list(palavra))):
                        for j in range(len(letras)):
                            if palavra[i] == letras[j]:
                                break
                            elif letras[j] == letras[-1]:
                                stop = False

                    if stop:
                        quant_score = quant_score / tentativas
                        scoreUpdate(score, quant_score, nome, palavra, tentativas)
                        print(f'  Você conseguiu em {tentativas} tentativas!! A palavra era: {palavra.upper()}\n')

                        tentativas = 0
                        del letras
                        quant_score = 0

                        break

            else:
                print('Erro. Contate o desenvolvedor!')

        case 2:  # Score
            if achar_arquivo(score):

                palavra = carregar_palavra(score)
                if palavra:
                    print(f'\n{palavra}\n')
                else:
                    print('\n Nenhum Score registrado!\n')

            else:
                print('Erro. Contate o desenvolvedor!')

        case 3:  # Sair
            break
