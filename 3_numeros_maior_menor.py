numero1 = int(input("escreva o primeiro numero: "))
numero2 = int(input("escreva o segundo numero: "))
numero3 = int(input("escreva o terceiro numero: "))

maiornumero = numero1

if numero2 > numero1 and numero2 > numero3:
    maiornumero = numero2

if numero3 > numero2 and numero3 > numero2:

    maiornumero = numero3

print('o maior numero é: ',maiornumero)

menornumero = numero1

if numero2 < numero1 and numero2 < numero3:
    menornumero = numero2

if numero3 < numero2 and numero3 < numero2:
    menornumero = numero3

print ('o menor numero é: ',menornumero)