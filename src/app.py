from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


df = pd.read_csv("../data/processed_wage.csv")


app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])

server = app.server

app.layout = html.Div([
    html.H1("NY state wages EDA dashboard"),
    html.Label("Select X-axis column for box plot:"),
    dcc.Dropdown(
        id='xcol-widget',
        value=' Area Name',  
        options=[' Area Name', ' Occupational Title']),
    html.Label("Select Y-axis column for box plot:"),
    dcc.Dropdown(
        id='ycol-widget',
        value='Mean Wage',  
        options=[' Employment', 'Mean Wage', ' Median Wage',' Entry Wage', ' Experienced Wage'],
        style={'margin-bottom': '50px'} ),

    html.Iframe(
        id='iframe-box',
        style={'border-width': '0', 'width': '100%', 'height': '600px'}),


    html.Label("Select column for the histogram below:"),
    dcc.Dropdown(
        id='hist-widget',
        value=' Entry Wage',  
        options=[{'label': col, 'value': col} for col in df.columns],
        style={'margin-bottom': '50px'}),


    html.Iframe(
        id='iframe-histogram',
        style={'border-width': '0', 'width': '100%', 'height': '600px'}),

    
    
], style={'backgroundColor': '#209de6'})





@app.callback(
    Output('iframe-histogram', 'srcDoc'),
    Input('hist-widget', 'value')
)
def histogram(hist_col):
    fig = px.histogram(df, x=hist_col)
    fig.update_layout(title=f'Histogram of {hist_col}', xaxis_title=hist_col, yaxis_title='Number of observations')
    return fig.to_html(full_html=False)

@app.callback(
    Output('iframe-box', 'srcDoc'),
    [Input('xcol-widget', 'value'),
     Input('ycol-widget', 'value')]
)
def box(xcol, ycol):
    fig = px.box(df, x=xcol, y=ycol, color=' Area Name')
    fig.update_layout(title=f'Box plot of {xcol} vs {ycol}', xaxis_title=xcol, yaxis_title=ycol)
    return fig.to_html(full_html=False)


if __name__ == '__main__':
    app.run_server(debug=True)
