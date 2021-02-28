"""
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""

name = input("Qual o seu nome? ").title()


def boas_vindas(name):
    return f"Seja muito bem vindo {name}"


print(boas_vindas(name))
