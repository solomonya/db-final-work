from fastapi import FastAPI, Depends
from .api import router

app = FastAPI()
app.include_router(router)

@app.get('/')
def root():
  return {'message': 'Hello, world!'}
