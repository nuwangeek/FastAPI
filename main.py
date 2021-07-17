from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Bimsara'}}

@app.get('/about')
def about():
    return {'data': 'About page'}

@app.get('/info')
def about():
    return {'info': 'Info page'}

#this is sub brnach of FATAPI-2
@app.get('/todo')
def about():
    return {'todo': 'ToDo page'}

