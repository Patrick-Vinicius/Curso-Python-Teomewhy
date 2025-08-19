#%%
class livro:
    def __init__(self,pages, author,editora,title):
        
        self.pages = pages
        self.author = author
        self.editora = editora
        self.title =  title
        
    def __str__(self):
        return f"Title:{self.title}, author:{self.author},editora {self.editora}"
    
    def __len__(self):
        return self.pages
    
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book is destroyed")


livro2 = livro(pages=2740,author="Patrick",editora="O'Reilly", title="O homem que se lascava")
# Métodos especiais
print(livro2)
print(f"O livro tem {len(livro2)} páginas.")
# %%
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                # unexpectedly shared by all dogs


# %%
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
#%%
e.add_trick('play dead')
d.tricks

# %%
import numpy as np
#%%
np.array([1,2,3]) +1
# %%
