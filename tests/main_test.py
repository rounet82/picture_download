import requests, re

def test_read_root():
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_download_picture():
    response = requests.get("http://localhost:8000/picture/cat/2")
    assert response.status_code == 200
    assert response.json() == {"message": "Picture(s) downloaded"}
    response = requests.get("http://localhost:8000/picture/dog/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Picture(s) downloaded"}
    response = requests.get("http://localhost:8000/picture/fox/3")
    assert response.status_code == 200
    assert response.json() == {"message": "Picture(s) downloaded"}
    response = requests.get("http://localhost:8000/picture/unknown/1")
    assert response.status_code == 200
    assert response.text == '"Item not found"'

def test_get_latest_picture():
    # First download a picture to populate the database
    requests.get("http://localhost:8000/picture/dog/1")
    
    response = requests.get("http://localhost:8000/picture/latest")
    assert response.status_code == 200
    json_response = response.json()
    assert "message" in json_response
    
    message = json_response.get("message", "")
    
    # Verify the message is one of the expected ones
    pattern = r'pictures/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\.jpg)'
    
    assert re.search(pattern, message), \
        f"Unexpected message: {message}"
    

if __name__ == "__main__":
    test_read_root()
    test_download_picture()
    test_get_latest_picture()
    print("All tests passed.")