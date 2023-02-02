from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from app import *
from components import sidebar, dashboards, extratos




# =========  Layout  =========== #
content = html.Div(id="page-content")
 
 

app.layout = dbc.Container(children=[
dbc.Row([
dbc.Col([
    dcc.Location(id='url'),
    sidebar.layout]          # estou trazendo o layout da pasta sidebar 
, md=2, style={'background-color':'red','height':'1080px'}),                   #o md=2 é uma formula bootstrap onde eu vou ocupar dois espaços de 12 dentro do nosso projeto 
    
    dbc.Col([
    content]
    , md=10, style={'background-color':'blue','height':'1080px'})
])

], fluid=True,) #essa fluid=true significa que o conteudo vai se espalhar em relação ao tamanho da tela 


 
@app.callback(Output('page-content','children'),[Input('url','pathname')]) #função que vai disparar o evento
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout
    
    if pathname == '/extratos':
        return extratos.layout


if __name__ == '__main__':
    app.run_server(port=8051, debug=True) #se debug for igual a true vai aparecer diretamente no meu projeto, se for false eu tenho que dar um refresh na pagina 

