from tortoise.models import Model
from tortoise import fields


class Products(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(max_length=30,nullable=False)
    quantity_in_stock=fields.IntField(default=0)
    quantity_sold=fields.IntField(default=0)
    