
#%%
from functools import reduce

a = [17,22,25,32,40]

resolucao = reduce(lambda z, w: (z + w) -z,a)
print(resolucao)
#%%
class Spiderman:
   
    def __init__(self, name, age , power):
        self.name = name
        self.age = age
        self.power = power
        
spd1 = Spiderman("Tony",57,180000)

#%%
spd1.name
# %%
