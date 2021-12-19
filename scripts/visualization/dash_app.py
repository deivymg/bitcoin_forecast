import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import plotly.express as px 
import os
import pandas as pd


"""
def actualizar_df():
	make data_acquisition
"""

def get_df():
	data_path =os.path.join( os.environ['BINANCE_RAW_PATH'],"ultimos_15_minutos.csv")
	df = pd.read_csv(data_path)
	return df


app = dash.Dash(__name__) #, external_stylesheets)

app.layout = html.Div([
    html.H1('BITCOIN FORECAST'),
    dcc.Checklist(
        id='toggle-rangeslider',
        options=[{'label': 'Include Rangeslider', 
                  'value': 'slider'}],
        value=['slider']
    ),
    dcc.Graph(id="graph"),
    html.Br(),
    html.Div(id='body-div'),
    html.Br(),
    html.Div([
    html.Div([
    html.Button('Update data', id='update-data-button'),
    ]),
    html.Div([
    html.Button('predict data', id='predict-data-button'),
    ]),
    ])

])



df = get_df()

def Candlestick_fig(df: DataFrame):
  fig = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
  fig 

  return fig


@app.callback(
    Output("graph", "figure"), 
    [Input("toggle-rangeslider", "value")])

def display_candlestick(value):
    
    fig = Candlestick_fig(df)
    fig.update_layout(
        xaxis_rangeslider_visible='slider' in value
    )

    return fig    


@app.callback(
    Output("body-div", "children"),
    Input("predict-data-button", "n_clicks")
)
def change_text(n_clicks):
      """
      funcion para predecir 

      """
      if n_clicks is None:
        raise PreventUpdate
      else:
        y_pred=- -0.00566196
        datos = f" el modelo predice : {y_pred}"
        return datos
      


if __name__ == '__main__':
	app.run_server( debug=True) 
