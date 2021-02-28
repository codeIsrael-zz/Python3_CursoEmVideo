"""
Faça um programa que leia uma entrada do teclado e
mostre na tela o seu tipo primitivo e todas as
informações possiveis sobre ele.
"""

ent_tec = input("Digite algo: ")

print(f"O valor digitado é do tipo: {type(ent_tec)}\n"
      f"O valor digitado contem {len(ent_tec)} caracteres.\n"
      f"Só tem espaços? {ent_tec.isspace()}\n"
      f"É um número? {ent_tec.isalnum()}\n"
      f"É alfabético? {ent_tec.isalpha()}\n"
      f"É alfanumerico? {ent_tec.isalnum()}\n"
      f"Está em maiúsculo? {ent_tec.isupper()}\n"
      f"Está em minúsculo? {ent_tec.islower()}\n"
      f"Está capitalizado? {ent_tec.istitle()}"
      )
