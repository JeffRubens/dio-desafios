menu = """

[D] Deposito
[R] Retirada
[I] Investir
[E] Extrato
[S] Sair

=> """

saldo = 0
limite = 500
extrato = ""
saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Valor depositado: R$ {valor:.2f}\n"
        else:
            print("Operação não realizada! O valor informado é inválido.")
    elif opcao == "R":
        valor = float(input("Valor da retirada: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = saques >= limite_saques
        if excedeu_saldo:
            print("Operação não realizada! O saldo é insuficiente.")
        elif excedeu_limite:
            print("Operação não realizada! O valor a ser retirado excede o limite.")
        elif excedeu_saques:
            print("Operação não realizada! Limite de saques excedido no dia.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Valor retirado: R$ {valor:.2f}\n"
            saques += 1
        else:
            print("Operação não realizada! O valor informado é inválido.")
    elif opcao == "I":
        valor = float(input("Valor da retirada para investimento: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = saques >= limite_saques
        if excedeu_saldo:
            print("Operação não realizada! O saldo é insuficiente.")
        elif excedeu_limite:
            print("Operação não realizada! O valor a ser retirado excede o limite.")
        elif excedeu_saques:
            print("Operação não realizada! Limite de saques excedido no dia.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Valor retirado para investimento: R$ {valor:.2f}\n"
            saques += 1
        else:
            print("Operação não realizada! O valor informado é inválido.")
    elif opcao == "E":
        print("\n************ MOVIMENTAÇÕS REALIZADAS ***********")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("--------------------------------------------------")
    elif opcao == "S":
        break
    else:
        print("Operação inválida, por favor selecione a operação disponibilizada.")
