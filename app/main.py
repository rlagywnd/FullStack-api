from typing import List,Optional
from fastapi import FastAPI,Query
from resolver import random_items
app = FastAPI();
a = 0;
@app.get("/all/") #localhost:8000/
async def all_movies():
    result=random_items()
    return {"message":result}

@app.get("/genres/{genre}")
async def genre_movies(genre:str):
    return {"message":f"genre:{genre}"}
    

@app.get("/user-based/")
async def user_based(param: Optional[List[str]]=Query(None)):
    return {"message":"user based"}

@app.get("/item-based/{item_id}")
async def user_based(item_id:str):
    return {"message":f"item based:{item_id}"}

@app.get("/")
async def root():
    return {"message":"인덱스 주소입니다"}

