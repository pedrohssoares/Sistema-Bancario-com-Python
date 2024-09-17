from Facilitar_Vida import Sacar, Extrato, Depositar, Limpar_Terminal

login = input("Digite o login: ")
senha = input("Digite a senha: ")

while VerificarLogin(login, senha) == False:
     Limpar_Terminal()
     print("Login Inválido")
     login = input("Digite o login: ")
     senha = input("Digite a senha: ")

while True:
    opcao = input(str(
        f'''

        Bem vindo {Login}! O que você deseja fazer?

        [d] Depositar
        [s] Sacar
        [e] Consultar Extrato
        [q] Sair

        '''
    ))
    
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