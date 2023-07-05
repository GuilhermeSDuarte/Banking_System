import os
os.system('cls') or None
selecionar = int
saldo = float(0)
valor = int
qtd_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:

    print("""
Bem vindo ao CashBank

    Saldo:R${saldo:.2f}
    
        Menu
    [1]- Depósito
    [2]- Saque
    [3]- Extrato
    [0]- Sair
    
""".format(saldo=saldo))

    selecionar = input("Digite a Opção:")

    if selecionar == "1":

        print("\nDepósito")

        try:

            valor = int(input("\nDigite o valor que deseja depositar: "))

            if valor <= 0:
                print("Valor invalido")

            else:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            selecionar = input("\ntoque em qualquer tecla para continuar com operações ou 0 para sair: ")

            if selecionar == "0":
                break

        except ValueError:
            print("O valor digitado não é numérico, tente novamente.")

    elif selecionar == "2" and qtd_saques < LIMITE_SAQUES:

        print("\nSaque")

        try:

            valor = int(input("\nDigite o valor que deseja sacar: "))

            if valor <= 500:

                if saldo > valor:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                else:
                    print("Você não possui saldo suficiente.")

            else:
                print("\nO Limite Maximo por saque é R$500,00.")

            qtd_saques += 1

            selecionar = input("\nToque em qualquer tecla para continuar com operações ou 0 para sair: ")

            if selecionar == "0":
                break

        except ValueError:
            print("O valor digitado não é numérico, tente novamente.")

    elif selecionar == "2" and qtd_saques == LIMITE_SAQUES:

        print("Limite de Saques excedidos.")
        print(f"Saques:{qtd_saques}".format(qtd_saques=qtd_saques))

    elif selecionar == "3":

        print("\n================== Extrato ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===============================================")

        selecionar = input("toquem em qualquer tecla para continuar com operações ou 0 para sair: ")

        if selecionar == "0":
            break

    elif selecionar == "0":
        break

    else:
        print("Opção Invalida, digite uma opção valida.")