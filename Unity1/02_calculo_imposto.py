#%%

def calculo_imposto(preco:float, tx_base=0.3, **kwargs):
    imposto = preco * tx_base
    
    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
        
    return imposto


# %%

lista_impostos = {
    "municipal": 0.01,
    "estadual": 0.05,
    "federal": 0.04
}

calculo_imposto(100,0.3, **lista_impostos, international = 0.0000001)
    #%%