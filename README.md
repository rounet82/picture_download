# picture_download

## install python
apt install python3 python3-pip

## install packages
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

# Or with dev dependencies (includes testing tools)
pip install -e ".[dev]"

## run the app
uvicorn main:app --reload
