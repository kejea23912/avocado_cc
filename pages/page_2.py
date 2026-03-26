
import pandas as pd
from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc


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

options_regions = [
    {"label": region, "value": region}
    for region in sorted(df["region"].unique())
]


options_types = (
    [{"label": "  Tous", "value": "Tous"}]
    + [{"label": f"  {t}", "value": t} for t in sorted(df["type"].unique())]
)

REGION_DEFAUT = options_regions[0]["value"]
df_init = df[df["region"] == REGION_DEFAUT][COLONNES_AFFICHEES]

layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Card(
            children=[dbc.CardBody(children=[dbc.Row(
                            className="mb-3 align-items-end",
                            children=[
                                dbc.Col(
                                    xs=12, md=5,
                                    children=[
                                        html.Label(
                                            "Sélectionner une région :",
                                            style={
                                                "fontWeight": "bold",
                                                "fontSize": "13px",
                                                "marginBottom": "4px",}),
                                        dcc.Dropdown(
                                            id="p2-dropdown-region",
                                            options=options_regions,
                                            value=REGION_DEFAUT,
                                            clearable=False,
                                            style={"width": "100%"},),]),
                                dbc.Col(
                                    xs=12, md=5,
                                    children=[
                                        html.Label(
                                            "Sélectionner un type :",
                                            style={
                                                "fontWeight": "bold",
                                                "fontSize": "13px",
                                                "marginBottom": "4px",}),
                                        dcc.RadioItems(
                                            id="p2-radio-type",
                                            options=options_types,
                                            value="Tous",
                                            inline=True,      
                                            inputStyle={
                                                "marginRight": "4px",
                                                "cursor": "pointer",
                                            },
                                            labelStyle={
                                                "marginRight": "16px",
                                                "fontSize": "14px",
                                                "cursor": "pointer",},),]),
                                dbc.Col(
                                    xs=12, md=2,
                                    className="text-end",
                                    children=[
                                        dbc.Badge(
                                            id="p2-badge-lignes",
                                            children=f"Lignes : {len(df_init)}",
                                            color="primary",
                                            style={
                                                "fontSize": "14px",
                                                "padding": "8px 14px",
                                                "borderRadius": "6px",}),]),]),

                        dbc.Row(
                            dbc.Col(
                                dash_table.DataTable(
                                    id="p2-tableau",

                                    columns=[
                                        {"name": col, "id": col}
                                        for col in COLONNES_AFFICHEES
                                    ],

                                    data=df_init.to_dict("records"),

                                    sort_action="native",
                                    page_size=15,
                                    style_header={
                                        "backgroundColor": "#6e6e6e",
                                        "color": "white",
                                        "fontWeight": "bold",
                                        "textAlign": "left",
                                        "padding": "10px 12px",
                                        "border": "none",
                                    },
                                    style_cell={
                                        "textAlign": "left",
                                        "padding": "8px 12px",
                                        "fontFamily": "Arial, sans-serif",
                                        "fontSize": "13px",
                                        "border": "1px solid #dee2e6",
                                        "minWidth": "80px",
                                    },

                                    style_table={
                                        "overflowX": "auto",
                                        "borderRadius": "6px",
                                        "border": "1px solid #dee2e6",
                                    },

                                    style_data_conditional=[
                                        {
                                            "if": {"row_index": "odd"},
                                            "backgroundColor": "#D4D4D4",}],))),]),],
            style={
                "backgroundColor": "rgba(255, 255, 255, 0.93)",
                "borderRadius": "8px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.3)",
                "marginTop": "10px",
            }
        ),
    ]
)

