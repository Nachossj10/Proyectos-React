from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola desde Python"}

@app.get("/usuarios")
def usuarios():
    return [
        {"id":1,"nombre":"Juan"},
        {"id":2,"nombre":"Ana"}
    ]