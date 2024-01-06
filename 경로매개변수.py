from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

#app은 인스턴스로 uvicorn test:app --reload 여기서 사용됨
#만약 goodapp이라면 실행할떄 uvicorn test:goodapp 사용됨
#reload는 알아서 automatically하게 코드가 수정되면 서버 재실행
app = FastAPI()


class Item(BaseModel):
    name : str
    price : float
    is_offer : Union[bool, None] = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


#경로 매개변수 item_id의 값은 함수의 itemid로
# @app.get("/items/{item_id}")  
# def read_item(item_id: int, q : Union[str, None] = None ):
#     return {"item_id": item_id, "q": q}


# @app.get("/items/{item_id}") 
# def read_item1(item_id):
#     return {"item_id": item_id}

#타입이 있는 매개변수
@app.get("/items/{item_id}") 
def read_item1(item_id: int):
    return {"item_id": item_id}



#사전 정의값: 만약 밑에 read_user에서 user_id로 me 값이 들어올때 read_user가 이 reae_user_me 함수보다
#/user/me도 연결
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}