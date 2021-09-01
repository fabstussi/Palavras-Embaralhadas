# Projeto: Utilidades para tela do terminal
# Data: 01/08/2021
# License: GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007
# Fabiano Stussi Pereira® - © 2021

import os
import platform


def limpa_tela():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def desenha_linha(simbolo: str, tamanho=10):
    print(simbolo * tamanho)


def titulo(texto: str, simbulo='*'):
    texto = f'** {texto} **'
    desenha_linha(f'{simbulo}', len(texto))
    print(texto)
    desenha_linha(f'{simbulo}', len(texto))


def titulo_ml(titulos: list):
    maior_texto = len(titulos[0])
    for texto in titulos:
        tamanho_texto = len(texto)
        if tamanho_texto > maior_texto:
            maior_texto = tamanho_texto
    desenha_linha('=', maior_texto + 4)
    for texto in titulos:
        completa_espaco = maior_texto - len(texto)
        print(f'| {texto}'
              f'{" " * completa_espaco}|')
    desenha_linha('=', maior_texto + 4)


def cria_menu(menu: list):
    maior_texto = len(menu[0])
    for item in menu:
        tamanho_texto = len(item)
        if tamanho_texto > maior_texto:
            maior_texto = tamanho_texto
    desenha_linha('=', maior_texto + 9)
    for i, item in enumerate(menu):
        completa_espaco = maior_texto - len(item)
        if i < 10:
            print(f'|  {i + 1} - {item}'
                  f'{" " * completa_espaco} |')
        else:
            print(f'| {i + 1} - {item}'
                  f'{" " * completa_espaco}|')
    desenha_linha('=', maior_texto + 9)


if __name__ == '__main__':
    pass
