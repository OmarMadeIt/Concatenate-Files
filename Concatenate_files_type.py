import streamlit as st
import pandas as pd

# Définir le titre de l'application
st.title("Outil de Concaténation de Fichiers")

# Sélectionner le type de fichier
file_type = st.selectbox("Sélectionnez le type de fichier à charger", ["CSV", "TXT", "XLSX"])

# Charger les fichiers
st.header("Charger les fichiers")

uploaded_files = st.file_uploader("Sélectionnez les fichiers à charger", accept_multiple_files=True)

if not uploaded_files:
    st.warning("Veuillez sélectionner au moins un fichier.")
else:
    # Initialiser une liste pour stocker les DataFrames
    dataframes = []

    for uploaded_file in uploaded_files:
        if file_type == "CSV":
            data = pd.read_csv(uploaded_file, sep=";", on_bad_lines='skip', encoding='latin-1')
        elif file_type == "TXT":
            data = pd.read_csv(uploaded_file, delimiter="\t")
        elif file_type == "XLSX":
            data = pd.read_excel(uploaded_file, engine='openpyxl')

        dataframes.append(data)

    # Concaténer les DataFrames en un seul
    concatenated_df = pd.concat(dataframes, ignore_index=True)

    # Afficher le DataFrame concaténé
    st.header("Données Concaténées")
    st.write(concatenated_df)
    
st.download_button(
   "Télécharger le fichier",
   concatenated_df.to_csv(index=False, sep=';'),
   "file.csv",
   "text/csv",
   key='download-csv'
)
