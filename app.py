from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import (supplier_pydantic,Supplier_pydanticIn,Supplier)

app=FastAPI()
@app.get('/')
def index():
    return{"Msg":"go to /docs for the api documentation"}


@app.post('/supplier')
async def add_supplier(supplier_info:Supplier_pydanticIn):
    supplier_obj=await



register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models":["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)