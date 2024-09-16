from datetime import datetime
from time import sleep

import os

Saldo = float(2000)

extrato = []
def Registrar_Operacao(tipo, valor_operacao):
    global extrato
    transacao = {
        "Data e Hora": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        "Tipo": tipo,
        "Valor": valor_operacao
    }
    extrato.append(transacao)
    
def Limpar_Terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

VALOR_LIMITE_SAQUE = float(1500)
VALOR_LIMITE_SAQUE_UNITARIO = float(500)        
LIMITE_SAQUES = 3
valor_sacado = float(0)
Qtd_Saques = 0

def Sacar():
    global Saldo, valor_sacado, Qtd_Saques
    
    saldo_disponivel_para_sacar = VALOR_LIMITE_SAQUE - valor_sacado
    
    if Qtd_Saques == LIMITE_SAQUES:
        print("Você atingiu o limite de saques diários")
        sleep(1)
        Limpar_Terminal()
        return
        
    if saldo_disponivel_para_sacar == 0:
        print(f"Você não pode sacar mais de R${VALOR_LIMITE_SAQUE:.2f} em um dia.")
        sleep(1)
        Limpar_Terminal()
        return
    
    if Saldo == 0:
        print("Seu saldo é igual a 0, deposite alguma quantia para conseguir sacar.")
        sleep(1)
        Limpar_Terminal()
        return
    
    print(f'Saldo disponível para saque: R${saldo_disponivel_para_sacar:.2f}.')
    valor = float(input(f"Digite a quantidade que você deseja sacar até R${VALOR_LIMITE_SAQUE_UNITARIO:.2f}:  "))
    if valor < 0:
        print("Você não pode sacar uma quantidade negativa.")
        sleep(1)
        Limpar_Terminal()
        return
    if valor > Saldo:
        print("Você não tem saldo suficiente para sacar esse valor.")
        sleep(1)
        Limpar_Terminal()
        return
    elif valor > VALOR_LIMITE_SAQUE_UNITARIO:
        print(f"O valor máximo que você pode sacar é R${VALOR_LIMITE_SAQUE_UNITARIO}")
        sleep(1)
        Limpar_Terminal()
        return
    elif valor > saldo_disponivel_para_sacar:
        print(f"Você não pode sacar mais de R${saldo_disponivel_para_sacar:.2f}")
        sleep(1)
        Limpar_Terminal()
        return
    else:
        Saldo -= valor
        valor_sacado += valor
        Qtd_Saques += 1
        Registrar_Operacao('Saque', valor)
        print('Operação realizada com sucesso!')
        sleep(1)
        Limpar_Terminal()

def Depositar():
    global Saldo

def Extrato():
    Limpar_Terminal()
    print('Extrato de operações: ')
    for transacao in Extrato:
        print(f"{transacao['data_hora']} - {transacao['tipo']}: R${transacao['valor']:.2f}")
    input('Aperte ENTER para sair.')
    Limpar_Terminal
    