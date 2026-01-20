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
    
    # Verify the response is an image file (binary content)
    assert len(response.content) > 0, "Response should contain image data"
    
    # Verify the content-type header indicates an image
    content_type = response.headers.get("content-type", "")
    assert "image" in content_type.lower(), f"Expected image content-type, got {content_type}"
    
    # Verify the response starts with JPEG magic bytes (FFD8FFE0 or FFD8FFE1)
    assert response.content[:2] == b'\xff\xd8', "Response should be valid JPEG data"
    

if __name__ == "__main__":
    test_read_root()
    test_download_picture()
    test_get_latest_picture()
    print("All tests passed.")