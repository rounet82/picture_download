from urllib import response
from fastapi import FastAPI
import requests, random
import uuid, os


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}



@app.get("/picture/{item_id}/{q}")
def download_picture(item_id: str, q: int | None = None):
    match item_id:
        case "cat":
            url = "https://placekittens.com/200/300"
        case "dog":
            url = 'https://place.dog/300/200'
        case "fox":
            url = 'https://randomfox.ca/images/' + str(random.randint(1, 120)) + '.jpg'
        case _:
            return 'Item not found'
        
    if not os.path.exists("pictures"):
        os.makedirs("pictures")
    if not os.path.exists("pictures/" + item_id):
        os.makedirs("pictures/" + item_id)
    
    for _ in range(q or 1):
        response = requests.get(url)
        with open(f"pictures/{item_id}/{uuid.uuid4()}.jpg", "wb") as f:
            f.write(response.content)

    return {"message": "Picture(s)s downloaded"}