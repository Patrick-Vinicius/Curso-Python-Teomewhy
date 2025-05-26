#%% 
import pandas as pd
import requests
import json
# %%
url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
listapoke = []

# %%
for i in url:
    resposta =  requests.get(url.format(url=i))
    listapoke.append(resposta.json())
# %%
listapoke
# %%
with open("listapoke.json", "w", encoding="utf-8") as open_file:
    json.dump(listapoke,open_file, ensure_ascii= False)
# %%
listapoke
# %%
