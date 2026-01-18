from fastapi import FastAPI
import requests, random
import uuid, os
import sqlite3
import uvicorn

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
        os.remove("pictures/" + filename)
    conn.commit()
    conn.close()
    

    return {"message": "Picture(s) downloaded"}


@app.get("/picture/latest")
def get_latest_picture():
    conn = sqlite3.connect('picture_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, data FROM files ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        name, data = row
        if not os.path.exists("pictures"):
            os.makedirs("pictures")
        filepath = os.path.join("pictures", name)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "wb") as f:
            f.write(data)
        conn.commit()
        conn.close()
        return ({"message": filepath})
    else:
        conn.commit()
        conn.close()
        return {"message": "No pictures found in the database"}
    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)