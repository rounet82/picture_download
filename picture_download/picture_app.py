import streamlit as st
import requests
from PIL import Image
import os
from io import BytesIO

def fetch_data(url):
    response = requests.get(url)
    return response.json()

# Use API service name when in Docker, localhost otherwise
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = os.getenv("API_PORT", "8000")
API_URL = f"http://{API_HOST}:{API_PORT}"

st.title("Select the animal and the number of pictures to download")

animals = ["dog", "cat", "fox"]
animal = st.selectbox("Choose an animal:", animals, index=0)

numbers = list(range(1, 11))  # [1, 2, ..., 10]
num = st.selectbox("Choose a number:", numbers, index=0)

if st.button("Go"):
    response = requests.get(f"{API_URL}/picture/{animal}/{num}")
    st.write(response.json()["message"])

st.title("Get the latest downloaded picture")
if st.button("Get Latest Picture"):
    response = requests.get(f"{API_URL}/picture/latest")
    image = Image.open(BytesIO(response.content))
    st.image(image, caption="Latest picture", width="stretch")

