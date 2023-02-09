from datetime import datetime
from random import randint

from dash import Dash
from dash.html import Div, H1, P, H3
from dash.dcc import Graph, Dropdown, Slider, Checklist
from dash.dependencies import Input, Output

def get_data(number_instances=10):

    database = {
        'index': list(range(number_instances)),
        'maiores': [randint(1, 1000) for _ in range(number_instances)],
        'menores': [randint(1, 1000) for _ in range(number_instances)],
        'bebes': [randint(1, 1000) for _ in range(number_instances)],
    }

    return database

# INICIANDO O APP
app = Dash(__name__)

# OBTENDO OS DADOS
database = get_data(number_instances=30)

# DEFININDO OS WIDGETS QUE ESTARÃO EM TELA
app.layout = Div(
    children=[
        H1('Evento {}'.format(datetime.today().year)),
        H3('Escolha a faixa de idade que deseja analisar'),
        Checklist(
            id='meu_check_list',
            options=[
                {'label': 'Menores de Idade', 'value': 'menores'},
                {'label': 'Bebes', 'value': 'bebes'},
                {'label': 'Maiores de idade', 'value': 'maiores'}
            ],
            value=['bebes'] # Default
        ),
        H3('Escolha o tipo de gráfico desejado'),
        Dropdown(
            id='meu_dropdown',
            options=[
                {'label': 'Linha', 'value': 'line'},
                {'label': 'Barra', 'value': 'bar'},
            ],
            value='line' # Default
        ),
        Graph(
            id='meu_grafico',
            config={'displayModeBar': False},
        )
    ]
)

# DEFININDO O CALLBACK
@app.callback(
    Output('meu_grafico', 'figure'),
    [
        Input('meu_check_list', 'value'),
        Input('meu_dropdown', 'value'),
    ]
)
def my_callback(input_data, graph_type):

    # INICIANDO O GRÁFICO COM DADOS VÁZIOS
    grafico = {
        'data': []
    }

    # PERCORRENDO OS DADOS DESEJADOS PELO CLIENTE
    # O TIPO DE GRÁFICO TAMBÉM É UM INPUT DO CLIENTE
    for x in input_data:
        grafico['data'].append(
            {
                'y': database[x],
                'x': database['index'],
                'name': x,
                'type': graph_type
            },
        )
    return grafico

app.run_server(debug=True)