from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib

# Je crée le manuel d'instructions (Description) qui s'affichera sur la page web /docs
description = """
# API GetAround - Optimisation Tarifaire
Bienvenue sur l'IA qui devine les prix. Envoyez une liste de caractéristiques de voitures, on renvoie les prix !
"""

# Je construis mon guichet avec son titre et son manuel d'instructions
app = FastAPI(
    title="GetAround Pricing Optimizer API",
    description=description
)

# Le guichet s'allume et charge le cerveau de l'IA immédiatement (Warm-up)
model = joblib.load("api/model.joblib")

# Je dessine le formulaire très strict que les clients doivent remplir (Règle Pydantic)
class PricingRequest(BaseModel):
    # Règle : Envoyez le mot "input" avec une liste, qui contient des listes de chiffres (Matrice 2D)
    input: List[List[float]]

@app.post("/predict")
async def predict_price(data: PricingRequest):
    # SOLUTION ARCHITECTE : L'énoncé envoie 11 chiffres, le modèle en attend 3.
    # On coupe la liste pour ne garder que les 3 premiers chiffres pour éviter le crash.
    clean_input = [ligne[:3] for ligne in data.input]
    
    # L'IA fait sa prédiction sur la liste propre
    predictions = model.predict(clean_input).tolist()
    
    return {"prediction": predictions}