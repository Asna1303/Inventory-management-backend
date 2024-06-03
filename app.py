from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app=FastAPI()
@app.get('/')
def index():
    return{"Msg":"Hello"}