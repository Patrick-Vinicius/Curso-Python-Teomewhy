#%%
class Celular:
    
    def __init__(self,nome, marca, bateria , avaliacao):
        self.nome = nome 
        self.marca= marca
        self.capacidade_bateria =  bateria
        self.avaliacao = avaliacao
        
    def listar(self):
        print("Dados do celular: " + self.nome + self.marca + self.capacidade_bateria + self.avaliacao )
#%%
Celular1 = Celular("Poco X7", "POCO", 6550,7.9)
       
    
# %%
Celular1.marca

# %%
