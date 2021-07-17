from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Bimsara'}}

@app.get('/about')
def about():
    return {'data': 'About page'}
