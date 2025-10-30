# -*- coding: utf-8 -*-

def encontrar_maior(n1, n2, n3):
    """
    Recebe três números e retorna o maior deles.
    """
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    return maior

def encontrar_menor(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

def rodar_programa_principal():
    """
    Função principal para interagir com o usuário.
    """
    print("--- Comparador de Três Números ---")
    try:
        numero1 = int(input("Escreva o primeiro número: "))
        numero2 = int(input("Escreva o segundo número: "))
        numero3 = int(input("Escreva o terceiro número: "))
        
        maior = encontrar_maior(numero1, numero2, numero3)
        menor = encontrar_menor(numero1, numero2, numero3)
        
        print("\nO maior número é:", maior)
        print("O menor número é:", menor)
            
    except ValueError:
        print("Erro: Você deve digitar apenas números inteiros válidos.")

if __name__ == "__main__":
    rodar_programa_principal()
