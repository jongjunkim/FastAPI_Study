from fastapi import FastAPI
from typing import Union

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "Jun"}]

#기본값으로 skip = 0과 limit = 3으로 되어있어서
#http://127.0.0.1:8000/items/ 이동한거는 http://127.0.0.1:8000/items/?skip=0&limit=3
#현재 이거는 3까지 있으므로 뒤에 Jun은 나오지 않는다
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 3):
    return fake_items_db[skip : skip + limit]


# q 가 None이므로 선택적이라는것을 FastAPI는 인지   
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#http://127.0.0.1:8000/inputs/foo-item?needy=hello&essential=345
@app.get("/inputs/{input_id}")
async def read_user_input(input_id: str, needy: str, essential: int):
    item = {"input_ID": input_id, "needy": needy, "필수": essential}
    return item