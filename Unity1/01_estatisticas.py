def soma(a: float , b: float ,*args)-> float:
    valores = [a,b] + list(args)
    return sum(valores)
def media(a: float , b: float , *args)-> float:
    return soma(a,b,*args)/ (len(args)+2)

a = float(input("Entre com o primeiro valor: "))
b = float(input("Entre com o segundo valor: "))
c = float(input("Entre com o 3 valor: "))
d = float(input("Entre com o 4 valor: "))



print("media", media(a,b,c,d))

#%%
loja = {'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
        'precos': [2000, 1500, 3500, 4000, 1500]}
for chave, elementos in loja.items():
  print(f'Chave: {chave}\nElementos:')
  for dado in elementos:
    print(dado)
# %%
    