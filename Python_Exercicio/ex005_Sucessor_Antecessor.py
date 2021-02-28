"""
Faça um programa que leia dois numeros e
mostre qual pe o seu sucessor e o seu antecessor.
"""


def ant(n):
    return n - 1


def sus(n):
    return n + 1


num = int(input("Digite um numero qualquer para saber seu sucesso e seu antecessor: "))


print(f"O antecessor de {num} é {ant(num)}\n"
      f"O sucessor de {num} é {sus(num)}")
