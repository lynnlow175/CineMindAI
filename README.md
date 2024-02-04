# The movie recommendation app

### Get Started

From here, you can run pip install commands

#### In order to run the app

Make sure to cd into server and client directories respectively

In client:

```
cd client
npm i
npm run dev
```

In server:
Run commands in order to run the right python environment

```
cd server
python -m venv .venv
source ./.venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
python server.py
```

### ML Model

Refer to this video https://youtu.be/pvY0BmAFxwg?si=2-8nCJE4BAcYjrA5

Model: https://tfhub.dev/google/universal-sentence-encoder/4

Dataset: https://www.kaggle.com/datasets/omkarborikar/top-10000-popular-movies?resource=download

In order to test the model, make sure to be in venv before running the command

```
jupyter notebook
```
