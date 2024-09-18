from Conexao_bd import Conexao
from datetime import datetime
from time import sleep
import os

conexao = Conexao()
cursor = conexao.cursor()

def Limpar_Terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def VerificarLogin(vcpf, vsenha):
    conexao = Conexao()
    if conexao:
        cursor = conexao.cursor()

        # Defina a consulta SQL como uma string
        comando = "SELECT * FROM TbLogin WHERE cpf = %s AND senha = %s"
        
        # Execute a consulta passando os parâmetros corretamente
        cursor.execute(comando, (vcpf, vsenha))

        # Busca o primeiro registro que corresponda
        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        # Verifique se o resultado foi encontrado
        if resultado:
            return True
        else:
            return False
    
def Nome_Cliente(cpf):
    conexao = Conexao()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT Nome FROM TbLogin WHERE cpf = {cpf}")
        resultado = cursor.fetchone()
        cursor.close()
        conexao.close()
        
        nome = str(resultado).split(0)
        if nome is not None:
            return(nome)
        else:
            return None

extrato = []
def Registrar_Operacao(tipo, valor_operacao):
    global extrato
    transacao = {
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "tipo": tipo,
        "valor": valor_operacao
    }
    extrato.append(transacao)
    

VALOR_LIMITE_SAQUE = float(1500)
VALOR_LIMITE_SAQUE_UNITARIO = float(500)        
LIMITE_SAQUES = 10
valor_sacado = float(0)
Qtd_Saques = 0
Saldo = float(cursor.callproc('ConsultaSaldo', Cpf))




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
    
    print(f'Saldo total: R${Saldo}')
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
    valor = float(input('Digite o valor que você quer depositar:  R$'))
    if valor <= 0:
        print("Você deve depositar um valor positivo.")
        sleep(1)
        Limpar_Terminal()
        return
    Saldo += valor
    Registrar_Operacao('Depósito', valor)
    print('Operação realizada com sucesso!')
    sleep(1)
    Limpar_Terminal()

def Extrato():
    global Saldo
    Limpar_Terminal()
    print('Extrato de operações: ')
    print(f'Saldo total: R${Saldo}')
    for transacao in extrato:
        print(f"{transacao['data_hora']} - {transacao['tipo']}: R${transacao['valor']:.2f}")
    input('Aperte ENTER para sair.')
    Limpar_Terminal
    