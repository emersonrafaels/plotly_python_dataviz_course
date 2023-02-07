from random import randint

from dash import Dash
from dash.html import Div, H1, P, H3
from dash.dcc import Graph, Dropdown, Slider, Checklist

# INICIANDO O APP
app = Dash(__name__)

# CRIANDO UM DATABASE
N = 20

# OBTENDO O DATABASE
database = {
    'index': list(range(N)),
    'maiores': [randint(1, 1000) for _ in range(N)],
    'menores': [randint(1, 1000) for _ in range(N)],
    'bebes': [randint(1, 1000) for _ in range(N)],
}

# DEFININDO CONFIGURAÇÕES ADICIONAIS
# NÃO APARECER O MODE BAR
config = {"displayModeBar": False}

app.layout = Div(
    children=[
        H1('Evento X'),
        H3('idade das pessoas que foram ao evento'),
        Dropdown(
            options=[
                {'label': 'Menores de Idade', 'value': 'menores'},
                {'label': 'Bebes', 'value': 'bebes'},
                {'label': 'Maiores de idade', 'value': 'maiores'}
            ],
            value='maiores'
        ),
        Slider(
            min=0,
            max=10,
            step=1,
            value=5
        ),
        Checklist(
            options=[
                {'label': 'Menores de Idade', 'value': 'menores'},
                {'label': 'Bebes', 'value': 'bebes'},
                {'label': 'Maiores de idade', 'value': 'maiores'}
            ]
        ),
        Graph(
            id="example-graph-line",
            config=config,
            figure={
                'data': [
                    {
                        'y': database['maiores'],
                        'x': database['index'],
                        'name': 'Maiores'
                    },
                ],
            }
        )
    ]
)


app.run_server(debug=True)