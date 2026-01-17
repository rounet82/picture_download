from fastapi import FastAPI
import requests, random
import uuid, os, shutil
import sqlite3


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
    
    conn = sqlite3.connect('picture_database.db')
    cursor = conn.cursor()
    # Create table with BLOB column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY,
            name TEXT,
            data BLOB
        )
    ''')
    for _ in range(q or 1):
        response = requests.get(url)
        filename = f"{uuid.uuid4()}.jpg"
        with open(f"pictures/{filename}", "wb") as f:
            f.write(response.content)
        cursor.execute("INSERT INTO files (name, data) VALUES (?, ?)", (filename, response.content))
        shutil.move("pictures/" + filename, "pictures/latest_picture.jpg")
    conn.commit()
    conn.close()
    

    return {"message": "Picture(s) downloaded"}


@app.get("/picture/latest")
def get_latest_picture():
    if os.path.exists("pictures/latest_picture.jpg"):
        return ({"message": "pictures/latest_picture.jpg"})
    else:
        return ({"message": "No picture found"})
        