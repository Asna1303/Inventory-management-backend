from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import supplier_pydantic, supplier_pydanticIn, Supplier  # Corrected import statement

app = FastAPI()

@app.get('/')
def index():
    return {"Msg": "go to /docs for the API documentation"}

@app.post('/supplier')
async def add_supplier(supplier_info:supplier_pydanticIn):
    supplier_obj = await Supplier.create(**supplier_info.dict(exclude_unset=True))
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {"status": "OK", "data": response}

@app.get('/supplier')
async def get_all_supplier():
    response=await supplier_pydantic.from_queryset(Supplier.all())
    return {"status": "OK", "data": response}

@app.get('/supplier/{supplier.id}')
async def get_specific_supplier(supplier_id:int):
    response=await supplier_pydantic.from_queryset_single(Supplier.get(id=supplier_id))
    return {"status": "OK", "data": response}


@app.put('/supplier/{supplier.id}')
async def update_supplier(supplier_id:int,update_info:supplier_pydanticIn):
    supplier=await Supplier.get(id=supplier_id)
    update_info=update_info.dict(exclude_unset=True)
    supplier.name=update_info.name
    supplier.company=update_info.company
    supplier.phone=update_info.phone
    supplier.email=update_info.email
    await supplier.save()
    response=supplier_pydantic .from_tortoise_orm(supplier)
    return {"status": "OK", "data": response}






register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
