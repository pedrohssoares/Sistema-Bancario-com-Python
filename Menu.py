from Facilitar_Vida import Sacar, Extrato, Depositar

MENU = '''

Bem vindo! O que você deseja fazer?

[d] Depositar
[s] Sacar
[e] Consultar Extrato
[q] Sair

'''

while True:
    opcao = input(str(MENU))
    
    if opcao.lower() == 's':
        Sacar()
    elif opcao.lower() == 'd':
        Depositar()
    elif opcao.lower() == 'e':
        Extrato()
    elif opcao.lower() == 'q':
        break
    else:
        print('Opção inválida. Tente novamente.')

print('Até breve!')