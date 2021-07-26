from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alisson = "Alisson Gustavo"
    joismar = "Joismar Parvi"
    carlos = "Carlos"

app = FastAPI()
# Você também pode acessar o valor "Carlos" com ModelName.lenet.value.


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alisson:
        return {"model_name": model_name, "message": "Encontrou Alisson hehehe"}
    
    if model_name.value == "Carlos":
        return {"model_name": model_name, "message": "alguma coisa sei lá"}
    
    return {"model_name": model_name, "message": "Mais alguma coisa apenas de teste"}