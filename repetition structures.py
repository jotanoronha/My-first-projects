print("----- CONTADOR DE INIDADE -----")

numero = int(input("Início: "))
fim = int(input("Fim: "))
sequencia = int(input("Qual a sequência? "))

print("---- CONTANDO ----")

if numero <= fim:

    while numero <= fim:
        print(f"{numero}...")
        numero = numero + sequencia

else:

    while numero >= fim:
        print(f"{numero}...")
        numero = numero - sequencia

     