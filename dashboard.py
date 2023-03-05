import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash import Dash, html, Input, Output, ctx

app_path = str(pathlib.Path(__file__).parent.resolve())
csv = ['a_1.csv', 'b_1.csv', 'c_1.csv']
titles = ['Walking', 'Up_down_walking', 'Jumping']
titles_num = 0
app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Accelerometer data'),
                ],
            ),
        ],
    )


def build_graph(num=0):
    df = pd.read_csv(os.path.join(app_path, os.path.join("data", csv[num])))
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df.iloc[:,0],
                    'y': df.iloc[:,1],
                    'name': 'Acc X',
                    'marker': {'size': 12}
                },
                {
                    'x': df.iloc[:,0],
                    'y': df.iloc[:,2],
                    'name': 'Acc Y',
                    'marker': {'size': 12}
                },
                {
                    'x': df.iloc[:,0],
                    'y': df.iloc[:,3],
                    'name': 'Acc Z',
                    'marker': {'size': 12}
                },
                {
                    'x': df.iloc[:,0],
                    'y': df.iloc[:,4],
                    'name': 'Gyr X',
                    'marker': {'size': 12}
                },
                {
                    'x': df.iloc[:,0],
                    'y': df.iloc[:,5],
                    'name': 'Gyr Y',
                    'marker': {'size': 12}
                },
                {
                    'x': df.iloc[:,0],
                    'y': df.iloc[:,6],
                    'name': 'Gyr Z',
                    'marker': {'size': 12}
                },
                
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                },
                'xaxis':{
                    'title': 'Timestamp, ms'
                },
                'yaxis':{
                    'title': 'Data'
                },
                'title': titles[num]   
            }
        }
    )


def add_buttons():
    return html.Div([
        html.Button(
            'Previous', id='to_left', n_clicks=0
        ),
        html.Button(
            'Next', id='to_right', n_clicks=0
        ),  
    ])


@app.callback(
    Output('graph', 'children'),
    Input('to_left', 'n_clicks'),
    Input('to_right', 'n_clicks'),
)
def displayClick(btn1, btn2):

    num = (btn2 - btn1) % len(csv)

    return build_graph(num=num)


app.layout = html.Div([
        html.Div(
            className='big-app-container',
            children=[
                build_banner(),
                html.Div(
                    className='app-container',
                    children=[
                        html.Div(id='graph'),
                    ]
                )
            ]
        ),
        add_buttons()  
    ]
)

