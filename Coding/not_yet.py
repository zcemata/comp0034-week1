# Import the required packages
from dash import Dash, html
import dash_bootstrap_components as dbc

# Creates the Dash app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Creates the HTML page layout and adds it to the app. This uses dash.html package to add HTML components.
app.layout = dbc.Container(
    children=[
        html.H1(children='NOT YET', className="display-1"),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
