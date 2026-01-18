# picture_download

## install python
apt install python3 python3-pip

## install packages
python3 -m venv .venv
source .venv/bin/activate
cd picture_download
pip install -e .


## run the app
python -m picture_download.main

## run the UI (in a new terminal window)
source .venv/bin/activate
cd picture_download
streamlit run picture_download/picture_app.py