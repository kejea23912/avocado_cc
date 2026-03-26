
import pandas as pd
import plotly.graph_objects as go
from dash import Input, Output


import dash
app = dash.get_app()


df = pd.read_csv("datas/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])


REGIONS_FIXES = [
    "Midsouth",
    "Northeast",
    "SouthCentral",
    "Southeast",
    "TotalUS",
    "West",
]

COULEURS = [
    "#e90013",  
    "#10b19e", 
    "#d6a21c",  
    "#e06602",  
    "#0578A5",  
    "#0fe0e7",  
]



@app.callback(
    Output("graphique-regions-fixes", "figure"),
    Input("select-region", "value"),)


def afficher_regions_fixes(_):
    """
    Construit le graphique des 6 régions fixes.
    Une ligne par région, toutes affichées simultanément.
    La valeur du select n'est pas utilisée ici.
    """
    fig = go.Figure()

    for region, couleur in zip(REGIONS_FIXES, COULEURS):
        df_region = (
            df[df["region"] == region]
            .groupby("Date", as_index=False)["Total Volume"]  
            .sum() 
            .sort_values("Date")
        )

        fig.add_trace(
            go.Scatter(
                x=df_region["Date"],
                y=df_region["Total Volume"],
                mode="lines",
                name=region,
                line=dict(color=couleur, width=1.5),
            )
        )

    fig.update_layout(
        title=dict(
            text="Quantités vendues - Régions principales",
            font=dict(size=12),
        ),
        xaxis=dict(
            title="Date",
            showgrid=True,
            gridcolor="#e9ecef",
        ),
        yaxis=dict(
            title="Volume total",
            showgrid=True,
            gridcolor="#e9ecef",
        ),
        legend=dict(
            title="Région",
            font=dict(size=10),
            bgcolor="rgba(255,255,255,0.7)",
        ),
        plot_bgcolor="white",
        paper_bgcolor="rgba(0,0,0,0)",  
        margin=dict(l=50, r=20, t=50, b=50),
    )

    return fig



@app.callback(
    Output("graphique-region-select", "figure"),
    Input("select-region", "value"),
)
def afficher_region_selectionnee(region):
    """
    Construit le graphique de la région choisie dans le Select.
    Affiche l'évolution du Total Volume dans le temps.
    """
   
    df_region = (
    df[df["region"] == region]
    .groupby("Date", as_index=False)["Total Volume"]  
    .sum()                                             
    .sort_values("Date")
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_region["Date"],
            y=df_region["Total Volume"],
            mode="lines",
            name=region,
            line=dict(color="#0d6efd", width=1.5),
            fill="tozeroy",                         
            fillcolor="rgba(13, 110, 253, 0.1)",
        )
    )

    fig.update_layout(
        title=dict(
            text=f"Quantités vendues - {region}",
            font=dict(size=12),
        ),
        xaxis=dict(
            title="Date",
            showgrid=True,
            gridcolor="#e9ecef",
        ),
        yaxis=dict(
            title="Volume total",
            showgrid=True,
            gridcolor="#e9ecef",
        ),
        plot_bgcolor="white",
        paper_bgcolor="rgba(0,0,0,0)",  
        margin=dict(l=50, r=20, t=50, b=50),
        showlegend=False,
    )

    return fig
