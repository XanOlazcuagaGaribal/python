import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os  
from pathlib import Path

st.title("Visualisation interactive de données")

st.header("Choisir un dataset dans la liste ci dessous")

# Récupération des fichiers dans le dossier actuel
def file_selector(folder_path='./Data'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Choisir un fichier', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('Vous avez choisi `%s`' % filename)

# Lire le fichier
df = pd.read_csv(filename)

# Affichage du dataset
if st.checkbox("Afficher le dataset"):
	number = int(st.number_input("Nombre de lignes à afficher"))
	st.dataframe(df.head(number))

# Afficher le nom des colonnes 
if st.checkbox("Afficher le nom des colonnes"):
    st.write(df.columns)

# Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées
if st.checkbox("Sélectionner les colonnes pour afficher leur type"):
	all_columns = df.columns.tolist()
	selected_columns = st.multiselect("Select",all_columns)
	new_df = df[selected_columns]
	st.write(new_df.dtypes)

# La shape du dataset, par lignes et par colonnes
if st.checkbox("Shape du Dataset"):
	data_dim = st.radio("Afficher les dimensions par ",("Lignes","Colonnes"))
	if data_dim == 'Lignes':
		st.text("Nombre de lignes")
		st.write(df.shape[0])
	elif data_dim == 'Colonnes':
		st.text("Nombre de colonnes")
		st.write(df.shape[1])
	else:
		st.write(df.shape)

# Afficher les statistiques descriptives du dataset 
if st.checkbox("Afficher les statistiques descriptives"):
    st.write(df.describe())

# Affichage de différents graphiques
# Heatmap de corrélation 
if st.checkbox("Matrice de corrélation"):
    st.write(sns.heatmap(df.corr(),annot=True))
    st.pyplot()
		
