

import pandas as pd
from dash import Input, Output


import dash
app = dash.get_app()


df = pd.read_csv("datas/avocado.csv")


COLONNES_EXCLUES = [
    "Unnamed: 0",
    "4046",
    "4225",
    "4770",
    "Small Bags",
    "Large Bags",
    "XLarge Bags",
]

COLONNES_AFFICHEES = [col for col in df.columns if col not in COLONNES_EXCLUES]


@app.callback(
    Output("p2-tableau",       "data"),      
    Output("p2-badge-lignes",  "children"),  
    Input("p2-dropdown-region", "value"),    
    Input("p2-radio-type",      "value"),    
)
def filtrer_tableau(region, type_avocat):
    """
    Filtre le DataFrame selon :
    - la région choisie dans le Dropdown
    - le type choisi dans les RadioItems (Tous / conventional / organic)

    Retourne :
    - les données filtrées pour le DataTable
    - le texte mis à jour pour le Badge (ex: "Lignes : 169")
    """

    df_filtre = df[df["region"] == region]

    if type_avocat != "Tous":
        df_filtre = df_filtre[df_filtre["type"] == type_avocat]

    data_filtree = df_filtre[COLONNES_AFFICHEES].to_dict("records")

    nb_lignes = len(df_filtre)
    texte_badge = f"Lignes : {nb_lignes}"

    return data_filtree, texte_badge
