import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_table
import pandas as pd
import os

parentDirectory = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(parentDirectory, 'Data')   

file = "\output_data.csv"
df = pd.read_csv(path + file)[['occupation_level4','index_health', 'index_power', 
        'index_pay', 'index_distribution', 'index_total_geometric', 
        'index_total_aritmetic']]

df[' index'] = range(1, len(df) + 1)

app = dash.Dash(__name__)

TEMPLATE = 'plotly_white'

PAGE_SIZE = 5

app = dash.Dash(TEMPLATE)

app.layout = html.Div([
    html.H1("Gender Equality Index", 
        style={'color': '#3da4ab', 
        'fontSize': 44, 
        'text-align' : 'center',
        'font-family' : 'Gill Sans',
        }),
    dash_table.DataTable(
        id='table-paging-and-sorting',
        columns=[
            {'name': i, 'id': i, 'deletable': True} for i in sorted(df.columns)
        ],
        page_current=0,
        page_size=PAGE_SIZE,
        page_action='custom',

        sort_action='custom',
        sort_mode='single',
        sort_by=[]
    ),
])


@app.callback(
    Output('table-paging-and-sorting', 'data'),
    Input('table-paging-and-sorting', "page_current"),
    Input('table-paging-and-sorting', "page_size"),
    Input('table-paging-and-sorting', 'sort_by'))
def update_table(page_current, page_size, sort_by):
    if len(sort_by):
        dff = df.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = df

    return dff.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)