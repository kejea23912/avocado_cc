
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc

df = pd.read_csv("datas/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])

REGIONS_FIXES = [
    "MidSouth",
    "Northeast",
    "SouthCentral",
    "Southeast",
    "TotalUS",
    "West",
]

options_regions = [
    {"label": region, "value": region}
    for region in sorted(df["region"].unique())
]


REGION_DEFAUT = "Albany"

layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Card(
            children=[
                dbc.CardHeader(
                    html.H4(
                        "Quantités vendues (Total Volume)",
                        className="mb-0",
                        style={"color": "white", "fontWeight": "bold"},
                    ),
                    style={"backgroundColor": "#0d6efd"},
                ),
                dbc.CardBody(
                    dbc.Row(
                        children=[

                            dbc.Col(
                                xs=12, md=6,
                                children=[
                                    dcc.Graph(
                                        id="graphique-regions-fixes",
                                        # Contenu rempli au chargement par le callback
                                        config={"displayModeBar": False},
                                        style={"height": "450px"},
                                    )
                                ]
                            ),
                            dbc.Col(
                                xs=12, md=6,
                                children=[

                                    dbc.Badge(
                                        "Sélectionnez une région :",
                                        color="primary",
                                        style={
                                            "fontSize": "14px",
                                            "padding": "8px 16px",
                                            "marginBottom": "8px",
                                            "display": "block",
                                            "textAlign": "center",
                                            "backgroundColor": "#6f42c1",  # violet comme dans le sujet
                                        }
                                    ),
                                    dbc.Select(
                                        id="select-region",
                                        options=options_regions,
                                        value=REGION_DEFAUT,
                                        style={
                                            "marginBottom": "12px",
                                            "borderRadius": "4px",
                                        }
                                    ),

                                    # ── Graphique région dynamique ───
                                    dcc.Graph(
                                        id="graphique-region-select",
                                        config={"displayModeBar": False},
                                        style={"height": "380px"},
                                    ),
                                ]
                            ),
                        ]
                    )
                ),
            ],
            style={
                "backgroundColor": "rgba(255, 255, 255, 0.92)",
                "borderRadius": "8px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.3)",
                "marginTop": "10px",
            }
        ),
    ]
)
