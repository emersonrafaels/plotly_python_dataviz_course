from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from pages import page_sidebar
from pages import page_funil


# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col([dcc.Location(id="url"), page_sidebar.layout], md=2),
                dbc.Col([html.Div(id="page-content")], md=10),
            ]
        )
    ],
    fluid=True,
    style={"padding": "0px"},
    className="dbc",
)


# set the content according to the current pathname
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return html.P("Home page!")
    elif pathname == "/pd_funil":
        return page_funil.layout
    elif pathname == "/pd_ranking":
        return html.P("PD - Ranking das agências")

    # SE O USUÁRIO TENTAR ACESSAR UMA PÁGINA INEXISTENTE
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P("A página {} não foi encontrada...".format(pathname)),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
