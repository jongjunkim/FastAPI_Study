from fastapi import FastAPI
from pydantic import BaseModel


#Client(웹페이지) 에서 API로 데이터를 보낼때 데이터는 request body형태로 보내짐
class Item(BaseModel):
    name: str
    description: str | None = None #Use None to make it just optional
    price: float
    tax: float | None = None


app = FastAPI()


# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     # 만약 tax값이 들어온다면 Item class에 prcie_with_tax를 추가
#     if item.tax: 
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax}) 
#     return item_dict

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result