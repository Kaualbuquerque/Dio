# Declaração de variáveis
extrato = ["Não foram realizadas movimentações"]
saques = 3
saldo = 0

# Função de Saque
def Saque(saldo, valor, saques):
    if saques > 0:
        if valor > 500:  # Verifica se o valor a ser sacado é maior que 500
            print("ERRO! O valor limite de saque é R$500!\n")
        elif valor < 0:  # Verifica se o valor a ser sacado é negativo
            print("ERRO! Não aceitamos valores negativos!\n")
        elif valor > saldo:  # Verifica se o valor a ser sacado é maior que o saldo da conta
            print("ERRO! Valor do saque maior que saldo em conta!")
        else:
            saldo -= valor
            extrato.append(f"Operação: Saque | Valor: R${valor}")
            print(f"Saldo atual: R${saldo}\n")
            saques -= 1
    else:
        print("Você atingiu o limite de saques diários!")
    return saldo, saques

# Função de Deposito
def Deposito(saldo, valor):
    if valor < 0:  # Verifica se o valor a ser sacado é negativo
        print("ERRO! Não aceitamos valores negativos!\n")
    else:
        saldo += valor
        extrato.append(f"Operação: Depósito | Valor: R${valor}")
        print(f"Saldo atual: R${saldo}\n")
    return saldo

# Função de Verificar o Extrato
def Extrato(saldo, extrato):
    if len(extrato) == 1 and extrato[0] == "\nNão foram realizadas movimentações":
        print(extrato[0])
    else:
        for i in extrato[1:]:
            print(i)
    print(f"Saldo atual: R${saldo}\n")

# Loop para sempre realizar a pergunta
while True:
    escolha = input("""Que operação deseja realizar?
        Saque[1]
        Deposito[2]
        Extrato[3]
        Sair[0]\n""")

    if escolha == "0":
        print("Desligando sistema")
        continuar = False
    elif escolha == "1":
        valor = int(input("Qual o valor do saque? "))
        saldo, saques = Saque(saldo, valor, saques)
    elif escolha == "2":
        valor = int(input("\nQual o valor do depósito? "))
        saldo = Deposito(saldo, valor)
    elif escolha == "3":
        Extrato(saldo, extrato)
    else:
        print("Opção inválida. Tente novamente.")
