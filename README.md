# Abstract
* This app downloads pictures of cats, dogs, and foxes using external APIs.
* The files are stored in a database.
* There are 2 APIs :
  * One to download the pictures : `/picture/{animal}/{number}` (e.g. `/picture/dog/3` will download 3 pictures of a dog)
  * One to download the latest pictures fetched via API and stored in the database `/picture/latest`. The file named "latest_picture.jpg" can be accessed in the "pictures" subfolder
* These API can be fetched by a UI

# How to install the app manually
The following commands are to be run on a Linux terminal.
The tool is to be run on a local machine.

## Pull the code
`git clone https://github.com/rounet82/picture_download.git`

## Install python
```
sudo apt update
sudo apt install python3 python3.12-venv python3-pip
```

## Install packages
```
cd picture_download
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Install dev dependencies (for testing)
```
pip install -e ".[dev]"
```

# How to run the app manually
## Run the main app
```
python -m picture_download.main
```
Open http://127.0.0.1:8000  in a browser.

## Run the UI (in a new terminal window)
```
cd picture_download
source .venv/bin/activate
streamlit run picture_download/picture_app.py
```
Open http://127.0.0.1:8501 in a browser. 

## Test the app
After running the main app
```
source .venv/bin/activate
cd picture_download
streamlit run picture_download/picture_app.py
```

## Run unit tests
Run tests with Mock to verify API calls:
```
source .venv/bin/activate
python -m pytest tests/unit_tests.py -v
```

Run tests with coverage report:
```
python -m pytest tests/unit_tests.py --cov=picture_download --cov-report=html -v
```
The HTML coverage report will be generated in `htmlcov/index.html`

# How to run the app in a container environment
If docker is not installed on your host, follow the [instructions](https://docs.docker.com/engine/install/) to install it then:
```
sudo apt install docker-compose
sudo usermod -aG docker $USER
newgrp docker
```
Then run the container
```
git clone https://github.com/rounet82/picture_download.git
cd picture_download
docker-compose up
```
Open http://127.0.0.1:8501 in a browser. 


# Running on an EC2 instance on AWS
It is also possible to run this solution on an EC2 instance. Just make sure the Security Group allows the traffic on the correct port (preferably with your source public IP address to be more secure).
