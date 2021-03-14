import dash_html_components as html
from dash_html_components.H1 import H1
import pandas as pd

from dash import Dash
from .components import *
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from FlaskApp.utils.Model import AE
from glob import glob
import os
from glob import glob
import plotly.graph_objects as go

# Calling our Model
model = AE()

def prediction():    
    for file in glob('.//File//*.csv'):
        if not (file.endswith("normal.csv")):
            data_path = file
            print(f"[INFO] data_path : {data_path}")
            data = pd.read_csv(data_path)
            print(f"[INFO] data : {data.values}")
            preds = model.predict(data.values)
            return data, preds
    return None
    

print(f"[INFO] files inside File: {os.listdir('.//File')}")

def init_dashboard(server):

    print(f"[INFO] cwd for dash : {os.getcwd()}")
    dashApp = Dash(server = server,
                    routes_pathname_prefix="/analysis/",
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    title="Analysis"
                )

    dashApp._favicon = ".//assest//favicon.ico"
    print(f"[INFO] assets : {dashApp._assets_files}")
    print(f"[INFO] dashApp favicon : {dashApp._favicon}")
    
    dashApp.layout = html.Div(id= "dash-container", children=[
           
            html.H1("Analysis"),
            dcc.Markdown(id='verdict'),
            dcc.Markdown(id='loss'),
            dcc.Graph(id='ecgs',),  
            button,          
        ],
        style={
            "textAlign" : "center",
            'backgroundColor':'#111111',
            'color': '#7FDBFF',
            }
        )

    init_callbacks(dashApp)
    
    return dashApp.server


def init_callbacks(app):
    print(f"[INFO] Inside init_callbacks()...")
    print(f"[INFO] prediction: {prediction()}")

    # To update graph and model output when button is clicked
    @app.callback(
        Output(component_id='verdict', component_property='children'),
        Output(component_id='loss', component_property='children'),
        Output(component_id='ecgs', component_property='figure'),
        Input(component_id="show-results", component_property='n_clicks')
    )
    def modelVerdict(n_clicks):
        print("[INFO] Inside modelVerdict()..")
        print(f"[INFO] n_clicks : {n_clicks}")
        
        figure = go.Figure()
        # if (n_clicks == None):
        normal_ecg = pd.read_csv(".//File//normal.csv", header=None)
        print(f"[INFO] Normal ECG: {normal_ecg.values}")
        normal_curve = {
            'time':[d for d in range(len(normal_ecg.values[1]))],
            'values':normal_ecg.values[1]
        }

        
        figure.add_trace(go.Scatter(x = normal_curve['time'], y = normal_curve['values'], name = 'Normal ECG'))
        figure.update_layout(
                plot_bgcolor='#111111',
                paper_bgcolor='#111111',
                font_color='#7FDBFF',
                xaxis_title = 'Time Stamps',
                yaxis_title = 'Potentials',
                title = {
                        'text' : "Normal Electrocardiogram",
                        'xanchor' : 'center',
                        'x':0.5
                    }    
            )



        if (prediction() != None and n_clicks != None):
            data, preds = prediction()
            print(f"[INFO] preds : {preds}")
            print(f"[INFO] data.shape : {data.shape}")
            print(f"[INFO] data : {data}")
            # time_stamps = [d for d in range(len(data.values[1]))]
            figure.add_trace(go.Scatter(
                                    x =  normal_curve['time'], 
                                    y = data.values[0],
                                    name = f"User's ECG"
                            ))
            figure.update_layout(
                title = {'text':"Normal vs User's ECG",
                        'xanchor' : 'center',
                        'x':0.5        
                }
            )
            print(f"[INFO] loss : {preds['loss']}")
            verdict = f"## Verdict: {preds['verdict']}"
            loss = f"## Abnormality: {str(100*(round(1 - preds['loss'], 2)))}"
            return verdict, loss, figure
        return "CLick on the button to compare the result", "", figure
    
    
   
