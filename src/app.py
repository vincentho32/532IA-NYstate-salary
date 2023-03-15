from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


df = pd.read_csv("data/processed_wage.csv")


app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])

server = app.server

app.layout = html.Div([
    html.H1("NY state wages EDA dashboard"),
    html.Label("Select X-axis column for both plots:"),
    dcc.Dropdown(
        id='xcol-widget',
        value=' Area Name',  
        options=[{'label': col, 'value': col} for col in df.columns]),
    html.Label("Select Y-axis column for both plots:"),
    dcc.Dropdown(
        id='ycol-widget',
        value=' Area Name',  
        options=[{'label': col, 'value': col} for col in df.columns]),
    html.Iframe(
        id='iframe-scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    html.Iframe(
        id='iframe-histogram',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    
], style={'backgroundColor': '#209de6'})


@app.callback(
    Output('iframe-scatter', 'srcDoc'),
    Input('xcol-widget', 'value'),
    Input('ycol-widget', 'value')
)
def scatter(xcol, ycol):
    fig = go.Figure(data=go.Scatter(x=df[xcol], y=df[ycol], mode='markers'))
    fig.update_layout(title=f'Scatter Plot of {xcol} vs {ycol}', xaxis_title=xcol, yaxis_title=ycol)
    return fig.to_html(full_html=False)


@app.callback(
    Output('iframe-histogram', 'srcDoc'),
    Input('xcol-widget', 'value')
)
def histogram(xcol):
    fig = go.Figure(data=go.Histogram(x=df[xcol]))
    fig.update_layout(title=f'Histogram of {xcol}', xaxis_title=xcol, yaxis_title='Count')
    return fig.to_html(full_html=False)





if __name__ == '__main__':
    app.run_server(debug=True)

