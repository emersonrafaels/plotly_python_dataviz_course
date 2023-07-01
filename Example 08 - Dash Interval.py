from datetime import datetime
from random import randint

from dash import Dash
from dash.html import Div, H1, P, H3
from dash.dcc import (
    Graph, Dropdown, Slider,
    Checklist, Interval
)
from dash.dependencies import Input, Output

# INICIANDO O APP
app = Dash(__name__)

# QUANTIDADE DAS INSTÂNCIAS
N = 20

# INICIANDO O DATABASE QUE ARMAZENARÁ OS DADOS
database = {
    'index': [],
    'maiores': [],
    'menores': [],
    'bebes': [],
}

# DEFININDO OS WIDGETS QUE ESTARÃO EM TELA
app.layout = Div(
    children=[
        H1('Evento {}'.format(datetime.today().year)),
        H3('idade das pessoas que foram ao evento'),
        Interval(id='interval'),
        Checklist(
            id='meu_check_list',
            options=[
                {'label': 'Menores de Idade', 'value': 'menores'},
                {'label': 'Bebes', 'value': 'bebes'},
                {'label': 'Maiores de idade', 'value': 'maiores'}
            ],
            value=['bebes']
        ),
        Dropdown(
            id='meu_dropdown',
            options=[
                {'label': 'Linha', 'value': 'line'},
                {'label': 'Barra', 'value': 'bar'},
            ],
            value='line'
        ),
        Graph(
            id='meu_grafico',
            config={'displayModeBar': False},
        )
    ]
)


def update_database(value):
    """Minha query / Atualização do pandas."""
    database['index'].append(value)
    database['menores'].append(randint(1, 200))
    database['maiores'].append(randint(1, 200))
    database['bebes'].append(randint(1, 200))


@app.callback(
    Output('meu_grafico', 'figure'),
    [
        Input('meu_check_list', 'value'),
        Input('meu_dropdown', 'value'),
        Input('interval', 'n_intervals'),
    ]
)
def my_callback(input_data, graph_type, n_intervals):

    # ATUALIZANDO O DATABASE
    update_database(n_intervals)

    # INICIANDO O GRÁFICO COM DADOS VÁZIOS
    grafico = {
        'data': []
    }

    # PERCORRENDO OS DADOS DESEJADOS PELO CLIENTE
    # O TIPO DE GRÁFICO TAMBÉM É UM INPUT DO CLIENTE
    for x in input_data:
        grafico['data'].append(
            {
                'y': database[x][-20:],
                'x': database['index'][-20:],
                'name': x,
                'type': graph_type
            },
        )
    return grafico

app.run_server(debug=True)