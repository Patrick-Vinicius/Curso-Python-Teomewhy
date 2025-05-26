#%%
import numpy as npy
import pandas as pd
# %%
arr1 = npy.array([ 10,12,24,13,17,15,69])

# %%
type(arr1)
# %%
arr1.shape
# %%
mask = (arr1 % 2 == 0)
# %%
mask
# %%
arr1[mask]
# %%
arr4 = npy.zeros(17)
# %%
arr4
# %%
arr5 = npy.eye(12)
print(arr5)
# %%
print(npy.linspace(0,2))
# %%
lista = [ 
         [0,1,2,6],
         [9,10,11,12],
         [1,2,3,5]
         ]
# %%
arr1 = npy.matrix(lista)
# %%

print(arr1)
# %%
npy.shape(arr1)
# %%
pontos = [12,14,16,18,20,22,24,26,28,30,52,56,58,60]
filtro = []


valores_50mais = []


for i in pontos:
    filtro.append(i>50)
resultado=[]

for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

#%%
resultado

#%%
brinquedos =  pd.DataFrame (
    {
        "nome" : ["Poo" , "Lala", "Telletubbies"],
        "idade" : [ 23,23,24],
        "valor_compra": [70,50,230]
    }
)

filtro = brinquedos["valor_compra"] > 70

brinquedos[filtro]
# %%
