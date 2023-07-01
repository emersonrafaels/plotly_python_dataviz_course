# plotly.py

## Iniciando

pip install plotly

```python
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.show()
```

## Sobre

[plotly.py](https://plotly.com/python/) é uma biblioteca interativa, open source (possuem um módulo entreprise, porém vamos aprender com suas features open source) e que permite visualização de gráficos interativos diretamente no browser.


Feito sobre [plotly.js](https://github.com/plotly/plotly.js), `plotly.py` cria gráficos de alto nível, com mais de 30 tipos de gráficos (com desenvolvimento continuo), incluindo gráficos científicos, gráficos 3D, gráficos estatítsticos, SVG maps, gráficos financeiros e muito mais.

`plotly.py` é [MIT Licensed](https://github.com/plotly/plotly.py/blob/master/LICENSE.txt). Plotly pode ser usado em Jupyter notebooks, standalone HTML files ou integrado em dashboards [Dash applications](https://dash.plotly.com/).

<p align="center">
    <a href="https://plotly.com/python/" target="_blank">
    <img src="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/plotly_2017.png">
</a></p>

# Arquivos desse repositório

    - Example 01 - Line and Box Plot
        - Importar external CSS style
        - Importar dash html componentes (dhc)
        - Importar dash core componente (dcc)
        - Criando uma div
        - Criando um line plotly
        - Criando um bar plotly
        - Incluir gráficos plotly em uma dash
        
    - Example 02 - Display Mode Bar
        - Remover mode bar dos gráficos
    
    - Example 03 - Creating DCC Components
        - Uso de dropdown
        - Uso de slider
        - Uso de checklist
        - Uso do dash table
    
    - Example 04_i - Creating one callback with one return
        - Uso de callbacks: Um valor de input e um valor de return
    
    - Example 04_ii - Creating one callback with two returns
        - Uso de callbacks: Um valor de input e dois valores de return
    
    - Example 05 - Creating one callback with two inputs and two returns
        - Uso de callbacks: Dois valores de input e dois valores de return
        
    - Example 06 - Dash React
        - Uso de dropdown
        - Uso de checklist
        - Atualização de um gráfico plotly, dado o input do checklist e dropdown
            - Checklist: Atualiza os dados que são mostrados
            - Dropdown: Escolhe qual o tipo de gráfico irá ser mostrado.