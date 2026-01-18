# Abstract
* This app downloads pictures of cats, dogs, and foxes using external APIs.
* The files are stored in a database.
* There are 2 APIs :
  * One to download the pictures : `/picture/{animal}/{number}` (e.g. `/picture/dog/3` will download 3 pictures of a dog)
  * One to download the latest pictures fetched via API and stored in the database `/picture/latest`. The file named "latest_picture.jpg" can be accessed in the "pictures" subfolder
* These API can be fetched by a UI

# How to install the app manually
The following commands are to be run on a Linux terminal.

## Pull the code
`git clone https://github.com/rounet82/picture_download.git`

## Install python
`apt install python3 python3-pip`

## Install packages
```
python3 -m venv .venv
source .venv/bin/activate
cd picture_download
pip install -e .
```

# How to run the app manually
## Run the main app
```
python -m picture_download.main
```
Open http://0.0.0.0:8000  in a browser.

## Run the UI (in a new terminal window)
```
source .venv/bin/activate
cd picture_download
streamlit run picture_download/picture_app.py
```
Open http://0.0.0.0:8501 in a browser. 

## Test the app
```
source .venv/bin/activate
cd picture_download
streamlit run picture_download/picture_app.py
```

# How to run the app in a container environment
```
git clone https://github.com/rounet82/picture_download.git
docker-compose up
```
Open http://0.0.0.0:8501 in a browser. 
