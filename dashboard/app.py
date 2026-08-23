# Importation de l'outil de site web (Streamlit), du manipulateur de données (Pandas) et du dessinateur (Plotly)
import streamlit as st
import pandas as pd
import plotly.express as px

# Je dis à l'ordinateur de mémoriser ce fichier pour ne pas le recharger 100 fois par minute
@st.cache_data
def load_data():
    return pd.read_excel("data/getaround_delay_analysis.xlsx")

# Je pose les données sur la table
df = load_data()

# Je jette les feuilles où il manque les heures (Nettoyage indispensable)
df_clean = df.dropna(subset=['delay_at_checkout_in_minutes', 'time_delta_with_previous_rental_in_minutes'])

# J'affiche le gros titre en haut de mon site web
st.title("Dashboard GetAround - Optimisation des Seuils")

# Je crée un menu déroulant pour choisir si on analyse les voitures Connect ou Mobile (Le "Scope")
scope = st.selectbox("Sélectionnez le Scope (Type de Checkin)", ["All", "Connect", "Mobile"])

# Si le manager choisit un truc précis, je filtre mon tableau de données
if scope != "All":
    df_clean = df_clean[df_clean['checkin_type'] == scope]

# Je crée le bouton glissant (de 0 à 720 minutes) pour tester le "Threshold" (le temps de pause)
threshold = st.slider("Seuil de battement minimum (en minutes)", 0, 720, 120)

# Si le temps de pause réel est plus petit que celui choisi par le manager, la voiture est bloquée (Impactée = Vrai)
df_clean['impacted'] = df_clean['time_delta_with_previous_rental_in_minutes'] < threshold

# J'affiche en gros sur l'écran le nombre de locations qu'on va bloquer avec ce choix
st.metric(label="Locations affectées (Perte de CA)", value=df_clean['impacted'].sum())

# Je dessine le graphique (Histogramme) pour montrer à quel point les gens sont en retard
fig = px.histogram(df_clean, x="delay_at_checkout_in_minutes", title=f"Distribution des retards ({scope})")

# J'accroche mon dessin sur la page web Streamlit
st.plotly_chart(fig)