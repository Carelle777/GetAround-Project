# Je dis à Hugging Face d'installer un ordinateur virtuel avec Python 3.9
FROM python:3.13

# Je crée un dossier "code" à l'intérieur de cet ordinateur virtuel (la boîte Docker)
WORKDIR /code

# Je transfère ma liste de courses (les dépendances) dans la boîte
COPY ./requirements.txt /code/requirements.txt

# Je demande à la boîte d'installer tous les outils de la liste de courses
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# TRÈS IMPORTANT : Je copie mon dossier "api" (qui contient mon code main.py ET mon cerveau model.joblib) dans la boîte
COPY ./api /code/api

# J'appuie sur le bouton "ON". J'allume le guichet Uvicorn sur le port 7860 (obligatoire pour Hugging Face)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "7860"]