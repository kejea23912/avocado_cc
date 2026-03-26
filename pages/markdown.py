

from dash import html, dcc
import dash_bootstrap_components as dbc

def lire_markdown(nom_fichier):
    """Lit un fichier .md et retourne son contenu en string."""
    try:
        with open(f"markdowns/{nom_fichier}", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f" Fichier {nom_fichier} introuvable dans markdowns/"

contenu_md1 = lire_markdown("expli1.md")
contenu_md2 = lire_markdown("expli2.md")
contenu_md3 = lire_markdown("expli3.md")


layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Card(
            children=[
                dbc.CardHeader(
                    html.H4(
                        "PRÉSENTATION DE DASH",
                        className="mb-0",
                        style={
                            "color": "white",
                            "fontWeight": "bold",
                            "textAlign": "center",
                            "letterSpacing": "2px",
                        }
                    ),
                    style={
                        "backgroundColor": "#0d6efd",  
                        "padding": "16px",
                    }
                ),
                dbc.CardBody(
                    children=[
                        dbc.Tabs(
                            children=[
                                dbc.Tab(
                                    label="Accueil",
                                    tab_id="tab-1",
                                    children=[
                                        dcc.Markdown(
                                            contenu_md1,
                                            dangerously_allow_html=False,
                                            style={"color": "white",
                                                "padding": "20px",
                                                "backgroundColor": "#2c2c2c",
                                            }
                                        )
                                    ],
                                ),
                                dbc.Tab(
                                    label="Layout",
                                    tab_id="tab-2",
                                    children=[
                                        dcc.Markdown(
                                            contenu_md2,
                                            dangerously_allow_html=False,
                                            style={
                                                "padding": "20px",
                                                "backgroundColor": "#2c2c2c",
                                            }
                                        )
                                    ],
                                ),
                                dbc.Tab(
                                    label="CallBack",
                                    tab_id="tab-3",
                                    children=[
                                        dcc.Markdown(
                                            contenu_md3,
                                            dangerously_allow_html=False,
                                            style={
                                                "padding": "20px",
                                                "backgroundColor": "white",
                                            }
                                        )
                                    ],
                                ),
                            ],
                            active_tab="tab-1",
                            style={"marginBottom": "0px"},
                        ),
                    ],
                    style={"padding": "0px"},  
                ),
            ],
            style={
                "backgroundColor": "rgba(255, 255, 255, 0.95)",
                "borderRadius": "8px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.3)",
                "marginTop": "10px",
                "overflow": "hidden",
            }
        ),
    ]
)
