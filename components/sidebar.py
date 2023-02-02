import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *



from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd







# ========= Layout ========= #
layout = dbc.Col([
                html.H1("MyBudget" ,className = "text-primary"),
                html.P("By Yago Henrique", className="text-info"),
                html.Hr(),

            ])


dbc.Button(id='botao_avatar',
           children=[html.Img(src = '/assets/img_hom.png', id='avatar_change', className='perfil_name')])




# =========  Callbacks  =========== #
# Pop-up receita
