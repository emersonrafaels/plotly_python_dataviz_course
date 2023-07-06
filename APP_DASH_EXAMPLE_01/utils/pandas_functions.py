import pandas as pd


def load_data(data_dir):

    # REALIZANDO A LEITURA DOS DADOS
    df = pd.read_excel(data_dir)

    return df


def get_indicators_before_versus_after(
    df1, df2, column_on="CÓDIGO AG", name_column_indicator="CRUZAMENTO"
):
    # REALIZANDO O JOIN ENTRE OS DATAFRAMES
    df_join = pd.merge(
        df1, df2, on=column_on, how="inner", suffixes=("_antes", "_depois")
    )

    return df_join


def filter_columns_multiselect(colunas_desejadas, df_columns):

    colunas_desejadas_antes_depois = []

    for column in colunas_desejadas:
        colunas_desejadas_antes_depois.append(str(column))
        colunas_desejadas_antes_depois.append("{}{}".format(str(column), "_antes"))
        colunas_desejadas_antes_depois.append("{}{}".format(str(column), "_depois"))

    colunas_desejadas_filter = list(
        filter(lambda x: x in df_columns, colunas_desejadas_antes_depois)
    )
    return colunas_desejadas_filter
