import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import plotly.express as px 
import os
import pandas as pd


def get_df():
	return pd.read_csv("xxxx")



external_stylesheets =['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets)

app.layout = html.Div([

html.Button('Get data',id='get-data-button')
html.Button('Update data',id='update-data-button')
html.Button('predict data',id='predict-data-button')
dcc.Graph(id='graph')

])

df = get_df()




@app.callback(Output('graph','figure'),
		Input('update-data-button','n_clicks'))

def update_info():
	return get_df()


@app.callback(Output('graph','figure'),
		Input('get-data-button','n_clicks'))

def display_value (value):
	fig = px.scatter(df,x="x",y="y")
	fig.update_layout(transition_duration=500)
	return fig



if __name__ == '__main__':
	app.run_server(debug=True) 
