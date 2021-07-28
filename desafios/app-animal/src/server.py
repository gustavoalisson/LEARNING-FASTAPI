from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

app = FastAPI()

# Permisão para acessar a API
origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str

base_dados_memoria = []    

#Envia um objeto animal com todos os dados, exceto o ID
@app.post('/animais')
def insere_animal(animal: Animal):
    animal.id = str(uuid4())
    base_dados_memoria.append(animal)
    return {
        animal.nome,
        animal.idade,
        animal.sexo,
        animal.cor
    }
# Retorna todos os animais cadastrados
@app.get('/animais')
def lista_todos_animais():
    return base_dados_memoria

# Retorna com o ID especificado
@app.get('/animais/{id_animal}')
def busca_animais_por_id(id_animal: str):
    for animal in base_dados_memoria:
        if animal.id == id_animal:
            return animal
         
# apaga o animal pelo ID 
@app.delete('/animais/{id_animal}')
def deleta_animal_por_id(id_animal: str):
    for animal in base_dados_memoria:
        if animal.id == id_animal:
            base_dados_memoria.remove(animal)
            return "Animal removido com sucesso!"