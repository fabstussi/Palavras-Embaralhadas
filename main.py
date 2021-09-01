import os
from time import sleep
import random
import PyNumBR as pnum
import PyUtilTerminal as put


def config() -> bool:
    if not os.path.exists('palavras.txt'):
        with open('palavras.txt', 'wt+') as arq:
            arq.writelines('')
    if not os.path.exists('ranking.txt'):
        with open('ranking.txt', 'wt+') as arq:
            arq.writelines('')
    put.limpa_tela()
    with open('palavras.txt', 'r') as arq:
        vazio = arq.readlines()
    return len(vazio) > 0


def cria_menu(continua: bool, nome: str) -> str:
    if continua:
        print(f'{nome} vamos continuar então, escolha uma das opções')
    else:
        print(f'Dou-lhe as boas vindas {nome}')
    put.desenha_linha('=', 34)
    if not continua:
        nome = input('Diga-me seu nome por favor: ')
        put.desenha_linha('=', 34)
    menu = ['Adivinhar a palavra embaralhada [2 pontos]',
            'Adivinhar com a dica de duas letras [1 ponto]',
            'Cadastrar novas palavras',
            'Ver Ranking',
            'Sair']
    put.cria_menu(menu)
    return nome.capitalize()


def exibe_ranking() -> None:
    with open('ranking.txt', 'r') as arq:
        classificacao = arq.readlines()
    classificacao = list(map(lambda l: l.replace('\n', ""), classificacao))
    if len(classificacao) > 0:
        for i in range(len(classificacao)):
            print(classificacao[i])


def adiciona_palavras(palavra: str) -> None:
    with open('palavras.txt', 'r') as arq:
        lista = set(arq.readlines())
    total_palavras = len(lista)
    if total_palavras > 0:
        lista = set(map(lambda l: l.replace('\n', ""), lista))
    lista.add(palavra)
    if len(lista) == total_palavras:
        print(f'"{palavra}" já existe no dicionário de palavras')
    else:
        print(f'A palavra "{palavra}" foi adicionada com sucesso')
        with open('palavras.txt', 'a') as arqu:
            arqu.writelines(f'{palavra}\n')


def sorteia_palavra() -> str:
    with open('palavras.txt', 'r') as arq:
        lista = arq.readlines()
    lista = list(map(lambda l: l.replace('\n', ''), lista))
    palavra_sorteada = random.choice(lista)
    return palavra_sorteada


def embaralha_palavra(palavra: str) -> str:
    letras = [letra for letra in palavra[0:len(palavra)]]
    random.shuffle(letras)
    palavra = ''
    for letra in letras:
        palavra += letra
    return palavra


def mostra_dica(palavra: str) -> None:
    possicao_letras = [random.randrange(0, len(palavra) - 1) for i in range(2)]
    print('DICA: ', end='')
    for i in range(len(palavra)):
        print(palavra[i] if i in possicao_letras else ' * ', end='')
    print()


def palavras_embaralhadas(jogador: str, pontos: int, opcao: int) -> int:
    palavra = sorteia_palavra()
    palavra_embaralhada = embaralha_palavra(palavra)
    print(f'{jogador}, que palavra é esta {palavra_embaralhada}?')
    if opcao == 2:
        mostra_dica(palavra)
    palavra_jogador = input()
    put.desenha_linha('=', 34)
    if palavra_jogador.upper() == palavra:
        pontos += 2 if opcao == 1 else 1
        print(f'Parabéns {jogador}, você acertou!')
        print(f'você está com {pontos} pontos')
    else:
        print(f'Ops! {jogador} a palavra é {palavra}')
        print('Mais sorte na próxima!')
    put.desenha_linha('=', 34)
    return pontos


def grava_pontuacao(jogador: str, pontos: int) -> None:
    gravado = False
    controle = 1
    with open('ranking.txt', 'r') as arq:
        lista = arq.readlines()
    lista = list(map(lambda l: l.replace('\n', ''), lista))
    posicao_ranking = list(map(lambda l: l.split('-')[0], lista))
    jogador_ranking = list(map(lambda l: l.split('-')[1], lista))
    pontos_ranking = list(map(lambda l: l.split('-')[2], lista))
    with open('ranking.txt', 'w') as arqu:
        for i in range(len(lista)):
            if len(lista) == 0:
                break
            if pontos > int(pontos_ranking[i]) and not gravado:
                arqu.writelines(f'{i + controle}-{jogador}-{pontos}\n')
                print(f'{jogador} você é o {i + controle}º no ranking')
                controle += 1
                arqu.writelines((
                    f'{i + controle}-{jogador_ranking[i]}-{pontos_ranking[i]}\n'
                ))
                gravado = True
            else:
                arqu.writelines((
                    f'{i + controle}-{jogador_ranking[i]}-{pontos_ranking[i]}\n'
                ))
        if not gravado:
            controle = len(posicao_ranking) + 1
            arqu.writelines(f'{controle}-{jogador}-{pontos}\n')
            print(f'{jogador} você é o {controle}º no ranking')


if __name__ == '__main__':
    continuar = False
    jogador = 'desafiante'
    pontos = 0
    tem_palavras = config()
    if not tem_palavras:
        adiciona_palavras('EMBARALHADAS')
    while True:
        jogador = cria_menu(continuar, jogador)
        op = pnum.ler_inteiro('Escolha uma opção: ', tentativas=5)
        put.desenha_linha('=', 34)
        if op == 5:
            break
        if op == 4:
            exibe_ranking()
            put.desenha_linha('=', 34)
        if op == 3:
            adiciona_palavras(input('Digite a nova palavra: ').upper())
        if op == 2:
            pontos = palavras_embaralhadas(jogador, pontos, op)
        if op == 1:
            pontos = palavras_embaralhadas(jogador, pontos, op)
        if str(op) not in '12345':
            print('Opção inválida!')
        if input('Deseja continuar [Sim/Não]? ')[0].upper() == 'S':
            continuar = True
        else:
            break
if pontos > 0:
    grava_pontuacao(jogador, pontos)
print(f'{jogador} espero que tenha se divertido\n<Jogo encerrado>')
sleep(1)
