#%%

import random

#%%
numero_sorteio = random.randrange(1,15,1)

print(numero_sorteio)

# %%
for i in range(3):
    numero_usuario = int(input("Escolha um número de 0 à 15"))
    
    if numero_sorteio == numero_usuario:
        print("Parabéns, Ganhou um nada")
        break
    elif numero_usuario > numero_sorteio:
        print("You lose pança de porco, tente um número menor")
    elif numero_usuario <= 0:
        print("Entrada inválida, digite um número que esteja no intervalo de  1 à 15")
    else:
        print("Print número muito baixo... Tente um número maior")
else:
    ("Suas tentativas acabaram")
        
# %%
