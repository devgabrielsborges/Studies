import os
from random import randint

def roleta_russa(value : int):
    if value == randint(1,6):
        print(r"C:\Windows\System32")
    else:
        print("Parabéns!! Você venceu")

roleta_russa(int(input("Digite um número entre 1 e 6: ")))