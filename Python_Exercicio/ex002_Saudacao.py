"""
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""


def boas_vindas(name):
    return f"Seja muito bem vindo {name}"


nome = input("Qual o seu nome? ").title()


print(boas_vindas(nome))
