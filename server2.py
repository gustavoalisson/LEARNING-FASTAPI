from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    nome: str
    preco: float
    
@app.post('/produtos')
def produtos(produto: Produto):
    return {'mensagem': f'Produto {produto.nome} cadastrado com sucesso'}