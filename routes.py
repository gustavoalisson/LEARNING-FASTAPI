from fastapi import FastAPI

app = FastAPI()

#Mapeia a operação do tipo get, e passa o caminho raiz /
# É autorizado ter rotas com o mesmo nome, porém com a operação diferente
@app.get('/profile')
def profile(profile: str):
    return {"Pessoa": profile}

@app.post('/profile')
def signup(profile: str):
    return {"Pessoa": profile + "Inserido com sucesso"}

@app.put('/profile')
def update(profile: str):
    return {"Pessoa": profile + "atualizado com sucesso"}

@app.delete('/profile')
def delete(profile: str):
    return {"Pessoa": profile + "deletado com sucesso"}

@app.get('/saudacao/{profile}')
def saudacao(profile: str):
    texto = f"Olá {profile}, seja bem-vindo"
    return {"mensagem": texto}

@app.get('/quadrado/{numero}')
def quadrado(numero: int):
    resultado = numero ** 2
    mensagem = f"O número {numero} ao quadrado é igual a {resultado}"
    return {"mensagem": mensagem}

# parametro de query string
@app.get('/dobro')
def dobro(valor: int):
    resultado = valor * 2
    mensagem = f"O resultado será {resultado}"
    return {"mensagem": mensagem}