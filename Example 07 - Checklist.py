from dash import Dash
from dash import dcc
from dash import html

# INICIANDO O APP
app = Dash(__name__)

# DEFININDO OS WIDGETS QUE ESTARÃO EM TELA
app.layout = html.Div(
    children=[
        dcc.Checklist(
           options=[
               {'label': 'New York City', 'value': 'New York City'},
               {'label': 'Montreal', 'value': 'Montreal'},
               {'label': 'San Francisco', 'value': 'San Francisco'},
           ],
           value=['Montreal']
        )
    ]
)

app.run_server(debug=True)