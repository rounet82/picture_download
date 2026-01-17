import streamlit as st
import requests
from PIL import Image

def fetch_data(url):
    response = requests.get(url)
    return response.json()

st.title("Select the animal and the number of pictures to download")

animals = ["dog", "cat", "fox"]
animal = st.selectbox("Choose an animal:", animals, index=0)

numbers = list(range(1, 11))  # [1, 2, ..., 10]
num = st.selectbox("Choose a number:", numbers, index=0)

if st.button("Go"):
    data = fetch_data(f"http://127.0.0.1:8000/picture/{animal}/{num}")
    st.write(data["message"])

st.title("Get the latest downloaded picture")
if st.button("Get Latest Picture"):
    data = fetch_data("http://127.0.0.1:8000/picture/latest")
    print(data["message"])
    img = Image.open(data["message"])
    st.image(img, caption="Latest picture", width="stretch")