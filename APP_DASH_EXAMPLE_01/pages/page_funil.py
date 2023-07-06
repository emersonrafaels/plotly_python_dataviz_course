import random

import pandas as pd
import numpy as np

import dash
import dash.dcc as dcc
import dash.html as html
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import plotly.express as px

from dynaconf import settings

from app import *
from utils.pandas_functions import load_data, dataframe_convert_dtypes_to_aggrid

# DIRETÓRIO DE DADOS DO DATASET DE AGÊNCIAS
dir_data = settings.DATA_DIR_AGENCIAS

def create_data_funnel():

    N_SAMPLES = 500

    list_funnel = ["FUNNEL {}".format(str(np.random.randint(0, 7))) for _ in range(N_SAMPLES)]
    list_index_location = random.sample(range(10000), N_SAMPLES)

    dict_type_funnel = {"FUNNEL 1": "Potencial Encerramento",
                        "FUNNEL 2": "Ags Reformadas (PD + EI)",
                        "FUNNEL 3": "Remanejamento (Imóvel antigo)",
                        "FUNNEL 4": "AVCB Crítico",
                        "FUNNEL 5": "Itaú Rent",
                        "FUNNEL 6": "Ags que serão reformadas (PD + EI)",
                        "PD": "Saldo PD"}

    list_funnel_updated = ["PD" if value == "FUNNEL 0" else value for value in list_funnel]

    df = pd.DataFrame({"LOCATION": list_index_location, "GROUP FUNNEL": list_funnel_updated})

    df['GROUP FUNNEL LABEL'] = df['GROUP FUNNEL'].replace(dict_type_funnel)

    df_groupby_count_funnel = df.groupby(["GROUP FUNNEL", "GROUP FUNNEL LABEL"]).size().reset_index(name="QUANTIDADE")

    return df, df_groupby_count_funnel

# CARREGANDO OS DADOS
df = load_data(dir_data)
df_funnel, df_groupby_count_funnel = create_data_funnel()

# BARPLOT
fig_barplot = px.bar(df_groupby_count_funnel,
                     x="GROUP FUNNEL",
                     y="QUANTIDADE",
                     color="GROUP FUNNEL LABEL",
                     text_auto=True,
                     labels={"GROUP FUNNEL LABEL": "GRUPO FUNIL"})

# FORMATANDO O DATATABLE COM AGGRID
grid = dag.AgGrid(
    id="data_grid_funil",
    columnDefs=[
        {"field": column, "filter": field_type}
        for column, field_type in dataframe_convert_dtypes_to_aggrid(df).items()
    ],
    rowData=df.to_dict("records"),
    dashGridOptions={
        "resizable": True,
        "pagination": True,
        "sortable": True,
        "filter": True,
        "animateRows": True,
    },
    className="ag-theme-alpine",
    defaultColDef={"sortable": True},
    csvExportParams={
        "fileName": "BASE_FOOTPRINT_RESULTADO_FUNIL.csv",
    },
)

# LAYOUT
layout = html.Div(
    children=[
        html.Div(
            children=[
                # TÍTULO
                html.H1(children="Resultado - Modelo do Funil"),
                # DATATABLE
                grid,
                # LINHA SEPARADORA
                html.Hr(),
                # BOTÃO DE DOWNLOAD
                html.Button(
                    "Download Excel",
                    id="excel-button",
                    n_clicks=0,
                    className="btn btn-outline-primary",
                ),
                dcc.Download(id="download-dataframe-xlsx"),
            ],
            style={"margin-top": 20, "margin-right": 20},
        ),
        html.Div(
            children=[
                # TÍTULO
                html.H1(children="Resultado - Quantidade de ag. por etapa do funil"),
                # GRÁFICO DE BARRAS
                dcc.Graph(figure=fig_barplot),
            ],
            style={"margin-top": 20, "margin-right": 20},
        ),
    ]
)

# CRIANDO CALLBACK PARA DOWNLOAD DOS DADOS DA TABELA (data_grid_funil)
@app.callback(
    dash.Output("download-dataframe-xlsx", "data"),
    dash.Input("excel-button", "n_clicks"),
    prevent_initial_call=True,
)
def export_data_as_csv(n_clicks):
    if n_clicks:
        return dcc.send_data_frame(
            df.to_excel,
            "BASE_FOOTPRINT_RESULTADO_FUNIL.xlsx",
            sheet_name="RESULTADO_FOOTPRINT",
            index=None,
        )
    return False
