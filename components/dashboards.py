from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *




# =========  Layout  =========== #
layout = dbc.Col([
        html.H1("MyBudget" ,className = "text-primary"),
        html.P("By Yago Henrique", className="text-info"),
        html.Hr(),
    ])



# =========  Callbacks  =========== #
