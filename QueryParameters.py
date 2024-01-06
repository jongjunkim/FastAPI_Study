from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


# @app.get("/items/")
# async def read_items(q: str | None = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results["items"].append({"item_id": q})
#     return results


#Annotated를 사용하면 입력값에 대한 유효성 검사
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results