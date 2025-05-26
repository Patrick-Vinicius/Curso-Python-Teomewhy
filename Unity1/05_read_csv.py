#%%
arquivo = "times.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()

print(lines)
# %%

for l in lines:
    print(l)

# %%
dados = dict()
chaves = lines[0].strip("\n").split(";")
for c in chaves:
    dados[c] = []

# %%
for l in lines[1:]:
    valores = l.strip("\n").split(";")
    
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i]) 
dados
# %%
titulos = []
for i in dados["Títulos"]:
    titulos.append(int(i))
media = sum(titulos) / len(titulos)
media
# %%
