#%%
temp_celsius = [0,77,254,123,174,23,144]

temp_fahrenheit = list(map(lambda x: (x * 9/5) + 32, temp_celsius))

temp_fahrenheit
# %%
temp_fahrenheit2 =[23,53,70, 12.8 , 48.9, 93.7]

temp_kelvin = list(map(lambda y: (y + 273.8), temp_fahrenheit2))

temp_kelvin
# %%
for i in temp_kelvin:
    print("A temperatura convertida em kelvin é: ", i)
# %%
gols_marcados = [2, 1, 3, 1, 0,0]
gols_sofridos = [1, 2, 2, 1, 3,0]

def calcula_pontos(gols_marcados, gols_sofridos):
  pontos = 0
  for i in range(len(gols_marcados)):
    if gols_marcados[i] > gols_sofridos[i]:
      pontos += 3
    elif gols_marcados[i] == gols_sofridos[i]:
      pontos += 1
  aprov = 100 * pontos / (len(gols_marcados) * 3)
  return (pontos, aprov)

pontos, aprov = calcula_pontos(gols_marcados, gols_sofridos)
print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {round(aprov)}%")
# %%
pontos_marcados = [142, 128 , 132 , 139, 151]
pontos_sofridos = [152, 128, 120, 121 ,98]

pontos_extratimeA = [132]
pontos_extratimeB = [131]
def calcula_nba(pontos_marcados, pontos_sofridos):
    ponto = 0
    
    for i in range(len(pontos_marcados)):
        if pontos_marcados[i] > pontos_sofridos[i]:
            ponto += 1
        elif pontos_marcados[i] == pontos_sofridos[i]:
            ponto += 0
    aproveitamento = 100 * ponto / len (pontos_marcados)
    return (ponto, aproveitamento)
   
ponto , aproveitamento = calcula_nba(pontos_marcados, pontos_sofridos)

print(f"A quantidade de jogos gannhos foi de {ponto} e o aproveitamento foi de {round(aproveitamento)}%")
# %%
# Requisitando uma frase e separando-a pelos espaços. Usando replace para trocar
# pontuações por espaço.
frase = input("Digite uma frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

# Filtrando a frase no formato de lista, passando para a lista tamanho
# apenas as palavras com 5 ou mais caracteres e imprimindo-a na tela
tamanho = list(filter(lambda x: len(x) >= 5, frase))
print(tamanho)
# %%
