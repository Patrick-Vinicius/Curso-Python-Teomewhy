#%%
import requests
import json
from tqdm import tqdm
import pandas as pd

#%%
ceps = [
    "53180080",
    "58038200",
    "58040740"
]

dados = []

url = "https://viacep.com.br/ws/{cep}/json/"
for i in tqdm(ceps):
    resposta  = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        print ("Status Captado com sucesso")
        dados.append(resposta.json())
#%%
dataset = pd.DataFrame(dados)
dataset
#%% 
with open("ceps.json", "w", encoding="utf-8") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)
# %%
