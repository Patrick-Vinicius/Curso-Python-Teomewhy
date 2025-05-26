#%%
from random import randint
# %%
def gerar_cod():
    return str(randint(0,1999))

# %%
cod_estudantes = []
estudantes = ["Eduarda", "Luana", "Adriana", "Ana", "Papa Pio"]

for i in range(len(estudantes)):
    cod_estudantes.append((estudantes[i], estudantes[i][0] + gerar_cod()))

cod_estudantes
# %%
