from dash import Dash
from dash.html import Div, P, Br
from dash.dcc import Input as DCCInput
from dash.dependencies import Input, Output

# INICIANDO O APP
app = Dash(__name__)

# DEFININDO OS WIDGETS QUE ESTARÃO EM TELA
app.layout = Div(
    children=[
        DCCInput(id='meu_input1', value='Valor do input1'),
        Br(),
        P(id='output1'),
    ]
)

# DEFININDO O CALLBACK
"""

    DCC1: AO ALTERAR O OBJECT COM ID: MEU_INPUT1 (QUE É UM INPUT)
    
    O CHILDREN DO OBJECT COM ID: OUTPUT1 (QUE É UMA TAG HTML P)
    SOFRERÁ ALTERAÇÃO
    
    O CHILDREN RECEBERÁ O RETORNO DA FUNÇÃO DE CALLBACK.
    
"""

@app.callback(
    Output(component_id='output1', component_property='children'),
    Input(component_id='meu_input1', component_property='value')
)
def meu_callback(meu_input1):
    print(meu_input1)
    return (meu_input1,)


app.run_server()