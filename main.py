from fastapi import FastAPI
from typing import Union

# import comic.CreateComic



from src.routes import users, contacts, auth
app = FastAPI()
# app.include_router(ComicRouter.router)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(contacts.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
 