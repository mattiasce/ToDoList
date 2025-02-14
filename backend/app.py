from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from database import add_prodotto, get_prodotti

app = FastAPI()

@app.get('/prodotto')
def prodotto(nome:str):
    #aggiungere al db
    add_prodotto(nome)
    return True

@app.get('/prodotti')
def prodotti():
    return get_prodotti()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # origins,  # or ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # or specify specific methods ["GET", "POST"]
    allow_headers=["*"],  # or specify specific headers
)

uvicorn.run(app, host="0.0.0.0", port=8000)

### RESTAPI: INTERFACCIA WEB CHE EROGA UN SERVIZIO FORNENDO DATI/ PACCHETTI DI DATI(JSON)