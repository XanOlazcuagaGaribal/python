import streamlit as st
import pandas as pd
import numpy as np
import os  
from pathlib import Path

st.title("Visualisation interactive de données")

st.header("Choisir un dataset dans la liste ci dessous")

#Récupération des fichiers dans le dossier actuel
def file_selector(folder_path='./Data'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Choisir un fichier', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('Vous avez choisi `%s`' % filename)

# Lire le fichier
df = pd.read_csv(filename)

#Affichage du dataset
if st.checkbox("Afficher le dataset"):
	number = st.number_input("Nombre de lignes à afficher")
	st.dataframe(df.head(number))