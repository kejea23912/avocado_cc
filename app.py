import dash
from dash import  Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
 
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True 
)
from pages.page_1 import layout as page1_layout
from pages.page_2 import layout as page2_layout

import pages.page_1_cb
import pages.page_2_cb

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Comparaison entre région", href="/",       active="exact")),
        dbc.NavItem(dbc.NavLink("Affichage des données",    href="/page2",  active="exact")),
        dbc.NavItem(dbc.NavLink("Aide en ligne",            href="/page3",  active="exact")),
    ],
    brand="Application des M1 MECEN",
    brand_href="/",
    color="primary",
    dark=True,
    className="mb-3",
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    """Retourne le layout correspondant à l'URL."""
    if pathname == "/page2":
        return page2_layout
    else:
        return page1_layout
  
if __name__ == "__main__":
    app.run(debug=True)