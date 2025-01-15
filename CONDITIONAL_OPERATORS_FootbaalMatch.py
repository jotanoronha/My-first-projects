import math

print("BANGU X MADUREIRA")


bangu = int(input("Quantos gols BANGU fez? "))

madureira = int(input("Quantos gols MADUREIRA fez? "))

resultado = abs(bangu - madureira)

print(f"A diferença foi: {resultado}")

if resultado > 5:
    
    print("STATUS: PARTIDA COM GOLEADA")

else:

    print("STATUS: PARTIDA NORMAL")


