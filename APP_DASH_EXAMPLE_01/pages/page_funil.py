import dash
import dash.dcc as dcc
import dash.html as html
import dash_bootstrap_components as dbc
import dash_ag_grid as dag

from dynaconf import settings

from app import *
from utils.pandas_functions import load_data

# DIRETÓRIO DE DADOS DO DATASET DE AGÊNCIAS
dir_data = settings.DATA_DIR_AGENCIAS

# CARREGANDO OS DADOS
df = load_data(dir_data)

# LAYOUT
layout = html.Div(
    children=[
        html.H1(children=""),
        # DATATABLE
        dash.dash_table.DataTable(
            id="typing_formatting",
            data=df.to_dict("records"),
            # FORMATANDO AS COLUNAS
            columns=[
                {"id": "CÓDIGO AG", "name": "CÓDIGO DA AGÊNCIA", "type": "numeric"},
                {"id": "UF", "name": "UF", "type": "text"},
            ],
            # OPÇÃO PARA SELEÇÃO DE LINHAS
            row_selectable="single",
            # OPÇÃO PARA DELETAR LINHAS
            row_deletable=False,
            # OPÇÃO PARA EDITAR VALORES
            editable=False,
            # OPÇÃO PARA FILTRAR
            filter_action="native",
            # OPÇÃO PARA ORDENA
            sort_action="native",
            # FORMATAÇÃO DE ESTILO DAS CÉLULAS
            style_cell={"textAlign": "center"},
            # FORMATAÇÃO DE ESTILO DA TABELA
            style_table={"overflowX": "auto"},
            style_data_conditional=[
                {
                    "if": {"column_editable": False},
                    "backgroundColor": "rgb(30, 30, 30)",
                    "color": "white",
                }
            ],
            style_header_conditional=[
                {
                    "if": {"column_editable": False},
                    "backgroundColor": "rgb(30, 30, 30)",
                    "color": "white",
                }
            ],
            css=[
                {
                    "selector": ".dash-spreadsheet td div",
                    "rule": """
                                                line-height: 15px;
                                                max-height: 30px; min-height: 30px;
                                                display: block;
                                                overflow-y: hidden;
                                            """,
                }
            ],
            tooltip_data=[
                {
                    column: {"value": str(value), "type": "markdown"}
                    for column, value in row.items()
                }
                for row in df.to_dict("records")
            ],
            tooltip_duration=None,
        )
    ]
)
