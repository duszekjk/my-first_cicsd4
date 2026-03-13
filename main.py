from fastapi import FastAPI

app = FastAPI()

def hello():
    return {"message": "Hello World"}