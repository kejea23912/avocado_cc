import dash
from dash import  Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
 
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True 
)
from pages.page_1 import layout as page1_layout
 
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Comparaison entre région", href="/page1",       active="exact")),
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
    return page1_layout
  
if __name__ == "__main__":
    app.run(debug=True)