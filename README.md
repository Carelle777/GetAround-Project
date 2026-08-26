# GetAround : Pricing Optimizer & Delay Analysis

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-00a393)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31-FF4B4B)](https://streamlit.io)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ed)](https://www.docker.com/)
[![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-F7931E)](https://scikit-learn.org/)

> **Projet certifiant - Data Engineering & MLOps Bootcamp (Jedha)**

---

## 📌 Contexte Business (Le Problème)
GetAround, leader de l'autopartage, est confronté à des pertes de revenus liées à deux facteurs majeurs :
1. **Les retards de restitution :** Qui entraînent l'annulation des réservations suivantes.
2. **La tarification sous-optimale :** Les propriétaires fixent des prix décorrélés du marché réel.

## 🎯 Objectifs & Solutions
Ce projet déploie une solution "Full-Stack Data" pour résoudre ces frictions :
- **Phase Analytics :** Création d'un Dashboard interactif permettant à l'équipe Produit de définir le temps de battement (*check-in threshold*) optimal pour réduire les annulations en cascade.
- **Phase MLOps :** Développement et mise en production d'une API de Machine Learning prédisant le tarif journalier optimal d'un véhicule selon ses caractéristiques techniques.

---

## Architecture Technique (Cloud & CI/CD)

Le projet est divisé en deux services web indépendants (Microservices) :
1. **Front-End / BI :** Application Streamlit pour l'analyse métier. 
👉 [Voir le Dashboard en ligne](https://getaround-carelle.streamlit.app/)
2. **Back-End / Inférence :** Serveur REST **FastAPI** + Uvicorn hébergeant le modèle ML.
3. **Infrastructure :** API conteneurisée via **Docker** et hébergée publiquement sur **Render**.

---

## Modélisation Machine Learning
- **Modèle utilisé :** Régression Linéaire / XGBoost *(à adapter selon ton vrai modèle)*.
- **Preprocessing :** Encodage One-Hot pour les variables catégorielles (marque, type de carburant) et Standardisation pour les variables numériques (kilométrage, puissance moteur).

---

## Tester l'API en direct (Production)

L'API de prédiction est en ligne et accessible publiquement ! Vous pouvez interagir avec l'IA via l'interface Swagger (UI) : 
👉 **L'API de prédiction est en ligne et accessible publiquement ! Vous pouvez interagir avec l'IA via l'interface Swagger (UI) : 
👉 L'API de prédiction est en ligne et accessible publiquement ! Vous pouvez interagir avec l'IA via l'interface Swagger (UI) : 
👉 **[Lien vers l'API GetAround en ligne](https://getaround-api-o2ij.onrender.com/docs)**

*(⏳ Note : L'API est hébergée sur un serveur gratuit. Si elle n'a pas été utilisée récemment, le premier chargement peut prendre **1 à 2 minutes** le temps que le serveur se réveille. Merci de votre patience !)*

**Format de requête attendu (Exemple de Payload JSON) :**
```json
{
  "model_key": "Renault",
  "mileage": 15000,
  "engine_power": 120,
  "fuel": "diesel",
  "paint_color": "black",
  "car_type": "sedan",
  "private_parking_available": true,
  "has_gps": true,
  "has_air_conditioning": false,
  "automatic_car": false,
  "has_getaround_connect": true,
  "has_speed_regulator": true,
  "winter_tires": true
}