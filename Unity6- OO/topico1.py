#%%
import pandas
from functools import reduce
#%%
lst =[47,11,42,13]
reduce(lambda x,y: x+y,lst)
# %%
print(lst)
# %%
def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
res = reduce(add, a)
#reduce(max_find,lst)
print(res) 
# %%
def tere(x, y):
    return x + y
b = ["a","b","c"]

des = reduce(tere, b)
print(des) 
# %%
class Dog(object):
    def __init__(self,raça):
        self.raça = raça
        self.idade = 10
    def envelhecer(self):
        self.idade += 3
sam = Dog(raça='Lab')
frank = Dog(raça='Huskie')
# %%
frank.idade
# %%
class Circle(object):
    pi = 3.14
# O círculo é instanciado com um raio (o padrão é 1)
    def __init__(self, radius=1):
        self.radius = radius
    # Método de cálculo da área. Observe o uso de si mesmo.
    def area(self):
        return self.radius * self.radius * Circle.pi
    # Método que redefine a área
    def setRadius(self, radius):
        self.radius = radius
    # Método para obter raio (Mesmo que apenas chamar .radius)
    def getRadius(self):
        return self.radius
c = Circle()
c.setRadius(2)
print('O raio é :',c.getRadius())
print('A área é',c.area())
# %%
 