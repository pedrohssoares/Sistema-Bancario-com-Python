from Facilitar_Vida import Sacar, Extrato, Depositar, Limpar_Terminal, VerificarLogin, Nome_Cliente

cpf = input("Digite o CPF: ")
senha = input("Digite a senha: ")

while VerificarLogin(cpf, senha) == False:
     Limpar_Terminal()
     print("CPF ou Senha Inválido")
     cpf = input("Digite o CPF: ")
     senha = input("Digite a senha: ")



while True:
    opcao = input(str(
        f'''

        Bem vindo{Nome_Cliente(cpf)}! O que você deseja fazer?

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