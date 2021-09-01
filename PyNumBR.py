# Projeto: Utilidades para tela do terminal
# Data: 01/08/2021
# License: GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007
# Fabiano Stussi Pereira® - © 2021

from datetime import datetime
import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def ler_inteiro(msg: str,
                msg_erro='[Erro de tipo] É esperado um número inteiro,' +
                'tecle enter para tentar novamente',
                tentativas=3) -> int:
    while tentativas > 0:
        numero = input(msg)
        if numero.isnumeric():
            numero_inteiro = int(numero)
            break
        else:
            print(msg_erro, f'[Tentativas restantes: {tentativas - 1}]')
            tentativas -= 1
            input()
    else:
        numero_inteiro = 0
    return numero_inteiro


def ler_real(msg: str,
             msg_erro='[Erro de tipo] É esperado um número real,' +
             'tecle enter para tentar novamente',
             tentativas=3):
    while tentativas > 0:
        numero = input(msg).replace(',', '.')
        teste = numero.split('.')
        if len(teste) == 2:
            if teste[0].isnumeric() and teste[1].isnumeric():
                numero_real = float(numero)
                break
            else:
                print(msg_erro, f'[Tentativas restantes: {tentativas - 1}]')
                tentativas -= 1
                input()
        else:
            print(msg_erro, f'[Tentativas restantes: {tentativas - 1}]')
            tentativas -= 1
            input()
    else:
        numero_real = 0
    return numero_real


def mostra_real(num_float: float) -> str:
    return f'{num_float:,}'.split('.')[0].replace(',', '.') + ',' + f'{num_float:,}'.split('.')[1]


def pega_data() -> str:
    return datetime.now().strftime('%d/%m/%Y')


def pega_hora() -> str:
    return datetime.now().strftime('%H:%M')


if __name__ == '__main__':
    pass
