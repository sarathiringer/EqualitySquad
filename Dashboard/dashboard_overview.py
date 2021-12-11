import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
from dash_table.Format import Format

parentDirectory = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(parentDirectory, 'Data')   
pd.options.display.float_format = '${:.2f}'.format

pd.set_option('display.max_columns', None)

['occupation_level4_number', 'occupation_level4', 'n_sickcase_per1000',
       'n_sickcase_per1000_f', 'n_sickcase_per1000_m', 'avg_sickdays',
       'avg_sickdays_f', 'avg_sickdays_m', 'n_emp', 'n_emp_f', 'n_emp_m',
       'stw_pay_quota_2014', 'stw_pay_quota_2015', 'stw_pay_quota_2016',
       'stw_pay_quota_2017', 'stw_pay_quota_2018', 'uw_pay_quota_2014',
       'uw_pay_quota_2015', 'uw_pay_quota_2016', 'uw_pay_quota_2017',
       'uw_pay_quota_2018', 'index_health', 'index_power', 'index_pay',
       'index_distribution', 'index_total_geometric', 'index_total_aritmetic'],

file = "\output_data.csv"
df = pd.read_csv(path + file)

#print(input_df.head())

app = dash.Dash(__name__)

TEMPLATE = 'plotly_white'



app.layout = html.Div([
    html.H1("Gender Equality Index", 
        style={'color': '#3da4ab', 
        'fontSize': 44, 
        'text-align' : 'center',
        'font-family' : 'Gill Sans',
        }),
    dcc.Graph(id='overview'),
    html.Div(children=[
        html.P("Which factors do your care about?",
            style={'color': '#3da4ab', 
            'fontSize': 19, 
            'text-align' : 'center',
            'font-family' : 'Gill Sans',
            }
        ),
        dcc.Checklist(
            id = 'checklist',
            options=[
                {'label': 'Health', 'value': 'health'},
                {'label': 'Overall distribution', 'value': 'distribution'},
                {'label': 'Pay', 'value': 'pay'}
            ],
            value=['health', 'distribution', 'pay'],
            style={'fontSize': 18, 
                'text-align' : 'center',
                'font-family' : 'Gill Sans',
            }
        ),
        ],
        style={'width': '50%', 'padding' : 50, 'margin' : '0 auto'},
    ),
])

@app.callback(
    Output(component_id="overview", component_property="figure"), 
    [Input(component_id="checklist", component_property="value")])
def display_overview(options_chosen):
    if 'overview' in options_chosen:
        op = 1
    else:
        op = 0.2
    fig = go.Figure(data=[go.Table(
    columnwidth = [2, 1, 1, 1, 1, 1, 1],
    header=dict(values=list(
        ['Occupation','Index Health', 'Index Power', 'Index Pay',
        'Index Distribution', 'Index Total Geometric', 'Index Total Aritmetic']),
                fill_color='#fe8a71',
                align='left'),
    cells=dict(values=[df.occupation_level4, df.index_health, df.index_power, df.index_pay, df.index_distribution, df.index_total_geometric, df.index_total_aritmetic],
               fill_color='#3da4ab',
               #sort_action="native",
               format=[None, 
               			",.2f", ",.2f", ".2f", 
               			",.2f", ",.2f", ".2f"],
               align='left'))
    ])
    fig.update_layout(
        template=TEMPLATE,
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
