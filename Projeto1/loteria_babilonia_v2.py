#%%

import random

#%%
numero_sorteio = random.randint(1,1510)

print(numero_sorteio)


def get_input():
    while True:
        try:
            numero_usuario = int(input("Escolha um número de 0 à 15"))
        except ValueError as err:
            print("Valor Inválido!")
            continue
        if 1<= numero_usuario <= 15:
            return numero_usuario
        print("Valor inválido! Por Favor,Digitar um valor entr 1 À 15")
        
def check_num(sorteio, usuario):
        if sorteio == usuario:
            print("Parabéns, Ganhou um nada")
            return True
        elif usuario > sorteio:
            print(" pança de porco, tente um número menor")
            return False
        else:
            print("Print número muito baixo... Tente um número maior")
            return False

# %%
for i in range(3):
    numero_usuario = get_input()
    
    if check_num(sorteio=numero_sorteio , usuario=numero_usuario):
        break
    
else:
    ("Suas tentativas acabaram")