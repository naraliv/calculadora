numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite o segundo numero: "))

print("Escolha uma das opções abaixo")
print("1 - Adição")
print("2 -Subtração")
print("3 - Multipliação")
print("4 - Divisão")
operador = int(input("Digite o numero correspondente: "))

if operador == 1:
    print("A soma é: " + str(numero1 + numero2))
elif operador == 2:
    print("A soma é: " + str(numero1 - numero2))
elif operador == 3:
    print("A soma é: " + str(numero1 * numero2))
elif operador == 4:
    print("A soma é: " + str(numero1 / numero2))
else:
    print("Numero incorreto.")