print("-----ESCOLA PUBLICA----")



nota1 = float(input("Qual foi a sua primeira nota? "))

nota2 = float(input("Qual foi a sua segunda nota? "))

media = (nota1 + nota2) / 2

if media > 9:

    print(f"Sua média é: {media} \n APROVEITAMENTO: A ")

elif media > 8:
    
    print(f"Sua média é: {media} \n APROVEITAMENTO: B ")

elif media > 7:
    
    print(f"Sua média é: {media} \n APROVEITAMENTO: C ")

elif media > 6:

    print(f"Sua média é: {media} \n APROVEITAMENTO: D ")

elif media < 5:

    print(f"Sua média é: {media} \n APROVEITAMENTO: F ")