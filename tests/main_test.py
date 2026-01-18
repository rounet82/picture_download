import requests

def test_read_root():
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_download_picture():
    response = requests.get("http://localhost:8000/picture/cat/2")
    assert response.status_code == 200
    assert response.json() == {"message": "Picture(s)s downloaded"}
    response = requests.get("http://localhost:8000/picture/dog/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Picture(s)s downloaded"}
    response = requests.get("http://localhost:8000/picture/fox/3")
    assert response.status_code == 200
    assert response.json() == {"message": "Picture(s)s downloaded"}
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
    is_latest_picture_msg = "Latest picture" in message and "downloaded" in message
    is_no_pictures_msg = "No pictures found in the database" in message
    
    assert is_latest_picture_msg or is_no_pictures_msg, \
        f"Unexpected message: {message}"
    
    # print(f"✓ Response message is valid: {message}")
    

if __name__ == "__main__":
    test_read_root()
    test_download_picture()
    test_get_latest_picture()
    print("All tests passed.")