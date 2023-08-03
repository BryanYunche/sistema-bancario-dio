#Criar um sistema bancário com saque, deposito e extrato
# Saque: Só pode 3 saques por dia
# Saque: O limite de saques por dia é 500.0
# Saque: Deve armazenar o valor dos saques
# Depósito: Deve aceitar apenas valores positivos
# Depósito: Deve armazenar os valores depositados

# Limite de saques qe podem ser feitos
LIMITE_SAQUE = 3

# Conta quantas vezes já foi sacado
contSaque = 1

# Limite do valor do saque que pode ser feito
LIMITE_VALOR_SAQUE = 500

# Armazena os saques e extratos
extrato = ''

# Saldo Inicial
saldo = 1500

# Controla o loop do programa
sair = False

# Menu da aplicação
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> '''

while not sair:

    opcao = input(menu).lower()

    if opcao == 'd':
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo = saldo + valor
            extrato += f'Depósito: {valor:.2f}\n'
            print("Depósito concluido com sucesso!")
        else:
            print("Operação falhou! Valor inválido!")


    elif opcao == 's':
        valor = float(input("Digite o valor do saque: "))

        if contSaque <= LIMITE_SAQUE:
            if valor <= LIMITE_VALOR_SAQUE:
                if valor <= saldo:
                    saldo = saldo-valor
                    extrato += f'Saque: {valor:.2f}\n'

                    # Itera o número de saques já feitos
                    contSaque += 1

                    print("Saque concluido com sucesso!")
                else:
                    print("Valor do saque excede o valor do Saldo")
            else:
                print("O valor do saque excede o limite de R$500.00!")
        else:
            print("Limite de saques já foi atingido!")
    elif opcao == 'e':
        print("="*15)
        print(extrato)
        print(f'Saldo: {saldo}')
        print("=" * 15)


    elif opcao == 'q':
        sair = True

    else:
        print("Transação inválida")











