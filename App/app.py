import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os  
from pathlib import Path

st.set_option('deprecation.showPyplotGlobalUse', False)

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
    heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True)
    heatmap.set_title('Heatmap de corrélation', fontdict={'fontsize':12}, pad=12)
    st.write(heatmap)
    st.pyplot()
    
		
# Graphique en barre

if st.checkbox("Diagramme en bar"):
    all_columns_names = df.columns.tolist()
    primary_col = st.selectbox("Choisir la variable",all_columns_names)

    if st.button("Diagramme"):
        st.text("Création du diagramme")
        plt.figure(figsize=(30,10))
        plot = sns.displot(df,x=primary_col)
        st.write(plot)
        st.pyplot()
        

# Diagrammes personnalisés

st.subheader("Diagrammes personnalisés")
all_columns_names = df.columns.tolist()
type_of_plot = st.selectbox("Choisir le type de diagramme",["area","bar","line","hist","box","kde"])
selected_columns_names = st.multiselect("Choisir les colonnes pour le diagramme",all_columns_names)

if st.button("Générer le diagramme"):
	st.success("Génération du diagramme {} pour {}".format(type_of_plot,selected_columns_names))

		# Plot By Streamlit
	if type_of_plot == 'area':
		cust_data = df[selected_columns_names]
		st.area_chart(cust_data)

	elif type_of_plot == 'bar':
		cust_data = df[selected_columns_names]
		st.bar_chart(cust_data)

	elif type_of_plot == 'line':
		cust_data = df[selected_columns_names]
		st.line_chart(cust_data)

		# Custom Plot 
	elif type_of_plot:
		cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
		st.write(cust_plot)
		st.pyplot()
