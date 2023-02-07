from random import randint

from dash import Dash
from dash.html import Div, H1, P, H3
from dash.dcc import Graph

import plotly.express as px

# DEFININDO O CSS
external_stylesheets = [
    "https://unpkg.com/terminal.css@0.7.2/dist/terminal.min.css",
]

# INICIANDO O APP
app = Dash(__name__, external_stylesheets=external_stylesheets)

# CRIANDO UM DATABASE
N = 20

# OBTENDO O DATABASE
database = {"index": list(range(N)), "maiores": [randint(1, 1000) for _ in range(N)]}

# CRIANDO O LINE PLOT
fig_line = px.line(x=database["index"],
                   y=database["maiores"],
                   markers=True,
                   title="Example - Line Plot")

# CRIANDO O BOXPLOT
fig_box = px.box(database, y="maiores", points="all")


# CONSTRUINDO O DASH
app.layout = Div(
    children=[
        H1("Olá mundo"),
        P("Bem vindo ao Dash"),
        H3("Line Plot"),
        Graph(
            id="example-graph-line",
            figure=fig_line,
        ),
        H3("Box Plot"),
        Graph(
            id="example-graph-box",
            figure=fig_box,
        ),
    ]
)

# INICIANDO O SERVIDOR
app.run_server(debug=True)
