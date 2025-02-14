import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./Progetto_1/ServiceAccountKey.json')
# Serve per gestire le connessioni sicure alla piattaforma
app = firebase_admin.initialize_app(cred)
# inizializzazione verso firebase tramite le credenziali date, gestisce la connesione con il database ma non estrapola dati
db = firestore.client(app)
# una classe che gestisce tutte le comunicazioni con l'applicazione

def add_prodotto(nome: str):
    db.collection('prodotti').document(nome).set({'nome':nome})

def get_prodotti():
    prodotti = []
    for prodotto in db.collection('prodotti').stream(): # dobbiamo andare nel base, leggere la collection ed ottenere i valori
        prodotti += [prodotto.to_dict()] # è uguale a scrivere prodotti.append(prodotto.to_dict())
    return prodotti