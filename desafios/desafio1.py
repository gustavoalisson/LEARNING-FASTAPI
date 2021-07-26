from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Animal(BaseModel):
    id: int
    nome: str
    idade: int
    sexo: str
    cor: str

base_dados_memoria = [
    Animal(id = 1, nome="Lulu", idade=6, sexo="femea", cor="marrom")
    ]    

@app.post('/animais')
def insere_animal(animal: Animal):
    base_dados_memoria.append(animal)
    return {
        animal.nome,
        animal.idade,
        animal.sexo,
        animal.cor
    }

@app.get('/animais')
def todos_animais():
    return {"Animais cadastrados": base_dados_memoria}

@app.post('/animais/{id_animal}')
def animais_por_id(id_animal: int):
    for animal in base_dados_memoria:
        if animal.id == id_animal:
            return animal 
    
@app.delete('/animais/{id_animal}')
def deleta_animal_id(id_animal: int):
    for animal in base_dados_memoria:
        if animal.id == id_animal:
            base_dados_memoria.remove(animal)
            return "Animal removido com sucesso!"