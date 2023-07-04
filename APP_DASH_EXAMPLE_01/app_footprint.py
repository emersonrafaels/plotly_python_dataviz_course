from datetime import datetime as dt

import dash
import dash.dcc as dcc
import dash.html as html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

from dash.dependencies import Input, Output
from plotly import graph_objs as go
from plotly.graph_objs import *


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "APP - Footprint - PD"
server = app.server

# Layout of Dash App
APP_LOGO = app.get_asset_url('itau.png')

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)

sidebar = html.Div(
    [
        html.Div(
            [
                # width: 3rem ensures the logo is the exact width of the
                # collapsed sidebar (accounting for padding)
                html.Img(src=APP_LOGO, style={"width": "3rem"}),
                html.H2("Footprint - PD"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fa-solid fa-house"),
                     html.Span("Home", className="text-side-bar")
                     ],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-filter"),
                        html.Span("Funil", className="text-side-bar"),
                    ],
                    href="/pd_funil",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-ranking-star"),
                        html.Span("Ranking", className="text-side-bar"),
                    ],
                    href="/pd_ranking",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

content = html.Div(id="page-content", className="content")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# set the content according to the current pathname
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return html.P("Home page!")
    elif pathname == "/pd_funil":
        return html.P("PD - Funil")
    elif pathname == "/pd_ranking":
        return html.P("PD - Ranking das agências")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P("A página {} não foi encontrada...".format(pathname)),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == "__main__":
    app.run_server(debug=True)